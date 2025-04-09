
#  Purpose:
#
#
#  Key Attributes:
#
#
#  Main Methods:
#
#
#  Example:

# File Header: app/decorators/log_decorator.py

import functools # Provides tools to work with functions
from app_logging.log_utils import Logger

class LogDecorator:
    def __init__(self):
        self.logger = Logger().get_logger()


    def log_this(self,func): # the parameter is the function you're going to decorate
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.logger.info(f"Calling: {func.__name__}")

            try:
                result = func(*args, **kwargs)
                self.logger.info(f"{func.__name__} completed successfully!")

                return result

            except Exception  as e:
                self.logger.error(f"{func.__name__} failed with error {e}")
                raise

        return wrapper

