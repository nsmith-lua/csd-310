SHOW DATABASES;


USE pysports;

SELECT player_id, first_name, last_name, team_name
FROM player
LEFT OUTER JOIN team
ON player.team_id = team.team_id;