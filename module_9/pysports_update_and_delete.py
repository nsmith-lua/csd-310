#Noah Smith 
#12/2/23

import mysql.connector


config = {
    'host': 'localhost',
    'user': 'root',
    'password': '..',
    'database': 'pysports'
}

db = mysql.connector.connect(**config)

cursor = db.cursor()

   
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

   
players = cursor.fetchall()    
   
print("\n <<<<<<<<<<<<<<DISPLAYING PLAYER RECORDS>>>>>>>>>>>>>>")
for player in players:
    print("Player_ID: {}\n First_Name: {}\n Last_Name: {}\n Team_Name: {}\n".format(player[0], player[1], player[2], player[3]))

print("\n <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>")


add_player = ("(first_name, last_name, team_id (%s, %s, %s)")
    
player_data = ("The", "Balrog", 1)  

cursor.execute(add_player, player_data)

print("\n <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>")
for player in players:
    print("Player_ID: {}\n First_Name: {}\n Last_Name: {}\n Team_Name: {}\n".format(player[0], player[1], player[2], player[3]))
print("\n <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>")

update_player = ("UPDATE player SET team_id = 1, first_name = 'Gollum', last_name = 'Balrog' WHERE first_name = 'The'")

cursor.execute(update_player)

print("\n <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>")
for player in players:
    print("Player_ID: {}\n First_Name: {}\n Last_Name: {}\n Team_Name: {}\n".format(player[0], player[1], player[2], player[3]))
print("\n <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>")

delete_player = ("DELETE FROM player WHERE first_name = 'The'")

cursor.execute(delete_player)
print("\n <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>")
for player in players:
    print("Player_ID: {}\n First_Name: {}\n Last_Name: {}\n Team_Name: {}\n".format(player[0], player[1], player[2], player[3]))
print("\n <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>")