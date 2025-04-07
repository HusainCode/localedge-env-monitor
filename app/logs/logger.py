#  Purpose:
#     Provides a centralized logging utility to log messages of various severity levels
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

import logging
import os

class Logger:
    def __init__(selfself,log_file=None):
        base_dir = None
        log_path = None