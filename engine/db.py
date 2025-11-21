from re import I
import sqlite3

conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

#cursor

cursor =conn.cursor()

# Create a table sys_command

# X

query= "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))" 
cursor.execute(query)

#Create a table web_command



# # #insert into table

# query= "INSERT INTO sys_command VALUES (null, 'ms word', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe')"
# cursor.execute(query)
# conn.commit()



query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

query= "INSERT INTO web_command VALUES (null, 'youtube', 'https://www.youtube.com/')"
cursor.execute(query)
conn.commit()