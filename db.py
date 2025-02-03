import sqlite3

db = sqlite3.connect("Alexandru.db")
cur = db.cursor()


def init():
    create_server_script = open("sql/create_tables.sql")
    script_content = create_server_script.read()
    print("initializing tables...")
    cur.executescript(script_content)
    db.commit()
    create_server_script.close()


def insert_arr(table: str, content: str, id_server: str):
    cur.execute(
        f"INSERT INTO {table} (contet, id_server) VALUES (?, ?)", (content, id_server)
    )
    db.commit()


def delete_arr(table: str, content: str):
    cur.execute(f"DELETE FROM {table} WHERE content = ?", (content,))
    db.commit()


def insert_dict(table: str, key: str, content: str, id_server: str):
    cur.execute(
        f"INSERT INTO {table} (name, content, id_server) VALUES (?, ? ,?)",
        (key, content, id_server),
    )
    db.commit()


def remove_dict(table: str, key: str):
    cur.execute(f"DELETE FROM {table} where name = ?", (key,))
    db.commit()


def select(table: str):
    x = cur.execute(f"SELECT * FROM {table}")
    data = x.fetchall()
    return data
