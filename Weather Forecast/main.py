import datetime
import urllib.request
from CustomLogger import CustomFormatter

logger = CustomFormatter.getLogger()
now = datetime.datetime.now()

logger.info(now)

web = urllib.request.urlretrieve('https://www.youtube.com/embed/J9okBenAt-U', 'video_test.mp4')

print(web)

























# logger.debug("debug message")
# logger.info("info message")
# logger.warning("warning message")
# logger.error("error message")
# logger.critical("critical message")