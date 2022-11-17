from . import NAME
import time
from abcli import logging
import logging

logger = logging.getLogger(__name__)


def validate_hardware():
    from grove.grove_ryb_led_button import GroveLedButton

    ledbtn = GroveLedButton(5)

    while True:
        ledbtn.led.light(True)
        time.sleep(1)

        ledbtn.led.light(False)
        time.sleep(1)

        print("----")

    return True
