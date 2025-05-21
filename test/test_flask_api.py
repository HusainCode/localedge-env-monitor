import pytest
from app import create_app

class TestFlaskApi:
    @pytest.fixture(autouse=True)
    def setup_app(self):
        self.app = create_app().test_client()

    def test_read(self):
        response = self.app.get("/")
        assert response.status_code == 200

if __name__ == '__main__':
    pytest.main()
