import logging

FORMAT = '%(asctime)-s : %(levelname)-8s : %(name)s (LN %(lineno)d) : %(message)s %(levelno)d'
DATE_FMT = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(format=FORMAT, datefmt=DATE_FMT)

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

logger.debug(f"Sent `debug` message.")
logger.info(f"Sent `info` message.")
logger.warning(f"Sent `warning` message.")
logger.critical(f"Sent `critical` message.")
logger.error(f"Sent `error` message.")
