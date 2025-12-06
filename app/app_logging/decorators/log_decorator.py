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

"""
# Source: https://docs.python.org/3/library/logging.html

TABLE CONTEXT:
Level Numeric value What it means / When to use it

Logging.NOTSET 0 When set on a logger, indicates that ancestor loggers are to be consulted to determine the effective level. If that still resolves to NOTSET, then all events are logged. When set on a handler, all events are handled.

Logging.DEBUG 10 Detailed information, typically only of interest to a developer trying to diagnose a problem.

Logging.INFO 20 Confirmation that things are working as expected.

Logging.WARNING 30 An indication that something unexpected happened, or that a problem might occur in the near future (e.g. ‘disk space low’). The software is still working as expected.

Logging.ERROR 40 Due to a more serious problem, the software has not been able to perform some function.

Logging.CRITICAL 50 A serious error, indicating that the program itself may be unable to continue running
"""

import functools  # Provides tools to work with functions
import time  # used for timestamps (when an event happened)
import os  # to check environment variables
from typing import Callable  # Used in this code for readability. Returns something you can call, such a method

import logging
from app_logging.log_utils import Logger


class LogDecorator:
    """
       A reusable decorator class for structured function logging.
       Tracks:
       - function calls
       - success/failure
       - logs errors with full traceback
       """

    def __init__(self, debug_enabled: bool = True):
        self.logger = Logger().get_logger()

        # Allow debug mode. Its TRUE as of now. False for production level for cleaner logs
        self.debug_enabled = debug_enabled

    def start_timer(self):
        return time.time()  # Timer to track execution time

    def end_timer(self, start_time):
        return (time.time() - start_time) * 1000  # milliseconds (1 ms = 0.001 seconds)

    def log_this(self, func=None, level=logging.INFO) -> Callable:  # the parameter is the function you're going to decorate
        """
        Decorator factory: accepts a log level (default is INFO).
        Returns the actual decorator that wraps the targeted function.
        """

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                func_name = func.__name__  # stores the function name for cleaner code

                # If debug mode is True
                if self.debug_enabled:
                    self.logger.debug(f"Entering {func_name} with args={args} , kwargs={kwargs}")
                else:  # Use the stander log message
                    self.logger.info(f"Calling: {func_name}")

                start = self.start_timer()

                try:
                    result = func(*args, **kwargs)
                    duration_in_milliseconds = self.end_timer(start)

                    self.logger.log(level, f"{func_name} was completed in {duration_in_milliseconds:.2f}ms")

                    return result

                except Exception as e:
                    duration_in_milliseconds = self.end_timer(start)
                    self.logger.error(f"{func_name} failed with error {e} after {duration_in_milliseconds:.2f}ms",
                                      exc_info=True)  # exc_info=True is key for debugging.
                                                      # shows exactly where the error happened
                                                      # tells the logger to include the full traceback in the log
                    raise

            return wrapper

        if func is None:
            return decorator
        else:
            return decorator(func)
