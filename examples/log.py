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
    easylogconfig.configure(syslog_tag=args.log_tag, log_file=args.log_file, debug=args.debug)
    # if args.log_tag:
    #     easylogconfig.to_syslog(tag="testtag", debug=args.debug)
    # elif args.log_file:
    #     easylogconfig.to_file(path=args.log_file, debug=args.debug)
    # else:
    #     easylogconfig.to_stdout()

    log.info("info")
    log.error("error")
    log.debug("debug")


if __name__ == "__main__":
    main()

