import sqlite3

def execute_sqlite_script(db_path, sql_file):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(sql_file, "r") as f:
        sql_script = f.read()

    cursor.executescript(sql_script)
    conn.commit()
    conn.close()