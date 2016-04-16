CREATE TABLE Users (
  user_id INT NOT NULL,
  email VARCHAR(80) NOT NULL,
  display_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (user_id),
  UNIQUE (email)
);
CREATE TABLE Orders (
  user_id INT NOT NULL,
  orders VARCHAR(80),
  PRIMARY KEY (user_id),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
CREATE TABLE Service (
  user_id INT NOT NULL,
  service_info,
  PRIMARY KEY (user_id),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);