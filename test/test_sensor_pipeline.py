import pytest
from app.sensor_manager.sensor_pipeline import SensorPipeline

class TestSensorManager:

    @pytest.fixture
    def sensor(self):
        # Mock or initialize with test config
        return SensorPipeline()

    def test_read(self, sensor):

        result = sensor.read()

        assert result is not None, "Sensor read returned None"
        assert isinstance(result, dict), "Expected dict from sensor read"
        assert 'temperature' in result, "Missing 'temperature' in read output"
        assert 'humidity' in result, "Missing 'humidity' in read output"

        assert 0 <= result['temperature'] <= 100, "Temperature out of expected range"
        assert 0 <= result['humidity'] <= 100, "Humidity out of expected range"


if __name__ == '__main__':
    pytest.main()
