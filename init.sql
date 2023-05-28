CREATE DATABASE IF NOT EXISTS names;

USE names;

CREATE TABLE IF NOT EXISTS counts (
  ID int NOT NULL AUTO_INCREMENT,
  count int NULL,
  Filename varchar(200) NULL,
  PRIMARY KEY (ID)
);