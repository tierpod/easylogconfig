"""Contains functions to configure log output.
"""

import logging
import logging.config
import logging.handlers
import os
import sys


DATE_FMT = "%Y-%m-%d/%H:%M:%S"


def configure(syslog_tag=None, log_file=None, debug=False, thread=True, datetime=True, **kwargs):
    if syslog_tag:
        to_syslog(tag="testtag", debug=debug, thread=thread)
    elif log_file:
        to_file(path=log_file, debug=debug, thread=thread, datetime=datetime)
    else:
        to_stdout(debug=debug, thread=thread, datetime=datetime)


def choose_format(datetime=True, thread=True):
    fmt = "%(levelname)-7s %(message)s"
    if thread:
        fmt = "%(threadName)-10s " + fmt
    if datetime:
        fmt = "%(asctime)s " + fmt

    return fmt


def to_stdout(debug=False, thread=True, datetime=True):
    fmt = choose_format(datetime=datetime, thread=thread)
    lvl = logging.DEBUG if debug else logging.INFO

    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt=fmt, datefmt=DATE_FMT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(lvl)


def to_syslog(debug=False, thread=True, tag=None):
    tag = tag or os.path.basename(sys.argv[0])
    lvl = logging.DEBUG if debug else logging.INFO
    fmt = tag + ": " + choose_format(datetime=False, thread=thread)

    logger = logging.getLogger()
    handler = logging.handlers.SysLogHandler(address="/dev/log")
    formatter = logging.Formatter(fmt=fmt, datefmt=DATE_FMT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(lvl)


def to_file(debug=False, thread=True, datetime=True, path=None, **kwargs):
    """
    https://docs.python.org/2.7/library/logging.handlers.html#rotatingfilehandler
    """

    lvl = logging.DEBUG if debug else logging.INFO
    fmt = choose_format(datetime=datetime, thread=thread)

    logger = logging.getLogger()
    handler = logging.handlers.RotatingFileHandler(filename=path)
    formatter = logging.Formatter(fmt=fmt, datefmt=DATE_FMT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(lvl)
