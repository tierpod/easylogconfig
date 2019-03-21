easylogconfig
=============

This python library provides simple wrapper for standart logging module. It helps you configure
logger in simple cases without reading a lot of [documentation][1] and writing a lot of code.

Usage
-----

You can find examples in ./examples directory

```python
import logging
import easylogconfig

log = logging.getLogger(__name__)

# print messages to stdout, add debug level and datetime
easylogconfig.auto(debug=True, datetime=True)

log.info("info message")
log.debug("debug message")
```

Configuration
-------------

Library provides one simple function **auto** with arguments:

* formatter arguments:
  * *debug=False*: add debug level to output?
  * *thread=True*: add thread names to messages?
  * *datetime=True*: add datetime to messages?
* [SysLogHandler][2] arguments:
  * **syslog_tag=None**: if set to str, log messages to syslog with this tag
  * *syslog_address="/dev/log"*: syslog server address
* [TimedRotatingFileHandler][3] arguments:
  * **file_name=None**: if set to str, log messages to this tile
  * *file_when="midnight"*: file rotating time
  * *file_backup_count=7*: keep last files

If you want to log messages to the stdout, don't pass **syslog_tag** or **file_name** arguments. If
you want to log messages to the syslog server, pass **syslog_tag** argument. If you want to log
messages to the file, pass **file_name** argument.

Installation
------------

[1]: https://docs.python.org/2.7/howto/logging.html
[2]: https://docs.python.org/2.7/library/logging.handlers.html#sysloghandler
[3]: https://docs.python.org/2.7/library/logging.handlers.html#timedrotatingfilehandler
