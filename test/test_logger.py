from app_logging.decorators.log_decorator import LogDecorator
from app_logging.log_utils import Logger
import pytest
import os
import tempfile


class TestLogger:
    """Test suite for the Logger and LogDecorator functionality."""

    @pytest.fixture
    def temp_log_file(self):
        """Create a temporary log file for testing."""
        temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.log')
        temp_path = temp_file.name
        temp_file.close()
        yield temp_path
        # Cleanup after test
        if os.path.exists(temp_path):
            os.remove(temp_path)

    def test_logger_creation(self, temp_log_file):
        """Test that Logger creates a logger instance successfully."""
        logger_instance = Logger(log_file=temp_log_file)
        logger = logger_instance.get_logger()

        assert logger is not None
        assert logger.name == "AppLogger"
        assert logger.level == 10  # DEBUG level

    def test_logger_writes_to_file(self, temp_log_file):
        """Test that Logger writes log messages to the file."""
        logger_instance = Logger(log_file=temp_log_file)
        logger = logger_instance.get_logger()

        test_message = "Test log message"
        logger.info(test_message)

        # Force flush handlers
        for handler in logger.handlers:
            handler.flush()

        # Read the log file and verify content
        with open(temp_log_file, 'r') as f:
            content = f.read()
            assert test_message in content
            assert "INFO" in content

    def test_logger_different_levels(self, temp_log_file):
        """Test that Logger handles different log levels correctly."""
        logger_instance = Logger(log_file=temp_log_file)
        logger = logger_instance.get_logger()

        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")

        # Force flush handlers
        for handler in logger.handlers:
            handler.flush()

        with open(temp_log_file, 'r') as f:
            content = f.read()
            assert "DEBUG" in content
            assert "INFO" in content
            assert "WARNING" in content
            assert "ERROR" in content

    def test_log_decorator_basic_function(self, temp_log_file):
        """Test LogDecorator on a simple function."""
        decorator = LogDecorator(debug_enabled=True)

        @decorator.log_this
        def simple_function():
            return "Success"

        result = simple_function()
        assert result == "Success"

    def test_log_decorator_with_arguments(self, temp_log_file):
        """Test LogDecorator on a function with arguments."""
        decorator = LogDecorator(debug_enabled=True)

        @decorator.log_this
        def add_numbers(a, b):
            return a + b

        result = add_numbers(5, 3)
        assert result == 8

    def test_log_decorator_with_exception(self, temp_log_file):
        """Test that LogDecorator properly logs exceptions."""
        decorator = LogDecorator(debug_enabled=True)

        @decorator.log_this
        def failing_function():
            raise ValueError("Test exception")

        with pytest.raises(ValueError, match="Test exception"):
            failing_function()

    def test_log_decorator_debug_mode(self, temp_log_file):
        """Test LogDecorator with debug mode enabled vs disabled."""
        # Test with debug enabled
        decorator_debug = LogDecorator(debug_enabled=True)

        @decorator_debug.log_this
        def debug_function(x):
            return x * 2

        result = debug_function(5)
        assert result == 10

        # Test with debug disabled
        decorator_no_debug = LogDecorator(debug_enabled=False)

        @decorator_no_debug.log_this
        def no_debug_function(x):
            return x * 3

        result = no_debug_function(5)
        assert result == 15


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
