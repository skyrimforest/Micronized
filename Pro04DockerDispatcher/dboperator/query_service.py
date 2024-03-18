import sqlite3
import BaseConfig
db_path=BaseConfig.DB_PATH

def get_cur():
    conn = sqlite3.connect(db_path+"/database.db")
    cur = conn.cursor()
    return cur

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





