#-*- coding: utf-8 -*-

from yuantacat.common.logging_utils import setup_logging
from yuantacat.yuanta_cat import YuantaCat
import sys 

def main():
    setup_logging() 
    yuanta_cat = YuantaCat()
    yuanta_cat.run()
    
if __name__ == '__main__':
    sys.exit(main())