# -*- coding: utf-8 -*-
import urllib
import pycurl
import StringIO
import traceback
import sys
import re
import time
import random

def pycurl_wrapper_fetch(url, target_file = '', referer = '', retry = 3):

    html_text = ''

    try:
        f = open( target_file , 'r' )

        # Local target exists, just read from it and return
        html_text = f.read( r )
        f.close()

        return html_text

    except Exception, e:
        # Local target not exists
        pass

    for i in range(0, retry):
        try:
            print 'http pycurl_wrapper_fetch, try = %d, url = %s' % (i, url)

            (http_code, html_text) = pycurl_wrapper_fetch_internal(url, target_file, referer)

            if http_code != 200:
                html_text = ''

            if len(html_text) > 0:
                break

        except Exception, e:
            traceback.print_exc()
            time.sleep(random.random())
            pass

    return html_text


def pycurl_wrapper_fetch_internal(url, target_file = '', referer = ''):
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

    http_code = c.getinfo(pycurl.HTTP_CODE)

    #print b.getvalue()
    r = b.getvalue()
    b.close()

    #print 'http code is: %s, len(html) = %d' % (http_code, len(r))
        
    if target_file != '':

        a = {}
        a['ori_url'] = url
        r = "<!-- " + str(a) + " -->\n" + r

        f = open( target_file , 'wb' )
        f.write( r )
        f.close()

    return http_code, r



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
