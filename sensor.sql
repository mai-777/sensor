CREATE TABLE IF NOT EXISTS valores (
    id_medicion INTEGER PRIMARY KEY AUTOINCREMENT,
    valor_sensor INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);