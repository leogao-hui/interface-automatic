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

    name = []

    for table in tables:
        if str(table[0]) not in name:
            delete_table_sql = 'delete from ' + table[0]
            cur.execute(delete_table_sql)
    db.commit()
    cur.execute(yes_func_foreign_key)
    db.close()


def add_database_data_test_ci():

    db = pymysql.connect(
        host=host,
        port=port,
        user=user,
        passwd=pass_wd,
        db=db_name)

    cur = db.cursor()

    query_one = 'insert into spzh_organization(id, name, parentid, num, usestatus, ' \
                'level, tranid) values (1, "总军区", "", 02, 0, 1, "")'
    query_two = 'insert into spzh_user(id, realname, username, deviceid, password, organizationnum, userrole, num, usestatus, morendevice, lastlogintime, status, lastloginerrortime, loginerrorcount, loginstatus, createtime, translaterealname, ip) values (1, "管理员", "admin", "", "0192023a7bbd73250516f069df18b500", 1, "管理员", 0, 0, "", "", "", "", "", "", "", "", "")'

    cur.execute(query_one)
    cur.execute(query_two)
    db.close()



