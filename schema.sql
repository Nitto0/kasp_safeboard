CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    vendor TEXT NOT NULL,
    name TEXT NOT NULL,
    UNIQUE (vendor, name)
);

CREATE TABLE IF NOT EXISTS versions (
    product_id INTEGER NOT NULL REFERENCES products(id),
    version TEXT NOT NULL,
    PRIMARY KEY (product_id, version)
);

CREATE TABLE IF NOT EXISTS vulnerabilities (
    id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(id),
    kla_id TEXT NOT NULL,
    description TEXT NOT NULL,
    publish_date TEXT NOT NULL,
    start_vuln_version TEXT NOT NULL,
    fixed_version TEXT NOT NULL
);