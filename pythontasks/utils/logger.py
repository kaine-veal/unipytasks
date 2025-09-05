import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path    

def create_logger():

    # '__file__' is the path of the current python file. Path(__file__) turns the string into a path object so .resolve and .parent can be used
    # .resolve converts it into an absolute path. .parent moves one level up from the file to the containing folder
    # 'current_directory' is the folder where this logger.py file lives
    current_directory = str(Path(__file__).resolve().parent)

    # Takes the folder I just got (/Users/vealk1/VSCODE/py_projects/unipytasks/pythontasks/utils)
    # Wraps it back into a Path object so .parent can be used again. This file path then moves one level up again.
    # Resultant directory will be /Users/vealk1/VSCODE/py_projects/unipytasks/logs/seq_logger.log
    parent_directory = Path(current_directory).parent.parent

    
    logger = logging.getLogger('seq_logger') # Create logger
    # Setting the root default logger level to DEBUG to capture everything.
    # DEBUG is the lowest built-in level, meaning it will 'see' every message (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logger.setLevel(logging.DEBUG) 

    # Creates a stream handler
    stream_handler = logging.StreamHandler() # Creates a streamhandler to print to console
    stream_handler.setLevel(logging.DEBUG) # Only handle messages DEBUG or higher
    stream_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s") # This defines how log messages should look on the console
    stream_handler.setFormatter(stream_formatter) # Apply the above format to the stream handler

    # Creates a rotating file handler
    file_handler = RotatingFileHandler(str(parent_directory) + '/logs/seq_logger.log',
                                       maxBytes=500000,
                                       backupCount=2)
    file_handler.setLevel(logging.ERROR) # Only write ERROR and CRITICAL to logs/seq_logger.log to avoid filling disk with DEBUG/INFO/WARNING
    file_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s") # Same formatting as stream handler
    file_handler.setFormatter(file_formatter) # Apply the above format to the file handler

    # Attach both handlers to the logger
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger

logger = create_logger()