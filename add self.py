import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Marina Ortega\Downloads\Database4.accdb;')

    user_id=11
    Fullname="Marina Ortega"
    Age=20
    Grade = 90
    Address = "Cavite"
    Birthdate="10/01/2002"

    data = connection.cursor()
    data.execute('update Table1 SET Grade=? WHERE id=?',(Grade,user_id))
    data.execute('update Table1 SET Address=? WHERE id=?', (Address, user_id))
    data.execute('update Table1 SET Age=? WHERE id=?', (Age, user_id))
    data.execute('update Table1 SET Fullname=? WHERE id=?', (Fullname, user_id))
    data.execute('update Table1 SET Birthdate=? WHERE id=?', (Birthdate, user_id))
    data.commit()
    print("Data is updated")



except pyodbc.Error:
    print("Error in Connection")