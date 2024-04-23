import sqlite3
import BaseConfig
db_path=BaseConfig.DB_PATH

# 创建新的连接与游标
def get_cursor(dbname):
    global db_path
    db_path=db_path+'/'+dbname+'.db'
    cnx = sqlite3.connect(db_path)
    cur = cnx.cursor()
    return cnx,cur

# 释放连接与游标
def delete_cursor(cnx,cur):
    cur.close()
    cnx.commit()
    cnx.close()

# 做select操作
def select_ope(cur,select_sql):
    cur.execute(select_sql)
    res=cur.fetchall()
    return res

# 做insert操作
def insert_ope(cur,insert_sql,data):
    cur.execute(insert_sql,data)
    cur.commit()


def do_insert(insert_sql,data):
    conn = sqlite3.connect(db_path+"/database.db")
    cur = conn.cursor()
    cur.execute(insert_sql,data)
    conn.commit()
    conn.close()

def do_select(select_sql):
    conn = sqlite3.connect(db_path+"/database.db")
    cur = conn.cursor()
    res=cur.execute(select_sql).fetchall()
    conn.commit()
    conn.close()
    return res





