#!/usr/bin/env python3
import argparse
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('syslog.log')
logger.addHandler(file_handler)
formatter=logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)
#logging.basicConfig(level=logging.DEBUG, filename='syslog.log',format='%(asctime)s:%(name)s:%(message)s')
class Employee:
	def __init__(self,first,last):
		self.first = first
		self.last = last
		logger.debug("{} {} created".format(self.first,self.last))

emp1 = Employee("sameer","gawande")
