#logs
import logging
import datetime as dt

today = dt.datetime.today()
filename = f'{today.year}{today.month:02d}{today.day:02d}.log'

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

def test_1():
  # we will only see from warning to critical, by default info and debug message 
  # are noticed but not shows at prompt to change this you can
  # update it at logging.basicConfig(level=logging.DEBUG) now will work from debug to critical

  logging.basicConfig(level=logging.DEBUG)

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


def test_2():
  # change logger name

  logging.basicConfig(level=logging.INFO)
  logger = logging.getLogger("PERSONALIZED-NAME")
  logger.info("Personal info message")


def test_3():

  logging.basicConfig(level=logging.DEBUG)
  logging.log(logging.DEBUG, 'message at DEBUG level')
  logging.log(logging.INFO, 'message at INFO level')
  logging.log(logging.WARNING, 'message at WARNING level')
  logging.log(logging.ERROR, 'message at ERROR level')
  logging.log(logging.CRITICAL, 'message at CRITICAL level')

  logger = logging.getLogger("Test-ABC")

  file_handler = logging.FileHandler(filename)
  file_handler.setLevel(logging.WARNING)

  formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
  file_handler.setFormatter(formatter)

  logger.addHandler(file_handler)

  logger.debug('message at DEBUG level')
  logger.info('message at INFO level')
  logger.warning('message at WARNING level')
  logger.error('message at ERROR level')
  logger.critical('message at CRITICAL level')


if __name__ == '__main__':

  # test_1()
  # test_2()
  test_3()