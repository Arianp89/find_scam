def add_customer_black_list(customer_id):
    conn = mysql.connector.connect(**db_confing, database=database_name)
    cur = conn.cursor()
    SQL_Query = "UPDATE CUSTOMER SET BLACK_LIST=%s WHERE ID=%s;"
    cur.execute(SQL_Query, ('yes',customer_id))
    conn.commit()
    cur.close()
    conn.close()
    logging.info(f'customer {customer_id} add black list')