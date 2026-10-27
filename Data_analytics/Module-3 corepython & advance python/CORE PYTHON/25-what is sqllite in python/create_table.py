import sqlite3

# run code for make table in database
conn = sqlite3.connect('mydatabase.db')
cur = conn.cursor()
cur.execute("""
            create table if not exists country (
                cid integer primary key autoincrement,
                cname text ,
                created_at text
                )
            """)
cur.execute("""
            create table if not exists state (
                sid integer primary key autoincrement,
                sname text ,
                cid integer references country(cid)
            )
            """)
print("Table created successfully.")
conn.commit()
conn.close()