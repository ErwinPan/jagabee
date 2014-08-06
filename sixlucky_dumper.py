# -*- coding: utf-8 -*-
import urllib
import pycurl
import StringIO
import traceback
import sys, getopt
import re
import sixlucky_categories
import sixlucky_parse_pages
import jagabee_pycurl
import jagabee_sqlite3
from jagabee_printf import printf
import string
import time
import random
import os
import errno

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


sixlucky_working_directory = '.'
commodity_index = 0

def sixlucky_get_directory(main_cat = "main_cat", sub_cat = "sub_cat"):

    directory = "sixlucky/"  + string.replace(main_cat, "/", "_") + "/" + string.replace(sub_cat, "/", "_")

    return directory


def sixlucky_url_to_local_file(url, main_cat = "main_cat", sub_cat = "sub_cat", page_type = None, index = -1):

    global sixlucky_working_directory

    sixlucky_working_directory = sixlucky_get_directory(main_cat, sub_cat)

    try:
        os.makedirs(sixlucky_working_directory)
    
    except Exception, e:
        if e.errno != errno.EEXIST:
            printf('sixlucky_url_to_local_file mkdir exception: !!')
            traceback.print_exc()

    if page_type is None or index < 0:
        i = string.rindex(url, "?")
        target_file = sixlucky_working_directory + "/" + urllib.quote(url[i+1:], "") + ".html"
    else:
        target_file = sixlucky_working_directory + "/" + page_type + "_" + str(index) + ".html"

    return target_file


#
# Dump a list html page
#
def sixlucky_dump_list_page(url, main_cat = "main_cat", sub_cat = "sub_cat", index = 0):

    printf("sixlucky_dump_list_page: url = %s, main_cat = %s, sub_cat = %s " , url, main_cat, sub_cat)

    target_file = sixlucky_url_to_local_file(url, main_cat = main_cat, sub_cat = sub_cat, page_type = "list", index = index)

    printf('dump %s to target_file: %s ', url, target_file)
    # Fetch html page
    html_text = jagabee_pycurl.pycurl_wrapper_fetch(url, target_file)
   
    return html_text



#
# Dump all list html pages from all sub categories from a main category
#
def sixlucky_dump_main_category(main_cat_dict):

    try:
        main_cat = main_cat_dict['main_cat']
        sub_cats = main_cat_dict['sub_cats']

        for sub_cat_dict in sub_cats:
            url = sub_cat_dict['url']
            sub_cat = sub_cat_dict['sub_cat']
            sixlucky_dump_sub_category(url, main_cat, sub_cat)
            time.sleep(10)

    except Exception, e:
        printf('sixlucky_dump_main_category exception: !!')
        traceback.print_exc()

#
# Dump all list html pages from a sub category
#
def sixlucky_dump_sub_category(url, main_cat, sub_cat):

    printf("\n==> Start to parse category url: %s, main_cat: %s, sub_cat: %s ...", url, main_cat, sub_cat)

    global sixlucky_working_directory
    i = 0

    # Category with Referer
    #url = 'http://iqc.com.tw/List/2/'

    # Return here for debugging
    #return
    printf("List is %d", str.find(url, "List"))
    sixlucky_working_directory = url[str.find(url, "List"):]

    html_text = sixlucky_dump_list_page(url, main_cat = main_cat, sub_cat = sub_cat, index = i)

    # Parse html page
    if len(html_text) <= 0:
        print("Can not get list page html_text, len = 0")
        return

    ret = sixlucky_parse_pages.parse_list_page(html_text, True, ret={})

    print("ret['total_product_counts'] = %d", ret['total_product_counts'])

    # Calculate pages in this category
    page_count = 0
    if ret['total_product_counts'] > 0:
        page_count = ret['total_product_counts']/18 + 1

    if page_count > 10:
        page_count = 10

    # Fetch page from 2 ~ end
    for i in range(1, page_count):
        time.sleep(random.random()*10)
        url = "http://www.6lucky.com.tw/showroom/" + ret["list_link"][i]
        html_text = sixlucky_dump_list_page(url, main_cat = main_cat, sub_cat = sub_cat, index = i)


#
# Dump a commodity html page and parse a it
#
def sixlucky_dump_and_parse_commodity(url, main_cat = "main_cat", sub_cat = "sub_cat", index = -1, ret = {}):


    target_file = sixlucky_url_to_local_file(url, main_cat, sub_cat, "commodity", index)

    printf("\n===> Start to dump commodity page url: %s to target_file: %s ...", url, target_file)

    html_text = jagabee_pycurl.pycurl_wrapper_fetch(url, target_file)

    if len(html_text) > 0:
        sixlucky_parse_pages.parse_commodity_page(html_text, ret)

    return ret


#
# Parse a list html page and dump all commodities html pages from it
#
def sixlucky_parse_list_file(main_cat, sub_cat, list_file, db_name = 'test.db'):
    
    printf("\n==> Start to parse list file: %s ...", list_file)

    global commodity_index

    if list_file != '':
        f = open( list_file , 'r' )
        html_text = f.read()
        f.close()

    if len(html_text) <= 0:
        return

    ret = {}
    ret = sixlucky_parse_pages.parse_list_page(html_text, True, ret)

    list_dump = {'list_file' : list_file}
    list_dump['commodities'] = []

    for commodity_url in ret['link']:
        try:
            printf('commodity_index: %d', commodity_index)
            m = {'main_cat' : main_cat, 'sub_cat' : sub_cat}
            m = sixlucky_dump_and_parse_commodity(commodity_url, main_cat, sub_cat, commodity_index, m)
            list_dump['commodities'].append(m)

            commodity_index += 1
            #if i >= 3:
            #    break # dump leading 3 only because we're still debugging

        except Exception, e:
            printf("Parse commodity fails ...")
            traceback.print_exc()
        finally:
            # Sleep for a while to avoid busy accessing
            time.sleep(random.random()*3)
            pass

   
    jagabee_sqlite3.db_save_products(list_dump['commodities'], db_name)

    # Save to a dictionary file and export to database in the future (not a good idea because saved string is not human readable, e.g: u'1234)
    #f = open( list_dump_file , 'wb' )
    #f.write(str(list_dump))
    #f.close()

    return


#
# Parse list html pages from a dir and dump all commodities html pages from list html pages
#
def sixlucky_parse_list_dir(main_cat, sub_cat, list_dir):

    printf("\n=> Start to parse list pages in current directory: %s ...", list_dir)

    global sixlucky_working_directory
    global commodity_index
    
    sixlucky_working_directory = list_dir
    commodity_index = 0

    all_files = []
    db_name = os.path.join(list_dir, "products.db")
    printf("db_name = %s" % db_name)
    root = ''

    if os.path.exists(db_name):
        printf("db exists: %s , skip it", db_name)
        return

    for root, dirs, files in os.walk(list_dir):
        printf("root is %s, dirs is %s, files is %s", root, str(dirs), str(files))
        if list_dir == root:
            all_files = files
            break

    for f in all_files:
        printf("parsing file: %s ...", f)
        try:
            if f.startswith("list_"):
                sixlucky_parse_list_file(main_cat, sub_cat, os.path.join(root, f), db_name)

            pass

        except Exception, e:
            traceback.print_exc()


    return

#
# Steps:
#       1. dump-sub-category
#       2. dump-main-category
#       3. parse-list-file
#       4. parse-list-dir
#       5. dump-commodity-from-sub-category-dirs 
#       6. collect-all-db
#
#

def print_usage(cmd):
    usage = '''
        -m, --dump-main-category=N
            Dump list html pages from sub categories from a main category (index = N)
        -s, --dump-sub-category
            Dump list html pages from a sub category
        -r, dump-commodity-from-sub-category-dirs
            Dump commodity pages from sub category dirs
        -l, --parse-list-file=FILE
            Parse a list file
        -d, --parse-list-dir=DIR
            Parse list files in a directory
        -a, --collect-all-db
            Collect all database into one
        -h, --help
            Print this usage
    '''

    printf(('\n%s usage: ' + usage), cmd)
    return



def main(argv):

    dump_main_category = None
    dump_sub_category = None
    dump_commodity_from_sub_category_dirs = None
    parse_list_file = None
    parse_list_dir = None
    collect_all_db = None

    try:
        #printf(" argv=%s", str(argv))
        opts, other_args = getopt.getopt(argv[1:],"m:srlda",["dump-main-category=", "dump-sub-category", "dump-commodity-from-sub-category-dirs", "parse-list-file", "parse-list-dir", "collect-all-db"])

    except getopt.GetoptError:
        printf("getopt.GetoptError: ")
        traceback.print_exc()
        print_usage(argv[0])
        sys.exit(-1)

    for opt, arg in opts:
        if opt in ("-m", "--dump-main-category"):
            dump_main_category = int(arg)       # index of main category (int)
        elif opt in ("-s", "--dump-sub-category"):
            dump_sub_category = True
        elif opt in ("-r", "--dump-commodity-from-sub-category-dirs"):
            dump_commodity_from_sub_category_dirs = True
        elif opt in ("-l", "--parse-list-file"):
            parse_list_file = True
        elif opt in ("-d", "--parse-list-dir"):                 # A dir containing whole list pages
            parse_list_dir = True
        elif opt in ("-a", "--collect-all-db"):
            collect_all_db = True

    if dump_main_category is None and dump_sub_category is None and dump_commodity_from_sub_category_dirs is None and parse_list_file is None and parse_list_dir is None and collect_all_db is None:
        print_usage(argv[0])
        sys.exit()

    return dump_main_category, dump_sub_category, dump_commodity_from_sub_category_dirs, parse_list_file, parse_list_dir, collect_all_db



if __name__ == '__main__':
    try:

        dump_main_category, dump_sub_category, dump_commodity_from_sub_category_dirs, parse_list_file, parse_list_dir, collect_all_db = main(sys.argv) 


        if dump_main_category is not None:
            # Define Main Category Entry

            sixlucky_dump_main_category(sixlucky_categories.all_categories[ dump_main_category ])
            pass

        if dump_sub_category is not None:
            # Define Sub Category Entry

            main_cat = sixlucky_categories.all_categories[0]['main_cat']
            url = sixlucky_categories.all_categories[0]['sub_cats'][0]['url']
            sub_cat = sixlucky_categories.all_categories[0]['sub_cats'][0]['sub_cat']

            sixlucky_dump_sub_category(url, main_cat, sub_cat)
            pass

        if dump_commodity_from_sub_category_dirs is not None:
            # Define Sub Category Entry

            if True:  # debug first main category
                m = sixlucky_categories.all_categories[10]
                main_cat = m['main_cat']

                for s in m['sub_cats']:
                    sub_cat = s['sub_cat']
                    sub_cat_dir = sixlucky_get_directory(main_cat, sub_cat)
        
                    printf ("dump_commodity_from_sub_category_dirs, main_cat = %s, sub_cat = %s, dir = %s", main_cat, sub_cat, sub_cat_dir)
                    sixlucky_parse_list_dir(main_cat, sub_cat, sub_cat_dir)

            else:

                for m in sixlucky_categories.all_categories:
                    
                    main_cat = m['main_cat']
                    printf ("parse main catetories ... %s", main_cat)

                    for s in m['sub_cats']:
                        sub_cat = s['sub_cat']
                        sub_cat_dir = sixlucky_get_directory(main_cat, sub_cat)
        
                        printf ("dump_commodity_from_sub_category_dirs, main_cat = %s, sub_cat = %s, dir = %s", main_cat, sub_cat, sub_cat_dir)
                        sixlucky_parse_list_dir(main_cat, sub_cat, sub_cat_dir)

            pass

        if parse_list_file is not None:
            main_cat = sixlucky_categories.all_categories[0]['main_cat']
            sub_cat = sixlucky_categories.all_categories[0]['sub_cats'][1]['sub_cat']

            list_dir = sixlucky_get_directory(main_cat, sub_cat)
            list_file = list_dir + "/" + "list_0.html"

            sixlucky_parse_list_file(main_cat, sub_cat, list_file)
            pass
        
        if parse_list_dir is not None:
            main_cat = sixlucky_categories.all_categories[6]['main_cat']
            sub_cat = sixlucky_categories.all_categories[6]['sub_cats'][0]['sub_cat']

            list_dir = sixlucky_get_directory(main_cat, sub_cat)

            sixlucky_parse_list_dir(main_cat, sub_cat, list_dir)
            pass

        if collect_all_db is not None:

            all_products_db = "sixlucky/all.db"

            jagabee_sqlite3.db_create(all_products_db)

            if False:    # test
                m = sixlucky_categories.all_categories[0]
                main_cat = m['main_cat']

                s = m['sub_cats'][0]
                sub_cat = s['sub_cat']
                sub_cat_dir = sixlucky_get_directory(main_cat, sub_cat)
        
                printf ("collect_all_db, main_cat = %s, sub_cat = %s, dir = %s", main_cat, sub_cat, sub_cat_dir)
                jagabee_sqlite3.db_merge(sub_cat_dir + "/products.db", all_products_db)

            else:
                for m in sixlucky_categories.all_categories:
                    
                    main_cat = m['main_cat']

                    for s in m['sub_cats']:
                        sub_cat = s['sub_cat']
                        sub_cat_dir = sixlucky_get_directory(main_cat, sub_cat)
        
                        printf ("collect_all_db, main_cat = %s, sub_cat = %s, dir = %s", main_cat, sub_cat, sub_cat_dir)
                        jagabee_sqlite3.db_merge(sub_cat_dir + "/products.db", all_products_db)

                        pass

                    pass

                pass

        printf("done")
        sys.exit(0)

    except Exception, e:
        traceback.print_exc()
        sys.exit(-1)
