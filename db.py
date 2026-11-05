import sqlite3
from pathlib import Path


def get_data(product):
    db_path = Path("vulnerabilities.db")
    if not db_path.exists():
        raise ValueError("Введите команду python main.py init для создания таблицы")

    conn = sqlite3.connect(db_path)
    try:
        row = conn.execute("SELECT id FROM products WHERE name = ? COLLATE NOCASE",
                           (product,)).fetchone()
        if row is None:
            raise ValueError("Продукт не найден в базе")

        product_id = row[0]
        versions = conn.execute("SELECT version FROM versions WHERE product_id = ?",
                                (product_id,)).fetchone()
        vuln = conn.execute(
            '''
            SELECT kla_id, description, publish_date, start_vuln_version, fixed_version
            FROM vulnerabilities WHERE product_id = ?
            ORDER BY publish_date, kla_id
            ''',
            (product_id,)
        )
        return versions, vuln
    finally:
        conn.close()
