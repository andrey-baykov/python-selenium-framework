"""
File to handle simple logging as example
"""
import logging


def setup_logging():
    logger = logging.getLogger('sauceDemo')
    logger.setLevel(logging.DEBUG)

    f_handler = logging.FileHandler('sauceDemo.log', mode='w')
    f_handler.setLevel(logging.DEBUG)
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)

    return logger
