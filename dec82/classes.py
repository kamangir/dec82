import logging

logger = logging.getLogger(__name__)


class Dec82(object):
    def __init__(self):
        logger.info(f"{self.__class__.__name__} initialized.")

    def step(self):
        print(f"{self.__class__.__name__} step.")
