#this file is for get database data 

import mysql.connector
from config import db_config,database_name

def get_black_list_list():
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_QUERY = "SELECT * FROM BLACK_LIST;"
    cur.execute(SQL_QUERY)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return [row['CUSTOMER_ID'] for row in data]



def get_customer_black(customer_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_QUERY = "SELECT * FROM BLACK_LIST WHERE CUSTOMER_ID=%s;"
    cur.execute(SQL_QUERY , (customer_id, ))
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data

def check_black_list(customer_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True) 
    SQL_Query = "SELECT STATUS FROM BLACK_LIST  WHERE CUSTOMER_ID=%s;"
    cur.execute(SQL_Query,(customer_id,))
    data = cur.fetchone()
    cur.close()
    conn.close()
    if data==None:
        return False
    if data['STATUS']=='yes':
        return True
    return False
