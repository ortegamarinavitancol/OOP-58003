import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Marina Ortega\Downloads\Database4.accdb;')

    user_id=1
    Grade = 100
    Address = "Mandaluyong"

    data = connection.cursor()
    data.execute('update Table1 SET Grade=? WHERE id=?',(Grade,user_id))
    data.execute('update Table1 SET Address=? WHERE id=?', (Address, user_id))
    data.commit()
    print("Data is updated")



except pyodbc.Error:
    print("Error in Connection")