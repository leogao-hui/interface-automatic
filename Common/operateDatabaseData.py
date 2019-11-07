# author:LEO GAO
# project Encoding:UTF-8


import pymysql
import os
import configparser

first = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
case_path = os.path.join(first, "config.ini")
config = configparser.ConfigParser()
config.read(case_path)


host = config.get("mysql", "host")
port = int(config.get("mysql", "port"))
user = config.get("mysql", "user")
pass_wd = config.get("mysql", "passwd")
db_name = config.get("mysql", "database")


def delete_database_data_test_ci():

    db = pymysql.connect(
        host=host,
        port=port,
        user=user,
        passwd=pass_wd,
        db=db_name)

    cur = db.cursor()

    no_func_foreign_key = 'SET FOREIGN_KEY_CHECKS = 0'
    yes_func_foreign_key = 'SET FOREIGN_KEY_CHECKS = 1'

    cur.execute(no_func_foreign_key)
    cur.execute('SHOW DATABASES')
    cur.execute('use ' + db_name)
    cur.execute('show tables')

    tables = cur.fetchall()

    name = ['gw_bank_card_bin', 'gw_bank_entity', 'gw_document', 'gw_yntrust_binding_config',
            'gw_job_lock', 'gw_channel_white_list']

    for table in tables:
        if str(table[0]) not in name:
            delete_table_sql = 'delete from ' + table[0]
            cur.execute(delete_table_sql)
    db.commit()
    cur.execute(yes_func_foreign_key)
    db.close()






