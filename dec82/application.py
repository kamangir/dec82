from blue_sbc import application
import logging

logger = logging.getLogger(__name__)


class Application(application.Application):
    def __init__(self):
        super().__init__()
