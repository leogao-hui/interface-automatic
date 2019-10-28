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

    name = ['reco_migrations', 'reco_rvw_states', 'reco_food_material_tag_categories', 'reco_food_material_apply_scenario_categories']

    for table in tables:
        if str(table[0]) not in name:
            delete_table_sql = 'delete from ' + table[0]
            cur.execute(delete_table_sql)
    db.commit()
    cur.execute(yes_func_foreign_key)
    db.close()

# delete_database_data_test_ci()


def add_database_data_ci():

    db = pymysql.connect(
        host=host,
        port=port,
        user=user,
        passwd=pass_wd,
        db=db_name)
    cur = db.cursor()

    add_scenario_one = "insert into reco_topics(id,name,rank) values('%s', '%s', '%s')" % (1, '分类1', 1)
    add_scenario_two = "insert into reco_topics(id,name,rank) values('%s', '%s', '%s')" % (2, '分类2', 2)
    add_tag_one = "insert into reco_tags(id,type,name) values('%s', '%s', '%s')" % (1, 'variable', '标签一')
    add_tag_two = "insert into reco_tags(id,type,name) values('%s', '%s', '%s')" % (2, 'variable', '随访关注')

    add_user = "insert into reco_administrator_departments(id,name) values('%s', '%s')" % (1, '测试')
    add_account = "insert into reco_administrators(id,name,administratorDepartmentId,phone,password,status) values('%s', '%s', '%s', '%s', '%s', '%s')" % (1, 'leogao', 1, 123456, 'MTIzNDU2', 'valid')
    cur.execute(add_scenario_one)
    cur.execute(add_scenario_two)
    cur.execute(add_tag_one)
    cur.execute(add_tag_two)
    cur.execute(add_user)
    cur.execute(add_account)

    db.commit()
    db.close()

add_database_data_ci()



