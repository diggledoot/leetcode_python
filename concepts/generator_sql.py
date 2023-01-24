import sqlite3


def get_data_from_db(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM large_table")
    while True:
        rows = cursor.fetchmany(1000)  # fetch 1000 rows at a time
        if not rows:  # if rows equals to None
            break
        for row in rows:
            yield row
    cursor.close()
    conn.close()


for data in get_data_from_db("large_db.db"):
    # Do something with data
    print(data)
