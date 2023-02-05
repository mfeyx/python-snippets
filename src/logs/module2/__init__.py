import logging


logger = logging.getLogger(__name__)

logger.setLevel(logging.WARNING)

def hello():
    logger.debug(f"hello from `module2`")
    logger.info(f"hello from `module2`")
    logger.warning(f"hello from `module2`")
    logger.critical(f"hello from `module2`")
    logger.error(f"hello from `module2`")
