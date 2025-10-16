import mysql.connector

#connect to server
cnx = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="rIshu@my89",
    database="esp_scores"
)

#Get a cursor
cursor = cnx.cursor()

#Taking Participant Inf0
def get_info():
    num_participant = int(input("How many Participant's data to be added ?  "))
    rows = []
    while num_participant>0:
        val1 = int(input("index number (sorry its a dumb mistake _ will delete later: )"))
        val2 = input("Enter the Name of Participant :  ")
        val3 = int(input("Enter the Batch (e.g.-2021,2022,2023...) :-"))
        print("Score Giving Guidelines:- WIN = +10 , LOSS = 0 , DRAW = +5")
        val4 = int(input("Enter Score :-"))
        rows.append(((val1,val2,val3,val4)))
        num_participant = num_participant - 1
    return rows

#Add Values to table SCORES
participant_rows = get_info()

#INSERT INTO TABLE
sql = "INSERT INTO scores(S_No,Name,Batch,Score) VALUES(%s,%s,%s,%s)"
val = participant_rows

cursor.executemany(sql,val)

cnx.commit()

print(cursor.rowcount, "record inserted")