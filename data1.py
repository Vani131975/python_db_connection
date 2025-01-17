import mysql.connector as c
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="vani"
)

if mydb.is_connected():
    print("Connection successful!")
else:
    print("Connection failed.")

mycursor = mydb.cursor()

while True:
    id = input("Enter player id (or type 'exit' to quit).... ")
    if id.lower() == 'exit':
        print("exiting the loop....")
        break

    name = input("Enter player name: ")
    score = input("Enter player score: ")
    city = input("Enter city: ")

    mycursor.execute("insert into cricket_player (id, name, score, city) VALUES (%s, %s, %s, %s)", (id, name, score, city))
    mydb.commit()
    print(f"Player {name} with ID {id} inserted successfully.")

id_to_delete = input("Enter player ID to delete: ")
mycursor.execute("delete from cricket_player where id = %s", (id_to_delete,))
mydb.commit()
print(f"Player with ID {id_to_delete} deleted successfully.")

print("Update player details. Give player ID and details to update.")
id_to_update = input("Enter player ID to update: ")
name_to_update = input("Enter player name: ")
score_to_update = input("Enter player score: ")
city_to_update = input("Enter city: ")

mycursor.execute("update cricket_player set name = %s, score = %s, city = %s where id = %s", (name_to_update, score_to_update, city_to_update, id_to_update))
mydb.commit()
print(f"Player with ID {id_to_update} updated successfully.")

mycursor.execute("select * from cricket_player")
result = mycursor.fetchall()
print("\nAll players")
for row in result:
    print(row)

mycursor.execute("select * from cricket_player order by name ASC")
player_sorted = mycursor.fetchall()
print("\nPlayers sorted by name")
for p in player_sorted:
    print(p)

mycursor.execute("select * from cricket_player where score between 70 AND 90")
player_score_range = mycursor.fetchall()
print("\nPlayers with score between 70 and 90 are")
for a in player_score_range:
    print(a)

mycursor.execute("select * from cricket_player where city = 'Hyderabad'")
player_from_hyderabad = mycursor.fetchall()
print("\nplayers from Hyderabad")
for b in player_from_hyderabad:
    print(b)
mydb.commit()

