#!/usr/bin/env python

import argparse
import logging

import easylogconfig


log = logging.getLogger(__name__)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--debug", action="store_true")
    p.add_argument("--log-tag", type=str)
    p.add_argument("--log-file", type=str)
    return p.parse_args()


def main():
    args = parse_args()

    easylogconfig.auto(
        syslog_tag=args.log_tag,
        file_name=args.log_file,
        debug=args.debug,
        datetime=True,
    )

    log.info("info")
    log.error("error")
    log.debug("debug")


if __name__ == "__main__":
    main()
