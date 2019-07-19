import os
import logging

logging.basicConfig(filename='debug_log1.log',level=logging.DEBUG)
def hello():
    logging.debug(111)
    logging.info(222)
    os.curdir

if __name__ == '__main__':
    hello()