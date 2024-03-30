from pathlib import Path
import logging
from colorlog import ColoredFormatter
from logging.handlers import RotatingFileHandler

def get_logger(name, fname, s_lvl, f_lvl):
    """Return a logger with a default ColoredFormatter."""
    color_formatter = ColoredFormatter(
        "%(log_color)s[%(levelname).1s][%(asctime)s][%(filename)s:%(lineno)d]:%(message)s",
        datefmt='%H:%M:%S',
        reset=True,
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'bold_red',
        }
    )

    formatter = logging.Formatter(
        "[%(levelname).1s][%(asctime)s][%(filename)s:%(lineno)d]:%(message)s",
        datefmt='%Y%m%d %H:%M:%S'
    )

    logger = logging.getLogger(name)
    #add handler at first time call
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)

        s_handler = logging.StreamHandler()
        s_handler.setFormatter(color_formatter)
        s_handler.setLevel(s_lvl)
        logger.addHandler(s_handler)
        f_handler = RotatingFileHandler(Path(fname).with_suffix(".log"), maxBytes=10000000, backupCount=5)
        f_handler.setFormatter(formatter)
        f_handler.setLevel(f_lvl)
        logger.addHandler(f_handler)

    return logger

'''
#!/usr/bin/env python3

import pyutils.logging as dlog
import logging

log = dlog.get_logger("test", __file__, logging.DEBUG, logging.DEBUG)

log.debug("this is debug")
log.info("this is info")
log.warning("this is warning")
log.error("this is error")
log.critical("this is critical")
'''

''' import from other folder
#!/usr/bin/env python3

import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import pyutils.logging as dlog
import logging
'''