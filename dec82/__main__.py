import argparse
from . import *
from blue_sbc.session import Session
from abcli import logging
import logging

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="start_session",
)
args = parser.parse_args()

success = False
if args.task == "start_session":
    success = Session.start(Dec82())
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
