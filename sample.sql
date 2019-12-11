CREATE TABLE posts ( 
  id bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  subject varchar(255) NOT NULL,
  content mediumtext,
  created datetime,
  user_id int(10) unsigned NOT NULL,
  user_name varchar(32) NOT NULL,
  hit int(10) unsigned NOT NULL default '0',  
  PRIMARY KEY (id)
);


CREATE TABLE sample ( 
  no int(3) unsigned NOT NULL ,
  name char(20) NOT NULL,
  tel varchar(20) NOT NULL,
  etc varchar(50),
  created datetime,
  PRIMARY KEY (no)
);