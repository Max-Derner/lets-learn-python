import logging
from traceback import TracebackException
import os
from typing import List, Union

# assigns a logger to the logger variable
logger = logging.getLogger('my_magic_logger')
# 'my_magic_logger' can be anything and gives the logger a name
# if two loggers have the same name, they will be the exact same logger (singleton object)
logger.setLevel(logging.DEBUG)  # sets the default level


# Let me point you to these docs for more info:
# https://docs.python.org/3/library/logging.html
# https://docs.python.org/3/howto/logging.html
# https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook
# https://docs.python.org/3/library/logging.html#logrecord-attributes

_ROOT_FILE_NAME = 'Python-Lessons'
_ROOT_DIR_PATH = os.path.dirname(os.path.abspath(_ROOT_FILE_NAME))
_LOGGER_FILE_NAME_FOR_CONSOLE_OUTPUT = 'console_output.log'
_LOGGER_FILE_NAME_FOR_DEBUG_OUTPUT = 'debug_output.log'
_CONSOLE_OUTPUT_FILE_PATH = f'{_ROOT_DIR_PATH}/{_LOGGER_FILE_NAME_FOR_CONSOLE_OUTPUT}'
_DEBUG_OUTPUT_FILE_PATH = f'{_ROOT_DIR_PATH}/{_LOGGER_FILE_NAME_FOR_DEBUG_OUTPUT}'

_CONSOLE_LOG_LEVEL = logging.INFO
_DEBUG_FILE_LOG_LEVEL = logging.DEBUG

handlers: List[logging.Handler]

config_message = 'NFT_logger configured:\n'
config_message += 'logging will go to 2 output files\n'
config_message += 'console output - '.ljust(18)
config_message += f'{_CONSOLE_OUTPUT_FILE_PATH}\n'
config_message += 'debug output - '.ljust(18)
config_message += f'{_DEBUG_OUTPUT_FILE_PATH}\n'


# -~- -~- -~- -~- -~- -~- -~- -~- -~- FORMATTERS -~- -~- -~- -~- -~- -~- -~- -~- -~-

def _get_debug_output_formatter() -> logging.Formatter:
    """dictates the format for our debug output"""
    debug_file_format = '%(levelname)s '  # debug, info, warning etc
    debug_file_format += 'from '
    debug_file_format += 'function "%(funcName)s" '  # which function does this output come from
    debug_file_format += 'in "%(pathname)s", '  # which file does this output come from
    debug_file_format += 'line %(lineno)s '  # which line does this output come from
    debug_file_format += 'at %(asctime)s '  # what time was this output given
    debug_file_format += '\n%(message)s\n'  # the output itself
    return logging.Formatter(fmt=debug_file_format)


def _get_console_output_formatter() -> logging.Formatter:
    """dictates the format for out console output"""
    console_format = '%(message)s'  # just the output
    return logging.Formatter(fmt=console_format)


# -~- -~- -~- -~- -~- -~- -~- -~- -~- HANDLERS -~- -~- -~- -~- -~- -~- -~- -~- -~-

def _get_stream_handler(level: int, formatter: logging.Formatter) -> logging.StreamHandler:
    """constructs a stream handler for the logger"""
    # stream handlers are what stream the output to your console
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level=level)
    stream_handler.setFormatter(fmt=formatter)
    return stream_handler


def _get_file_handler(level: int, filename: str, mode: str, formatter: logging.Formatter) -> logging.FileHandler:
    """constructs a file handler for the logger"""
    # file handlers are what handle streaming the output to a file
    file_handler = logging.FileHandler(filename=filename, mode=mode)
    file_handler.setLevel(level=level)
    file_handler.setFormatter(fmt=formatter)
    return file_handler


def _get_handlers() -> List[logging.Handler]:
    """constructs all the stream and file handlers we want in our logger"""

    # one stream handler to output into the console
    console_output_formatter = _get_console_output_formatter()
    console_stream_handler = _get_stream_handler(level=_CONSOLE_LOG_LEVEL,
                                                 formatter=console_output_formatter)

    # a filehandler to mirror console output into a file
    console_file_handler = _get_file_handler(level=_CONSOLE_LOG_LEVEL,
                                             filename=_CONSOLE_OUTPUT_FILE_PATH,
                                             mode='w',
                                             formatter=console_output_formatter)

    # another filehandler to provide detailed debugging info into a file
    debug_output_formatter = _get_debug_output_formatter()
    debug_file_handler = _get_file_handler(level=_DEBUG_FILE_LOG_LEVEL,
                                           filename=_DEBUG_OUTPUT_FILE_PATH,
                                           mode='w',
                                           formatter=debug_output_formatter)

    return [console_stream_handler, console_file_handler, debug_file_handler]


def _add_handlers(handlers: Union[List[logging.Handler], List[logging.FileHandler], List[logging.StreamHandler]]):
    """allows you to add a list of handlers to the logger in one go"""
    for handler in handlers:
        logger.addHandler(handler)


def _remove_handlers(handlers: Union[List[logging.Handler], List[logging.FileHandler], List[logging.StreamHandler]]):
    """allows you to remove a list of handlers in one go"""
    for handler in handlers:
        logger.removeHandler(handler)


def _extract_file_handlers(handlers: List[logging.Handler]) -> List[logging.FileHandler]:
    """takes a list of handlers and returns only the file handlers"""
    file_handlers = []
    for handler in handlers:
        if isinstance(handler, logging.FileHandler):
            file_handlers.append(handler)
    return file_handlers


def reset_file_handlers():
    """removes the file handlers, creates new ones, and puts the new ones back into the logger.
    Really only used in testing"""
    current_handlers: List[logging.Handler] = logger.handlers
    current_file_handlers = _extract_file_handlers(handlers=current_handlers)
    _remove_handlers(handlers=current_file_handlers)
    new_handlers = _get_handlers()
    new_file_handlers = _extract_file_handlers(handlers=new_handlers)
    _add_handlers(handlers=new_file_handlers)
    logger.info(config_message)


def get_output_file_paths() -> List[str]:
    """gives filenames of all filehandler outputs"""
    handlers = logger.handlers
    file_handlers = _extract_file_handlers(handlers=handlers)
    output_file_paths = []
    for file_handler in file_handlers:
        output_file_paths.append(file_handler.baseFilename)
    return output_file_paths


# -~- -~- -~- -~- -~- -~- -~- -~- -~- SET-UP -~- -~- -~- -~- -~- -~- -~- -~- -~-

def _set_up_nft_logger():
    """configures and assigns handlers to logger"""
    handlers = _get_handlers()
    _add_handlers(handlers=handlers)
    logger.info(config_message)


def exception_traceback_to_string(e: Exception):
    # TODO add this traceback object to it's own lesson
    trace_back = TracebackException(exc_type=e.__class__,
                                    exc_value=e,
                                    exc_traceback=e.__traceback__)
    return '\n'.join(trace_back.format(chain=True))


# this bit is always run when this module is imported, if there's no handlers on the logger, then we know it was never set up
if not logger.hasHandlers():
    _set_up_nft_logger()
