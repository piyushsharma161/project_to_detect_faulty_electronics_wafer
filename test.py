# -*- coding: utf-8 -*-

from application_logging.logger import App_Logger

log_file = open('C:/projects/WaferFaultDetection1/testlogging.txt', 'a+')

logger = App_Logger()

logger.log(log_file,'test successfull')

