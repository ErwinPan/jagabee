# -*- coding: utf-8 -*-
import urllib
import pycurl
import StringIO
import traceback
import sys
import re
import iqc_parse_pages
import pycurl_wrapper
import string

if __name__ == '__main__':
    try:
	# Category Entry
        #url = 'http://iqc.com.tw/List/0/1/61'

        # Category with Referer
	url = 'http://iqc.com.tw/List/2/'
	referer = 'http://iqc.com.tw/List/1/'
        #referer = 'http://iqc.com.tw/List/0/1/61'

	# Replace filename
	target_file = url[7:]
	target_file = string.replace(target_file, '/', '_') + '.html'

	# Fetch html page
        html = pycurl_wrapper.pycurl_wrapper_fetch(url, target_file, referer)

	# Parse html page
	if len(html) > 0:
	    iqc_parse_pages.parse_list_page(html, True)

        print "done"
        sys.exit(0)

    except Exception, e:
        traceback.print_exc()
        sys.exit(-1)
