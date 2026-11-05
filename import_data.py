import json
import sqlite3
from pathlib import Path


def create_tables():
    with open("data/versions.json", "r") as file:
        versions = json.load(file)

    with open("data/vulnerabilities.json", "r") as file:
        vuln = json.load(file)

    conn = sqlite3.connect("vulnerabilities.db")
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(Path("schema.sql").read_text(encoding="utf-8"))

    products = set()

    for ver in versions:
        products.add((ver['vendor'], ver['product']))
    for v in vuln:
        products.add((v['vendor'], v['product']))

    for product in products:
        conn.execute("INSERT INTO products (vendor, name) VALUES (?, ?)",
                     (product[0], product[1]))

    for version in versions:
        row = conn.execute("SELECT id from products WHERE vendor = ? AND name = ?",
                           (version['product'], version['vendor']),).fetchone()

        product_id = row[0]
        conn.execute("INSERT INTO versions (product_id, version) VALUES (?, ?)",
                     (product_id, version['version']),)
