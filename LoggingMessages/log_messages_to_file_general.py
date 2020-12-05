import logging
import logging.config

class LoggerConfiguration():
    def testLog(self):
        #Create logger
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerConfiguration.__name__)

        # Logging message
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')


obj1 = LoggerConfiguration()
obj1.testLog()