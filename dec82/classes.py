from abcli.modules.cookie import cookie
from abcli.timer import Timer
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from abcli import string
import logging

logger = logging.getLogger(__name__)

RST = None  # on the PiOLED this pin isnt used


class Dec82(object):
    def __init__(self):
        logger.info(f"{self.__class__.__name__} initialized.")

        self.timer = Timer(
            cookie.get("dec82.screen.period", 1),
            "dec82.screen.period",
        )

        self.line_count = 8
        self.line_length = 21

        self.hr = self.line_length * ["-"]

        self.log = []

        # https://github.com/IcingTomato/Seeed_Python_SSD1315/blob/master/examples/stats.py
        self.display = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

        self.display.begin()
        self.display.clear()
        self.display.display()

        self.image = Image.new(
            "1",
            (self.display.width, self.display.height),
        )

        self.draw = ImageDraw.Draw(self.image)

        # Draw a black filled box to clear the image.
        self.draw.rectangle(
            (0, 0, self.display.width, self.display.height),
            outline=0,
            fill=0,
        )

        self.padding = -2
        self.top = self.padding
        self.bottom = self.display.height - self.padding

        self.font = ImageFont.load_default()

    def process_image(self, frame, image):
        self.log += [
            self.hr,
            "",
            f"frame #{frame}: {string.pretty_shape_of_matrix(image)}",
            "",
            self.hr,
        ]

    def process_message(self, messages):
        self.log += [
            self.hr,
            "",
            message.process_message(),
            "",
            self.hr,
        ]
        return None

    def step(self, session):
        ...

    def update_screen(self, session):
        if len(self.log) < self.line_count:
            self.log += (" | ".join(session.signature())).split(" | ")

        if self.timer.tick("wait"):
            self.log = self.log[1:]

        self.draw.rectangle(
            (0, 0, self.display.width, self.display.height),
            outline=0,
            fill=0,
        )

        for row in range(min(self.line_count, len(self.log))):
            self.draw.text(
                (0, self.top + 8 * row),
                self.log[row],
                font=self.font,
                fill=255,
            )

        self.display.image(self.image)
        self.display.display()
