# logger.py
"""
Utility module for logging across the AI ROBOPET ecosystem.
"""

import logging

def setup_logger(name, log_file, level=logging.INFO):
    """
    Set up a logger with the specified name, log file, and level.
    
    :param name: Name of the logger
    :param log_file: File path for logging output
    :param level: Logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
    :return: Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger

# Example usage
if __name__ == "__main__":
    app_logger = setup_logger("app_logger", "app.log")
    app_logger.info("Logger is set up and running.")
