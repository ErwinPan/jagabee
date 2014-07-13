# -*- coding: utf-8 -*-
import urllib
import pycurl
import StringIO
import traceback
import sys
import re


def dump_list_tuple(list_or_tuple, indent):

    #print 'dump_list_tuple, indent=%d' % indent

    i = 0
    for m in list_or_tuple:
        dump_node(m, indent)
        i += 1



def dump_string(string, indent):

    #print 'dump_string, indent=%d' % indent

    i = indent
    indent_string = ''
    while (i > 0):
        indent_string += ' '
        i -= 1
    print "%s-> %s" % (indent_string, string)



def dump_node(node, indent):

    #print 'dump_node, indent=%d' % indent

    if type(node).__name__ == 'str':
        dump_string(node, indent)
        return

    if type(node).__name__ == 'tuple' or type(node).__name__ == 'list' :
        i = indent
        indent_string = ''
        while (i > 0):
            indent_string += ' '
            i -= 1
        print "%s->" % (indent_string)
        dump_list_tuple(node, indent + 1)
        return
    
    print "Invalid match type:%s (which is expected to be a 'tuple', 'list', 'str,...), abort" % str(type(match))
    return



def dump_match(match):
    indent = 0

    print "\n======================= dump_match start =========================="
    dump_node(match, indent)
    print "======================= dump_match done ==========================\n"
    return    	



def parse_list_page(html, b_first_page, ret={}):

    count = 0
    ret['link'] = []
    ret['total_product_counts'] = 0

    body = re.findall( re.compile( '(<body(.*?)</body>)' , flags=(re.IGNORECASE|re.DOTALL) ) , html);
    #print "len(body) = " + str(len(body))
    if len(body) < 1 :
        print "No BODY DATA"
        return ret

    if b_first_page:
        all_matches = re.findall( re.compile( '<div class=\"searchInfo\">[\s]*SHOWING ITEMS(.*?)</b> of ([0-9]*)</div>' , flags=(re.IGNORECASE|re.DOTALL)) , html)

        if type(all_matches).__name__ != 'list' or len(all_matches) == 0:
            print "Invalid all_matches: " + str(type(all_matches))
            ret['total_product_counts'] = 0
        else:
            #dump_match(all_matches)
            ret['total_product_counts'] = int(all_matches[0][1])
            print "ret['total_product_counts'] = " + str(ret['total_product_counts'])
        

    # Parse product list tag
    all_matches = re.findall( re.compile( '<div class=\"searchItemList\">[\s]*<ul>(.*?)</ul>' , flags=(re.IGNORECASE|re.DOTALL)) , html)
    for match in all_matches:
        #print "len(match) = " + str(len(match))
        #dump_match(match)
        continue

    if type(all_matches).__name__ != 'list' or len(all_matches) == 0:
        print "Invalid all_matches: " + str(type(all_matches))
        return ret

    # Check if we get <li>  </li> in the first match
    list_text = all_matches[0]
    if type(list_text).__name__ != 'str':
        print "Invalid list_text" + type(list_text).__name__
        return ret

    #print "list_text = " + list_text
    #print "================================================="

    test_text = '''
                <li>
                    <a href="http://iqc.com.tw/Commodities/Detail/173185">
                    <img src="./iqc.com.tw_List_0_1_61_files/黑松沙士600.jpg" title="黑松沙士(PET600ml)" height="160" width="160">
                    </a>
                    <h4><a href="http://iqc.com.tw/Commodities/Detail/173185">黑松沙士(PET600ml)</a></h4>
                </li>

                <li>
                    <a href="http://iqc.com.tw/Commodities/Detail/319465">
                    <img src="./iqc.com.tw_List_0_1_61_files/黑松沙士.png" title="黑松沙士加鹽 600ml" height="160" width="160">
                    </a>
                    <h4><a href="http://iqc.com.tw/Commodities/Detail/319465">黑松沙士加鹽 600ml</a></h4>
                </li>'''

    # Parse list_text into 'li' list, where re.findall will return a "list" composed of "str" (due to single capturing group "()")
    all_matches = re.findall( re.compile( '<li>(.*?)</li>' , flags=(re.IGNORECASE|re.DOTALL)) , list_text)
    for li_match in all_matches:
        #print "len(li_match) = " + str(len(li_match))
        #dump_match(li_match)

        if type(li_match).__name__ != 'str':
            continue

        # Parse li tag, where re.findall will return a "list" composed of "str" (due to single capturing group "()")
        href_matches = re.findall( re.compile( '<a href=\"(.*?)\">[\s]*<img' , flags=(re.IGNORECASE|re.DOTALL)) , li_match)
        for href_match in href_matches:
            #dump_match(href_match)
            ret['link'].append(href_match)
            print "ret['link'][%d] = %s" % (count, ret['link'][count])
            count += 1

        #print "commodity title=%s, vendor=%s, vendor_addr=%s, vendor_tel=%s, website=%s" % (ret['title'], ret['vendor'], ret['vendor_addr'], ret['vendor_tel'], ret['website'])

    return ret




def parse_commodity_page(html, ret={}):
    
    body = re.findall( re.compile( '(<body(.*?)</body>)' , flags=(re.IGNORECASE|re.DOTALL) ) , html);
    #print "len(body) = " + str(len(body))
    if len(body) < 1 :
        print "No BODY DATA"
        return ret

    # Parse , where re.findall returns a "list" of "str" (single capturing group)
    all_matches = re.findall( re.compile( '<td bgcolor=\"#ffffff\" valign=\"top\" align=\"center\" class=\"font09\" width=\"40%\"><br><a href=\"(.*?)\" target=\"_blank\">' , flags=(re.IGNORECASE|re.DOTALL)) , html)
    for match in all_matches:

        dump_match(match)
        break # only get first item from list


    # Parse , where re.findall returns a "list" of tuples (multiple capturing groups)
    all_matches = re.findall( re.compile( '<font color=\"#377EB3\" class=\"font09\">商品編號:</font>(.*?)<b>(.*?)<br><br>(.*?)</b>' , flags=(re.IGNORECASE|re.DOTALL)) , html)
    for match in all_matches:
        dump_match(match)
        break # only get first item from list

    # Parse , where re.findall returns a "list" of tuples (multiple capturing groups)
    all_matches = re.findall( re.compile( '<b>市售價: (.*?)<s>(.*?)</s>(.*?), 馬上省下: <font color=\"#D32417\" style=\"font-family:Arial;\">(.*?)</font> 元<br><b>網路價 <font color=\"#D32417\" style=\"font-family:Arial;\">(.*?)</font> 元 </b>' , flags=(re.IGNORECASE|re.DOTALL)) , html)
    for match in all_matches:
        #print "commodity barcode=%s, reserv_date=%s, title=%s, img_url=%s" % (ret['barcode'], ret['reserv_date'], ret['title'], ret['img_url'])
        dump_match(match)
        break # only get first item from list

    return ret


if __name__ == '__main__':
    try:
        # Read file
        f = open("6lucky/commodity/MICCOSMO.html", "r")
        html_text = f.read()
        f.close()

        # parse 
        parse_commodity_page(html_text)
        #parse_list_page(html_text, True)

        print "regular expression parsing done"
        sys.exit(0)

    except Exception, e:
        traceback.print_exc()
        print "regular expression parsing failed"
        sys.exit(-1)
