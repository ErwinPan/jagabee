# -*- coding: utf-8 -*-
import urllib
import pycurl
import StringIO
import traceback
import sys
import re

def pycurl_wrapper_fetch(url, target_file, referer = ''):


    #
    # 1st request
    #
    c = pycurl.Curl()

    #c.setopt( pycurl.VERBOSE , True )
    c.setopt( pycurl.URL , url )
    c.setopt( pycurl.FOLLOWLOCATION , True )
    if (referer is not None) and (referer != ''):
        c.setopt( pycurl.REFERER, referer.encode('utf-8') )

    c.setopt( pycurl.COOKIEFILE , './pycurl.cookie' )
    c.setopt( pycurl.COOKIEJAR , './pycurl.cookie' )

    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)

    c.perform()

    #print b.getvalue()
    r = b.getvalue()
    b.close()

    f = open( target_file , 'wb' )
    f.write( r )
    f.close()

    return r



if __name__ == '__main__':
    try:
        url = 'http://iqc.com.tw/List/0/1/61'
	target_file = './1.html'
        pycurl_wrapper_fetch(url, target_file)
        print "done"
        sys.exit(0)

    except Exception, e:
        traceback.print_exc()
        sys.exit(-1)
