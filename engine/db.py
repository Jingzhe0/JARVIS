from re import I
import sqlite3

conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

#cursor

cursor =conn.cursor()

# Create a table sys_command

# X

# query= "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))" 
# cursor.execute(query)

#Create a table web_command



# # #insert into table

# query= "INSERT INTO sys_command VALUES (null, 'ms word', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe')"
# cursor.execute(query)
# conn.commit()


# add url in url db
# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query= "INSERT INTO web_command VALUES (null, 'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)
# conn.commit()

# add contanct in number database
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255),email VARCHAR(255) NULL) ''')

# query="INSERT INTO contacts VALUES (null,'sarthak','8881931169', NULL)"
# cursor.execute(query)
# conn.commit()

query= 'sarthak'
query=query.strip().lower()

cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query +'%', query+ '%'))
results=cursor.fetchall()
print(results[0][0])

