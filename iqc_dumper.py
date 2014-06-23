# -*- coding: utf-8 -*-
import urllib
import pycurl
import StringIO
import traceback
import sys, getopt
import re
import iqc_parse_pages
import jagabee_pycurl
import jagabee_sqlite3
import string
import time
from os.path import join, getsize

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def iqc_dump_list_page(url, referer = ''):
    # Replace filename
    target_file = url[7:]
    target_file = string.replace(target_file, '/', '_') + '.html'

    print 'dump %s to target_file:%s , referer:%s' % (url, target_file, referer)
    # Fetch html page
    html_text = jagabee_pycurl.pycurl_wrapper_fetch(url, target_file, referer)
   
    return html_text


def iqc_dump_category(url):

    print "\n==> Start to parse category url: %s ..." % url

    # Category with Referer
    #url = 'http://iqc.com.tw/List/2/'
    #referer = 'http://iqc.com.tw/List/1/'
    #referer = 'http://iqc.com.tw/List/0/1/61'

    html_text = iqc_dump_list_page(url)

    # Parse html page
    if len(html_text) > 0:
        ret = iqc_parse_pages.parse_list_page(html_text, True)

    # Calculate pages in this category
    page_count = 0
    if ret['total_product_counts'] > 0:
        page_count = ret['total_product_counts']/24 + 1

    # Fetch page from 2 ~ end
    for i in range(1, page_count):
        referer = url
        url = 'http://iqc.com.tw/List/' + str(i) + '/'
        html_text = iqc_dump_list_page(url)


def iqc_parse_commodity(barcode, ret = {}):

    print "\n===> Start to dump barcode %s ..." % barcode

    # http://iqc.com.tw/Commodities/Detail/176725
    url = 'http://iqc.com.tw/Commodities/Detail/' + barcode
    html_text = jagabee_pycurl.pycurl_wrapper_fetch(url)

    if len(html_text) > 0:
        iqc_parse_pages.parse_commodities_page(html_text, ret)

    # http://iqc.com.tw/Commodity/Detail/176725
    url = 'http://iqc.com.tw/Commodity/Detail/' + barcode
    html_text = jagabee_pycurl.pycurl_wrapper_fetch(url)

    if len(html_text) > 0:
        iqc_parse_pages.parse_commodity_page(html_text, ret)

    return ret

def iqc_parse_list_file(list_file):
    
    print "\n==> Start to parse list file: %s ..." % list_file

    if list_file != '':
        f = open( list_file , 'r' )
        html_text = f.read()
        f.close()

    if len(html_text) <= 0:
        return

    ret = {}
    ret = iqc_parse_pages.parse_list_page(html_text, False, ret)

    i = 0

    list_dump = {'list_file' : list_file}
    list_dump['commodities'] = []
    list_dump_file = list_file + '.dict'    # Dump to a dictionary

    for c in ret['link']:
        # /Commodities/Detail/171342
        # print 'c=%s, type=%s, rindex of "/" is %d' % (str(c), str(type(c)), string.rindex(c, '/'))
        try:
            barcode = c[string.rindex(c, '/')+1:]
            print 'barcode: %s' % barcode
            if (barcode is not None) and (barcode != ''):
                commodity = {'barcode' : barcode}
                commodity = iqc_parse_commodity(barcode, commodity)
                list_dump['commodities'].append(commodity)

            i += 1
            if i >= 3:
                break # dump leading 3 only because we're still debugging

        except Exception, e:
            print "Parse commodity fails ..." 
            traceback.print_exc()
            pass

   
    jagabee_sqlite3.db_save_products(list_dump['commodities'])

    # Save to a dictionary file and export to database in the future (not a good idea because saved string is not human readable, e.g: u'1234)
    #f = open( list_dump_file , 'wb' )
    #f.write(str(list_dump))
    #f.close()

    return

def iqc_parse_list_dir(list_dir):

    print "\n=> Start to parse list pages in current directory: %s ..." % list_dir

    iqc_parse_list_file("iqc.com.tw_List_0_1_61/iqc.com.tw_List_0_1_61.html")

    return



def print_usage(cmd):
    usage = '''
        -c, --parse-category
            Parse category
        -l, --parse-list-file=FILE
            Parse a list file
        -d, --parse-list-file=DIR
            Parse list files in a directory
        -h, --help
            Print this usage
    '''

    print ('\n%s usage: ' + usage) % cmd
    return



def main(argv):

    parse_category = None
    parse_list_file = None
    parse_list_dir = None

    try:
        #print " argv=%s" % str(argv)
        opts, other_args = getopt.getopt(argv[1:],"cf:d:",["parse-category=", "parse-list-file=", "parse-list-dir="])

    except getopt.GetoptError:
        print "getopt.GetoptError: "
        traceback.print_exc()
        print_usage(argv[0])
        sys.exit(-1)

    for opt, arg in opts:
        if opt in ("-c", "--parse-category"):
            parse_category = True
        elif opt in ("-f", "--parse-list-file"):
            parse_list_file = arg
        elif opt in ("-d", "--parse-list-dir"):
            parse_list_dir = arg

    if not parse_category and not parse_list_file and not parse_list_dir:
        print_usage(argv[0])
        sys.exit()

    return parse_category, parse_list_file, parse_list_dir



if __name__ == '__main__':
    try:

        parse_category, parse_list_file, parse_list_dir = main(sys.argv) 
        

        if parse_category is not None:
            # Define Root Category Entry
            url = 'http://iqc.com.tw/List/0/1/61'
            iqc_dump_category(url)
            pass

        if parse_list_file is not None:
            iqc_parse_list_file(parse_list_file)
            pass
        
        if parse_list_dir is not None:
            iqc_parse_list_dir(parse_list_dir)
            pass

        print "done"
        sys.exit(0)

    except Exception, e:
        traceback.print_exc()
        sys.exit(-1)
