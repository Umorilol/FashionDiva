DROP TABLE IF EXISTS user;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE wardrobe (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    user_id INTEGER NOT NULL UNIQUE, 
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE clothing_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    wardrobe_id INTEGER NOT NULL,
    image_path TEXT NOT NULL,
    item_type TEXT,
    attributes TEXT,
    embedding BLOB,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (wardrobe_id) REFERENCESwardrobes(id)
);
