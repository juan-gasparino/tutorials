#logs
import logging

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

if __name__ == '__main__':

  # we will only see from warning to critical, by default info and debug message 
  # are noticed but not shows at prompt to change this you can
  # update it at logging.basicConfig(level=logging.DEBUG) now will work from debug to critical

  #logging.basicConfig(level=logging.DEBUG)

  logging.log(logging.DEBUG, "message at DEBUG level")
  logging.log(logging.INFO, "message at INFO level")
  logging.log(logging.WARNING, "message at WARNING level")
  logging.log(logging.ERROR, "message at ERROR level")
  logging.log(logging.CRITICAL, "message at CRITICAL level")

  logging.debug("message at DEBUG level")
  logging.info("message at INFO level")
  logging.warning("message at WARNING level")
  logging.error("message at ERROR level")
  logging.critical("message at CRITICAL level")

  #