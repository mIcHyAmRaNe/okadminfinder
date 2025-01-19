#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging


class LoggingConfig:
    @staticmethod
    def configure_logging(debug: bool):
        if debug:
            # Create a file handler for urllib3 logging
            urllib3_logger = logging.getLogger("urllib3")
            urllib3_logger.setLevel(logging.INFO)
            file_handler = logging.FileHandler("urllib3.log")
            file_handler.setLevel(logging.INFO)
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            file_handler.setFormatter(formatter)
            urllib3_logger.addHandler(file_handler)

            # Suppress urllib3 logging to the console
            urllib3_logger.propagate = False

            # Configure the root logger to show other logs
            logging.basicConfig(level=logging.INFO)
        else:
            # Disable all logging
            logging.basicConfig(level=logging.disable())
