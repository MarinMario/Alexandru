CREATE TABLE IF NOT EXISTS Server (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discord_id VARCHAR(255),
    welcome_channel VARCHAR(255),
    welcome_message VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS Quote (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content VARCHAR(255),
    id_server INTEGER,
    FOREIGN KEY (id_server) REFERENCES Server(id)
);
CREATE TABLE IF NOT EXISTS Reply (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    content VARCHAR(255),
    id_server INTEGER,
    FOREIGN KEY (id_server) REFERENCES Server(id)
);
CREATE TABLE IF NOT EXISTS Media (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    content VARCHAR(255),
    id_server INTEGER,
    FOREIGN KEY (id_server) REFERENCES Server(id)
);