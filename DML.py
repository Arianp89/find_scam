#this file is to add change to adatabase

import mysql.connector
from config import db_config,database_name



def add_customer_black_list(customer_id,time,stage=1,don='no'):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM BLACK_LIST WHERE CUSTOMER_ID=%s", (customer_id,))
    user = cur.fetchone()
    if user==None:
        SQL_Query ="INSERT INTO BLACK_LIST (customer_id,STATUS,STAGE,DON,TIME) VALUES (%s,%s,%s,%s,%s);"
        cur.execute(SQL_Query, (customer_id,'yes',stage,don,time))
        conn.commit()
    else:
        SQL_Query = "UPDATE BLACK_LIST SET STATUS=%s,STAGE=%s,DON=%s,TIME=%s WHERE CUSTOMER_ID=%s;"
        cur.execute(SQL_Query, ('yes',stage,don,time,customer_id))
        conn.commit()
    cur.close()
    conn.close()

def came_customer_black_list(customer_id):
    print('came')
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "UPDATE BLACK_LIST SET STATUS=%s,DON=%s WHERE CUSTOMER_ID=%s;"
    cur.execute(SQL_Query, ('no','yes',customer_id))
    conn.commit()
    cur.close()
    conn.close()

    print('came')