import pytest
import json
from app import create_app


class TestFlaskApi:
    """Comprehensive test suite for Flask API endpoints."""

    @pytest.fixture(autouse=True)
    def setup_app(self):
        """Setup Flask test client before each test."""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_home_route_returns_200(self):
        """Test that the home route returns HTTP 200."""
        response = self.client.get("/")
        assert response.status_code == 200

    def test_home_route_returns_message(self):
        """Test that the home route returns the expected message."""
        response = self.client.get("/")
        assert b"LocalEdge is up and running!" in response.data

    def test_index_html_template_renders(self):
        """Test that the index HTML template renders successfully."""
        response = self.client.get("/")
        assert response.status_code == 200
        assert b"<!DOCTYPE html>" in response.data or b"LocalEdge" in response.data

    def test_dht22_endpoint_exists(self):
        """Test that DHT22 endpoint exists and accepts POST requests."""
        response = self.client.post("/dht22")
        # Should return 200 or similar, not 404
        assert response.status_code != 404

    def test_dht22_with_valid_data(self):
        """Test DHT22 endpoint with valid sensor data."""
        test_data = "temp=25.5,humidity=60.2"
        response = self.client.post(
            "/dht22",
            data=test_data,
            content_type="text/plain"
        )
        assert response.status_code in [200, 201]
        assert response.is_json or response.content_type == "application/json"

    def test_dht22_returns_json(self):
        """Test that DHT22 endpoint returns JSON response."""
        test_data = "temp=22.0,humidity=55.0"
        response = self.client.post("/dht22", data=test_data)
        try:
            json.loads(response.data)
            assert True
        except json.JSONDecodeError:
            assert False, "Response is not valid JSON"

    def test_ens160_endpoint_exists(self):
        """Test that ENS160 endpoint exists and accepts POST requests."""
        response = self.client.post("/ens160")
        # Should return 200 or similar, not 404
        assert response.status_code != 404

    def test_ens160_with_valid_data(self):
        """Test ENS160 endpoint with valid sensor data."""
        test_data = "aqi=2,tvoc=150,eco2=400"
        response = self.client.post(
            "/ens160",
            data=test_data,
            content_type="text/plain"
        )
        assert response.status_code in [200, 201]

    def test_ens160_returns_json(self):
        """Test that ENS160 endpoint returns JSON response."""
        test_data = "aqi=1,tvoc=100,eco2=380"
        response = self.client.post("/ens160", data=test_data)
        try:
            json.loads(response.data)
            assert True
        except json.JSONDecodeError:
            assert False, "Response is not valid JSON"

    def test_invalid_route_returns_404(self):
        """Test that invalid routes return 404 Not Found."""
        response = self.client.get("/invalid-endpoint")
        assert response.status_code == 404

    def test_dht22_method_not_allowed(self):
        """Test that DHT22 endpoint rejects GET requests."""
        response = self.client.get("/dht22")
        assert response.status_code == 405  # Method Not Allowed

    def test_ens160_method_not_allowed(self):
        """Test that ENS160 endpoint rejects GET requests."""
        response = self.client.get("/ens160")
        assert response.status_code == 405  # Method Not Allowed

    def test_dht22_with_empty_data(self):
        """Test DHT22 endpoint with empty payload."""
        response = self.client.post("/dht22", data="")
        # Should handle gracefully, not crash
        assert response.status_code in [200, 400, 422]

    def test_ens160_with_empty_data(self):
        """Test ENS160 endpoint with empty payload."""
        response = self.client.post("/ens160", data="")
        # Should handle gracefully, not crash
        assert response.status_code in [200, 400, 422]

    def test_app_is_in_testing_mode(self):
        """Test that app is configured for testing."""
        assert self.app.config['TESTING'] is True

    def test_multiple_dht22_requests(self):
        """Test that multiple DHT22 requests can be handled."""
        responses = []
        for i in range(3):
            data = f"temp={20 + i},humidity={50 + i}"
            response = self.client.post("/dht22", data=data)
            responses.append(response)

        # All requests should succeed
        for response in responses:
            assert response.status_code in [200, 201]


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
