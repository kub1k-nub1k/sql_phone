import sqlite3


def create_table():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    table = f"""
    CREATE TABLE IF NOT EXISTS phone_table (
        id INTEGER PRIMARY KEY,
        name TEXT,
        phone TEXT
    );
    """
    cursor.execute(table)

    conn.commit()
    conn.close()


def phone_create(phone_id, name, number):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    sql = "INSERT INTO phone_table (id, name, phone) VALUES (?, ?, ?)"
    cursor.execute(sql, (phone_id, name, number))

    conn.commit()
    conn.close()


def phone_read():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM phone_table")

    result = cursor.fetchall()

    conn.close()
    return result


def phone_update(phone_id, name, number):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    update_query = "UPDATE phone_table SET name = ?, phone = ? WHERE id = ?"
    cursor.execute(update_query, (name, number, phone_id))

    conn.commit()
    conn.close()


def phone_delete(id_phone):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    del_phone = f"""
    DELETE FROM phone_table
    WHERE id = ?
    """
    cursor.execute(del_phone, (id_phone,))

    conn.commit()
    conn.close()
