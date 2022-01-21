import datetime
from re import sub
from CustomLogger import CustomFormatter

logger = CustomFormatter.getLogger()
now = datetime.datetime.now()

logger.info(now)



























# logger.debug("debug message")
# logger.info("info message")
# logger.warning("warning message")
# logger.error("error message")
# logger.critical("critical message")