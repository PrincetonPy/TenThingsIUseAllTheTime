#!/bin/env python

'''Demonstrate the logging module.'''

import logging
import logging.config
import logging.handlers

logging.config.fileConfig('loggingDemo.conf')

logger = logging.getLogger('demo')

def doWork():
    'Log some messages.'
    
    logger.debug('A debug message')
    logger.info('An info message')
    logger.warning('A warning message')
    logger.error('An error message')
    logger.critical('A critical message')

if __name__ == '__main__':
    
    doWork()
    
