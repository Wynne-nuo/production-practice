import pymysql
db = pymysql.connect(user = 'root',passwd = 'root',database = 'test')
cursor = db.cursor()
cursor.execute("SELECT 1+2")
data = cursor.fetchone()
print("Database version: %s " %data)
db.close()