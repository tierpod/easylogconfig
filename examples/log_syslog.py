#!/usr/bin/env python
# coding: utf-8

import logging
import easylogconfig

log = logging.getLogger(__name__)


easylogconfig.auto(syslog_tag="example_tag", debug=True, datetime=True, thread=False)

log.info("info message")
log.error("error message")
log.debug("debug message")
