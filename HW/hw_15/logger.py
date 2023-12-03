from os import path

import logging

logging.basicConfig(level=logging.NOTSET, encoding='utf-8', filename='logFile.log')
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('Test')
    