import logging
import os
from logging import StreamHandler
from logging.handlers import RotatingFileHandler

WORK_DIR = "../data/"
DONE_DIR = WORK_DIR + "/done/"
FAIL_DIR = WORK_DIR + "/failed/"
NEW_DIR = WORK_DIR + "/new/"
INCOMPLETE_DIR = WORK_DIR + "/incomplete/"

BLOWFISH_KEY = ''.join(['\xDE', '\x72', '\xBE', '\xA0', '\xDE', '\x04', '\xBE', '\xB1',
                        '\xDE', '\xFE', '\xBE', '\xEF', '\xDE', '\xAD', '\xBE', '\xEF'])


GAME_TYPES = {
    1: "Random",
    2: "Training",
    3: "Company",
    4: "Tournament",
    5: "CW",
}


VEHICLE_TYPES = {
    '01': "USSR",
    '11': "Germany",
    '21': "USA",
    '31': "China",
    '41': "France",
    '51': "UK",
}

#Needed for decoding crits in details
VEHICLE_DEVICE_TYPE_NAMES = ('engine', 'ammoBay', 'fuelTank', 'radio', 'track', 'gun', 'turretRotator', 'surveyingDevice')
VEHICLE_TANKMAN_TYPE_NAMES = ('commander', 'driver', 'radioman', 'gunner', 'loader')

## Database
SQLITE_DB = os.path.abspath(os.path.dirname(__file__)) + "/wot.db"

from pysqlite2 import dbapi2 as sqlite3
db_conn = sqlite3.connect(SQLITE_DB)
db_conn.row_factory = sqlite3.Row


## Logging settings
default_formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
rtb_formatter = logging.Formatter("%(asctime)s: %(message)s")

console_handler = StreamHandler()
console_handler.setFormatter(default_formatter)

default_handler = RotatingFileHandler("parser.log", "a", 1024 * 5, 3)
default_handler.setLevel(logging.DEBUG)
default_handler.setFormatter(default_formatter)

root = logging.getLogger()
root.addHandler(console_handler)
root.addHandler(default_handler)
root.setLevel(logging.DEBUG)
