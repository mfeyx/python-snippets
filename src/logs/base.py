import logging
from functools import wraps
from typing import Callable, Union

FORMAT = '%(asctime)-s : %(levelname)-8s : %(name)s (LN %(lineno)d) : %(message)s %(levelno)d'
DATE_FMT = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(FORMAT)
LEVELS  = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "critical": logging.CRITICAL,
    "error": logging.ERROR,
}


class MyLogger:
    def __init__(self, level: str):
        level = LEVELS.get(level)
        logging.basicConfig(level=level)

    def get_logger(self, name=None):
        return logging.getLogger(name)

def get_default_logger(level: str):
    return MyLogger(level).get_logger()

def log(_func=None, *, level: str = "info", my_logger: Union[MyLogger, logging.Logger] = None):
    def decorator_log(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if my_logger is None:
                logger = get_default_logger(level)
            else:
                if isinstance(my_logger, MyLogger):
                    logger = my_logger.get_logger(func.__name__)
                else:
                    logger = my_logger
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            logger.debug(f"function {func.__name__} called with args {signature}")
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                logger.exception(f"Exception raised in {func.__name__}. exception: {str(e)}")
                raise e
        return wrapper

    if _func is None:
        return decorator_log
    else:
        return decorator_log(_func)
