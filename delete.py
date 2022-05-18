import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Marina Ortega\Downloads\Database4.accdb;')

    user_id = 10
    data = connection.cursor()
    data.execute('Delete from Table1 where id=?',(user_id))
    data.commit()
    print("Data is deleted")

except pyodbc.Error:
    print("Error in Connection")