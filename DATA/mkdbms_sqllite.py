#!/usr/bin/python3
import sys
import os
import sqlite3

myconn = sqlite3.connect("presidents.db")

cu = myconn.cursor()

table_check_sql = """
    select count(*)
    from sqlite_master
    where
        type = 'table'
        and
        name = 'presidents'
"""

cu.execute(table_check_sql)
result = cu.fetchone()
if result[0] > 0:
    cu.execute("drop table presidents")

with open('mkpres.sql') as MKPRES:
    sql_to_build_db = MKPRES.read()

cu.executescript(sql_to_build_db)
myconn.commit()
cu.close()
myconn.close()
