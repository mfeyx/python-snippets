import logging


logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

def hello():
    logger.debug(f"hello from `module1`")
    logger.info(f"hello from `module1`")
    logger.warning(f"hello from `module1`")
    logger.critical(f"hello from `module1`")
    logger.error(f"hello from `module1`")
