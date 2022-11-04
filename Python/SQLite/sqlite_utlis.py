import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

def insert_into(table, values):
    res = cur.execute(("insert into {} values ({})").format(table,values))
    con.commit()
    return res