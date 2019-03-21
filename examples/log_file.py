#!/usr/bin/env python
# coding: utf-8

import logging
import easylogconfig

log = logging.getLogger(__name__)


easylogconfig.to_file(datetime=True, thread=True, debug=True, path="/tmp/123.log")


log.info("info message")
log.error("error message")
log.debug("debug message")
