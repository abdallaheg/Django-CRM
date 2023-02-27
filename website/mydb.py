import mysql.connector
dateBase =mysql.connector.connect(
    host ='localhost',
    user ='root',
    passwd='5528672',
)

cursorObject =dateBase.cursor()
cursorObject.execute("CREATE DATABASE Huntereg")
print("All Done!")