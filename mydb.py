
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Jungkookismyway7_'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE name")

print("All Done!")