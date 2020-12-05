import logging

class LoggerConsole():
    def testLog(self):
        # Create logger
        logger = logging.getLogger(LoggerConsole.__name__)
        logger.setLevel(logging.INFO)

        # Create console handler and set level to Info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')

        # Add formatter to console handler -> ch
        chandler.setFormatter(formatter)

        # Add console handler to logger
        logger.addHandler(chandler)

        # Logging message
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')


obj1 = LoggerConsole()
obj1.testLog()
