from abcli.modules.cookie import cookie
from abcli.timer import Timer
import logging

logger = logging.getLogger(__name__)


class Dec82(object):
    def __init__(self):
        logger.info(f"{self.__class__.__name__} initialized.")

        self.timer = Timer(
            cookie.get("dec82.screen.period", 2),
            "dec82.screen.period",
        )

        self.log = []

    def step(self):
        if self.timer.tick("wait"):
            self.log = self.log[1:]
