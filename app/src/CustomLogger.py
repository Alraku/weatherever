import logging

class CustomFormatter(logging.Formatter):

    green = "\x1b[32;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format_time = "%(name)s %(asctime)s %(message)s"
    format_desc = "%(message)s"
    
    FORMAT = {
        logging.INFO: green + format_time + reset,
        logging.ERROR: red + format_desc + reset,
        logging.CRITICAL: bold_red + format_desc + reset}

    def format(self, record):
        time_format = '[%H:%M:%S] %A, %-d %B %Y '
        log_fmt = self.FORMAT.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt=time_format)
        return formatter.format(record)

    def get_logger(self):

        # create logger with 'spam_application'
        logger = logging.getLogger("[WEATHER APP]:")
        logger.setLevel(logging.DEBUG)

        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(CustomFormatter())
        logger.addHandler(ch)

        return logger


# formatter = ColoredFormatter(log_format, datefmt=time_format)