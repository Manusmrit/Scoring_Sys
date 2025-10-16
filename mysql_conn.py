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

#Execute a query
cursor.execute("desc scores;")

#fetch results
myresult = cursor.fetchall()

#Print Results
for x in myresult:
    print(x)
