-- creates the database hbtn_0d_usa and the table states on the MYSQL server
-- creates the data base
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use database
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, namr VARCHAR9256) NOT NULL, PRIMARY KEY(id));
