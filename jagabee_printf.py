# -*- coding: utf-8 -*-
import urllib
import pycurl
import StringIO
import traceback
import sys, getopt
import re
import string
import time
import random
import os
import errno
from datetime import datetime, date, time


def printf(*argv):
    try:
        
        date_format = (datetime.now().strftime("[%Y/%m/%d %H:%M:%S.%f]"), )

        if len(argv) > 1:
            print ("%s " + argv[0]) % ( date_format +  argv[1:])
        else:
            print ("%s " + argv[0]) % ( date_format )

    except Exception, e:
        traceback.print_exc()

    pass



if __name__ == '__main__':
    try:
        printf("test = %d, %d, str=%s", 1, 3, "123")
        
        printf("test")

    except Exception, e:
        traceback.print_exc()
        sys.exit(-1)
