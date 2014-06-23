# -*- coding: utf-8 -*-
import sys
import traceback
import getopt
import sqlite3

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

'''
    table product:
        barcode
        title
        vendor
        vendor_addr
        vendor_tel
        website
        reserv_date
        img_url
'''


def db_insert_rows(products, db_name):

    inserted_row_count = 0

    try:
        conn = sqlite3.connect(db_name)

        cur = conn.cursor()

        conn.text_factory = str

    except sqlite3.Error:
        print 'sqlite3.Error: insert fail due to table exist '

    except Exception, e:
        traceback.print_exc()

    for p in products:

        try:
            row = (p['barcode'], p['title'].encode('utf-8'), p['vendor'].encode('utf-8'), p['vendor_addr'].encode('utf-8'), p['vendor_tel'].encode('utf-8'), p['website'].encode('utf-8'), p['reserv_date'].encode('utf-8'), p['img_url'])

            cur.execute('INSERT INTO product VALUES (?,?,?,?,?,?,?,?)', row)

            inserted_row_count += 1

        except sqlite3.Error:
            print 'sqlite3.Error: insert fail due to table exist '
            traceback.print_exc()


    print 'db_insert_rows, inserted_row_count=%d' % inserted_row_count

    conn.commit()
    conn.close()

    return inserted_row_count



def db_create(db_name):

    try:
        conn = sqlite3.connect(db_name)

        cur = conn.cursor()

        # Create table
        cur.execute('''CREATE TABLE product
                             (barcode text PRIMARY KEY, title text, vendor text, vendor_addr text, vendor_tel text, website text, reserv_date text, img_url text)''')

    except sqlite3.OperationalError:
        print 'sqlite3.OperationalError: insert fail due to table exist '

    except Exception, e:
        traceback.print_exc()
        return False

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

    return True


def db_save_products(products, db_name = 'test.db'):

    ret = db_create(db_name)

    if not ret:
        return 0

    inserted_row_count = db_insert_rows(products, db_name)    

    return inserted_row_count


if __name__ == '__main__':
    try:

        sqlite3_create('test.db');

        sqlite3_execute_script_with_transaction('test.db');

        sqlite3_test('test.db');

        sys.exit(0)

        print "done"
        sys.exit(0)

    except Exception, e:
        traceback.print_exc()
        sys.exit(-1)

