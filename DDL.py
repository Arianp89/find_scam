def create_database(database_name):
    conn=mysql.connector.connect(**db_confing)
    cur=conn.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {database_name};")
    cur.execute(f"CREATE database {database_name} ;")
    conn.commit()
    cur.close()
    conn.close()
    print(f'database {database_name} created successfully')
    logging.info(f'database {database_name} created successfully')


def create_table_customer(database_name):
    conn=mysql.connector.connection.MySQLConnection(**db_confing, database=database_name)
    cur=conn.cursor()
    SQL_Query="""
    CREATE TABLE CUSTOMER(
    `ID`                BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `NAME`              VARCHAR(20) ,
    `PHONE`             VARCHAR(11) ,
    `EMAIL`             VARCHAR(50) ,
    `PASSWORD`          VARCHAR(50) ,
    `BLACK_LIST`        VARCHAR(5)  ,
    `REGISTER_DATE`     DATETIME DEFAULT CURRENT_TIMESTAMP,
    `LAST_UPDATE`       DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
    """
    cur.execute(SQL_Query)
    conn.commit()
    cur.close()
    conn.close()
    print(f'table customer created successfully')
    logging.info(f'table customer created successfully')