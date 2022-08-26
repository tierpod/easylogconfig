#!/usr/bin/env python
# coding: utf-8

import logging
import easylogconfig

log = logging.getLogger(__name__)


easylogconfig.auto(syslog_tag="example_tag", syslog_address=("127.0.0.1", 514), debug=True)

log.info("info message")
log.error("error message")
log.debug("debug message")
