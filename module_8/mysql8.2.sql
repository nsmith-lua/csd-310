USE pysports;

SHOW TABLES;

DROP USER 'pysports_user'@'localhost';

CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'P@ssw0rd';

GRANT ALL PRIVILEGES ON pysports.* TO 'pysports_user'@'localhost';


DROP TABLE IF EXISTS player;

CREATE TABLE `team` ( 
team_id	INT 	NOT NULL 	AUTO_INCREMENT,
team_name 	VARCHAR(75) 	NOT NULL,
mascot		VARCHAR(75) 		NOT NULL,
PRIMARY KEY (team_id)
);


CREATE TABLE `player` ( 
player_id	INT 	NOT NULL 	AUTO_INCREMENT,
first_name 	VARCHAR(75) 	NOT NULL,
last_name	VARCHAR(75) 	NOT NULL,
team_id		INT 		NOT NULL,
PRIMARY KEY (player_id),
CONSTRAINT fk_team
FOREIGN KEY (team_id)
REFERENCES team(team_id)
);


INSERT INTO team( team_name, mascot) 
 VALUES ( 'Team Gandalf', 'White Wizards');

INSERT INTO team( team_name, mascot) 
 VALUES ( 'Team Sauron', 'Orcs');


source C:\Users\nsmit\Downloads\db_init.sql

SELECT team_id FROM team WHERE team_name = 'Team Sauron';

