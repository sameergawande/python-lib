#!/usr/bin/env python3
import logging
import Employee
logger = logging.getLogger(__name__)

logging.basicConfig(filename = 'calc.log',level=logging.DEBUG,format='%(asctime)s:%(name)s:%(message)s')
def add(x,y):
	return x+y

def mul(x,y):
	return x*y

def minus(x,y):
	return x-y

def div(x,y):
	return x/y

a,b = 100,50
add_result = add(a,b)
logger.debug("{} + {} = {}".format(a,b,add_result))
