import sqlite3

from click import secho
def select():
    try:
        with sqlite3.connect("data.sqilte") as conn :
            sql_cmd = "select * from data;"
            for row in conn.execute(sql_cmd):
                print(row)
    except Exception as e:
        print("1")

select()