from app_logging.decorators.log_decorator import LogDecorator
import pytest

@LogDecorator
def just_function():
    return "Done"

class TestLogger:
    def test_read(self, capsys):
        result = just_function()
        captured = capsys.readouterr()

        # assert "Logging" in captured.out
        assert result == "Done"

if __name__ == '__main__':
    pytest.main()
