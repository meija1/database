import psycopg2

connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()

cursor.execute('SELECT * FROM "Artist"')

results = cursor.fetchall()

connection.close()

for result in results:
    print(result)
