CREATE TABLE Users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  email VARCHAR(80) NOT NULL,
  display_name VARCHAR(50) NOT NULL,
  UNIQUE (email)
);
CREATE TABLE Orders (
  user_id INT NOT NULL,
  orders VARCHAR(80),
  PRIMARY KEY (user_id),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
CREATE TABLE Service (
  search_id INTEGER PRIMARY KEY AUTOINCREMENT,
  service_info VARCHAR(255)
);