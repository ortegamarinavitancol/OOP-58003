import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Marina Ortega\Downloads\Database4.accdb;')
    print("Database is Connected")

    data = connection.cursor()
    data.execute('SELECT * from Table1')
    for x in data.fetchall():
        print(x)

except pyodbc.Error:
    print("Error in Connection")