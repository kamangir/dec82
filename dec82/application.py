from abcli.modules.cookie import cookie
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from abcli import string
import logging

logger = logging.getLogger(__name__)

RST = None  # on the PiOLED this pin isnt used


class Application(object):
    def __init__(self):
        logger.info(f"{self.__class__.__name__} initialized.")

        self.line_count = 8
        self.line_length = 21

        self.history = []

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

    def log(self, line):
        self.history = self.line_count * ([""]) + ["", line, ""]

    def process_image(self, frame, image):
        self.log(f"frame #{frame}: {string.pretty_shape_of_matrix(image)}")

    def process_message(self, message):
        self.log(message.process_message())
        return None

    def step(self, session):
        ...

    def update_screen(self, session):
        self.history = self.history[1:]

        if len(self.history) < self.line_count:
            self.history += (" | ".join(session.signature())).split(" | ")

        self.draw.rectangle(
            (0, 0, self.display.width, self.display.height),
            outline=0,
            fill=0,
        )

        for row in range(self.line_count):
            self.draw.text(
                (0, self.top + 8 * row),
                self.history[row],
                font=self.font,
                fill=255,
            )

        self.display.image(self.image)
        self.display.display()
