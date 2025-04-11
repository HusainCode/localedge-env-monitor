#  Purpose:
#     Provides a centralized app_logging utility to log messages of various severity levels
#     (INFO, WARNING, ERROR) to a file for monitoring and debugging.
#
#  Key Attributes:
#
#
#  Main Methods:
#     info(message): Logs informational messages
#     warning(message): Logs warning messages
#     error(message): Logs error messages
#
#  Example:

# File Header: app/app_logging/log_utils.py

import logging
import os


class Logger:
    def __init__(self, log_file=None):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        log_path = log_file or os.path.join(base_dir, os.getenv("LOG_FILE", "app/logs/log.txt"))

        # Creates the directories if they don't exist. Just like mkdir -p in linux
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        self.log_path = log_path  # Fix: ensure log_path is stored for use in get_logger

    def get_logger(self) -> logging:
        self.logger = logging.getLogger("AppLogger")
        self.logger.setLevel(logging.DEBUG)

        if not self.logger.handlers:
            file_handler = logging.FileHandler(self.log_path)

            # asctime: Timestamp
            # levelname: Log level
            # message: the log message
            formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s",
                                          "%Y-%m-%d %H:%M:%S")  # time format
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        return self.logger
