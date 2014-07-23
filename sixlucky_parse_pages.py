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
    total_product_counts_gotten = False
    if not ret.has_key("list_link"):
        ret["list_link"]=[]

    body = re.findall( re.compile( '(<body(.*?)</body>)' , flags=(re.IGNORECASE|re.DOTALL) ) , html);
    #print "len(body) = " + str(len(body))
    if len(body) < 1 :
        print "No BODY DATA"
        return ret

    if b_first_page:
        # Return pages count area
        header_text = ""
        all_matches = re.findall( re.compile( '<td align=[\"]?right[\"]?><font color=\"#666666\" class=[\"]?font09[\"]?>(.*?)</td>' , flags=(re.IGNORECASE|re.DOTALL)) , html)
        #dump_match(all_matches)
        for match in all_matches:
            header_text = match
            #print "[parse_list_page] header_text=%s" % header_text
            break # only get first

        if header_text == "":
            print "[parse_list_page] No additional list pages"
        else:
            # Return list page links
            all_matches = re.findall( re.compile( '共: (.*?)筆' , flags=(re.IGNORECASE|re.DOTALL)) , header_text)
            for match in all_matches:
                ret["total_product_counts"] = int(match)
                print "total_product_counts=%d" % ret["total_product_counts"]
                total_product_counts_gotten = True

            #dump_match(all_matches)
            all_matches = re.findall( re.compile( '<a style=[\'\"]color:#666666;[\'\"] href=\"(.*?)\">' , flags=(re.IGNORECASE|re.DOTALL)) , header_text)
            for match in all_matches:
                print "list_link=%s" % match
                ret["list_link"].append(match)

    table_text = ""

    # List pattern 1: having tbody
    all_matches = re.findall( re.compile( '<table border=\"0\" width=\"100%\" cellspacing=\"2\" cellpadding=\"6\" class=\"font09h15\">(.*)</tbody></table>[\s]*<style type=\"text/css\">' , flags=(re.IGNORECASE|re.DOTALL)) , html)

    # List pattern 2: no tbody
    if len(all_matches) <= 0:
        all_matches = re.findall( re.compile( '<table border=\"?0\"? width=\"?100%\"? cellspacing=\"?2\"? cellpadding=\"?6\"? class=\"?font09h15\"?>(.*?)</table>' , flags=(re.IGNORECASE|re.DOTALL)) , html)

    #dump_match(all_matches)
    for match in all_matches:
        table_text = match
        break # only get first item from list
    
    if table_text == "":
        print "No Table exist"
        return ret

    # Parse table list which returns a list of "str"s
    all_matches = re.findall( re.compile( '<a href=\"(.*?)\">' , flags=(re.IGNORECASE|re.DOTALL)) , table_text)
    for match in all_matches:
        if match[0:7] != "http://":
            match = "http://www.6lucky.com.tw" + match
        #print "len(match) = " + str(len(match))
        ret["link"].append(match)
        if not total_product_counts_gotten:
            ret['total_product_counts'] += 1
        dump_match(match)
        continue

        #print "commodity title=%s, vendor=%s, vendor_addr=%s, vendor_tel=%s, website=%s" % (ret['title'], ret['vendor'], ret['vendor_addr'], ret['vendor_tel'], ret['website'])

    return ret




def parse_commodity_page(html, ret={}):
    
    body = re.findall( re.compile( '(<body(.*?)</body>)' , flags=(re.IGNORECASE|re.DOTALL) ) , html);
    #print "len(body) = " + str(len(body))
    if len(body) < 1 :
        print "No BODY DATA"
        return ret

    # Parse , where re.findall returns a "list" of "str" (single capturing group)
    all_matches = re.findall( re.compile( '<td bgcolor=\"?#ffffff\"? valign=\"?top\"? align=\"?center\"? class=\"?font09\"? width=\"?40%\"?><br><a href=\"(.*?)\" target=\"_blank\">' , flags=(re.IGNORECASE|re.DOTALL)) , html)
    for match in all_matches:
        ret["img_url"] = match
        #dump_match(match)
        break # only get first item from list


    # Parse , where re.findall returns a "list" of tuples (multiple capturing groups)
    all_matches = re.findall( re.compile( '<font color=\"?#377EB3\"? class=\"?font09\"?>商品編號:</font>(.*?)<b>(.*?)<br><br>(.*?)</b>' , flags=(re.IGNORECASE|re.DOTALL)) , html)
    for match in all_matches:
        ret["barcode"] = match[1]
        ret["title"] = match[2]
        #dump_match(match)
        break # only get first item from list

    if html.find("市售價") > 0 and html.find("馬上省下") > 0:
        # Parse , where re.findall returns a "list" of tuples (multiple capturing groups)
        all_matches = re.findall( re.compile( '<b>市售價: (.*?)<s>(.*?)</s>(.*?), 馬上省下: <font color=\"?#D32417\"? style=\"?font-family:Arial;\"?>(.*?)</font> 元<br><b>網路價 <font color=\"?#D32417\"? style=\"?font-family:Arial;\"?>(.*?)</font> 元 </b>' , flags=(re.IGNORECASE|re.DOTALL)) , html)
        for match in all_matches:
            ret["ori_price"] = match[1]
            ret["price"] = match[4]
            #dump_match(match)
            break # only get first item from list
    else:
        all_matches = re.findall( re.compile( '<b>網路價 <font color=\"#D32417\" style=\"font-family:Arial;\">(.*?)</font> 元 </b>' , flags=(re.IGNORECASE|re.DOTALL)) , html)
        for match in all_matches:
            ret["ori_price"] = match
            ret["price"] = match
            #dump_match(match)
            break # only get first item from list

    print "commodity barcode=%s, title=%s, img_url=%s, price=%s, ori_price=%s" % (ret['barcode'], ret['title'], ret['img_url'], ret["price"], ret["ori_price"])


    return ret


if __name__ == '__main__':
    try:
        # Read file
        #f = open("6lucky/commodity/MICCOSMO.html", "r")
        #f = open("6lucky/commodity/net_price.html", "r")

        f = open("6lucky/single_page_list/a.html", "r")
        #f = open("6lucky/page_list_head/a.html", "r")
        #f = open("6lucky/page_list_head/no_list.html", "r")
        #f = open("sixlucky/身體保養清潔/頸部保養/list_0.html", "r")
        html_text = f.read()
        f.close()

        # parse 
        #parse_commodity_page(html_text)
        parse_list_page(html_text, True)

        print "regular expression parsing done"
        sys.exit(0)

    except Exception, e:
        traceback.print_exc()
        print "regular expression parsing failed"
        sys.exit(-1)
