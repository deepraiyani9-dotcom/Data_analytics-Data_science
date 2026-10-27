import sqlite3

# run code for make table in database
conn = sqlite3.connect('mydatabase.db')
cur = conn.cursor()
cur.execute("""
            insert into state (sname, cid) values ('Maharashtra', 1)
            insert into state (sname, cid) values ('Gujarat', 2)
            insert into state (sname, cid) values ('Rajasthan', 3)
            """)

print("Data inserted successfully.")
conn.commit()
conn.close()