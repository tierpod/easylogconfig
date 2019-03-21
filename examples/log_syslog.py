#!/usr/bin/env python
# coding: utf-8

import logging
import easylogconfig

log = logging.getLogger(__name__)


# easylogconfig.to_syslog(thread=False, debug=True, tag="log_syslog")
easylogconfig.to_syslog(thread=False, debug=True)


log.info("info message")
log.error("error message")
log.debug("debug message")
