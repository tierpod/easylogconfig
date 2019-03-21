#!/usr/bin/env python
# coding: utf-8

import logging
import easylogconfig

log = logging.getLogger(__name__)


easylogconfig.to_stdout(datetime=True, thread=True, debug=True)


log.info("info message")
log.error("error message")
log.debug("debug message")
