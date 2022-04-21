import logging

class CustomFormatter(logging.Formatter):

    green = "\x1b[32;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    bold_blue = "\033[34;1m"
    reset = "\x1b[0m"
    format_time = "%(name)s %(asctime)s %(message)s"
    format_desc = "%(message)s"
    
    FORMAT = {
        logging.INFO: bold_blue + format_time + reset,
        logging.ERROR: red + format_desc + reset,
        logging.CRITICAL: bold_red + format_desc + reset}

    def format(self, record):
        time_format = '[%H:%M:%S]\n%A, %-d %B %Y '
        log_fmt = self.FORMAT.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt=time_format)
        return formatter.format(record)

    def get_logger(self):

        # create logger with 'spam_application'
        logger = logging.getLogger("[WEATHER APP]")
        logger.setLevel(logging.DEBUG)

        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(CustomFormatter())
        logger.addHandler(ch)

        return logger

# formatter = ColoredFormatter(log_format, datefmt=time_format)
# ct = ColoredText()
# ct.prCyan("Hello World")


class Colors():

    RESET = '\033[0m'
    BOLD = '\033[01m'
    DISABLE = '\033[02m'
    UNDERLINE = '\033[04m'
    REVERSE = '\033[07m'
    STRIKETHROUGH = '\033[09m'
    INVISIBLE = '\033[08m'

    class FG():

        BLACK = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        ORANGE = '\033[33m'
        BLUE = '\033[34m'
        PURPLE = '\033[35m'
        CYAN = '\033[36m'
        WHITE = '\033[37m'
        GREY = '\033[90m'

    class BG():

        BLACK = '\033[40m'
        RED = '\033[41m'
        GREEN = '\033[42m'
        ORANGE = '\033[43m'
        BLUE = '\033[44m'
        PURPLE = '\033[45m'
        CYAN = '\033[46m'
        WHITE = '\033[47m'
 

class ColoredText():

    def prRed(self, skk): print("\033[91m {}\033[00m" .format(skk))
    def prGreen(self, skk): print("\033[92m {}\033[00m" .format(skk))
    def prYellow(self, skk): print("\033[93m {}\033[00m" .format(skk))
    def prLightPurple(self, skk): print("\033[94m {}\033[00m" .format(skk))
    def prPurple(self, skk): print("\033[95m {}\033[00m" .format(skk))
    def prCyan(self, skk): print("\033[96m {}\033[00m" .format(skk))
    def prLightGray(self, skk): print("\033[97m {}\033[00m" .format(skk))
    def prBlack(self, skk): print("\033[98m {}\033[00m" .format(skk))


