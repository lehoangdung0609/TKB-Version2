import pyodbc

def connectDTU():
    server = '10.0.1.191'
    database = 'TKB_VERSION2'
    username = 'posct'
    password = 'postct@2018*'
    driver = '{SQL Server}'  # Driver you need to connect to the database ODBC Driver 11 for SQL Server
    cnxn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    return cursor
def connectLocal():
    server = '192.168.1.77'
    database = 'TKB_VERSION2'
    username = 'sa'
    password = '123456'
    driver = '{SQL Server}'  # Driver you need to connect to the database ODBC Driver 11 for SQL Server
    cnxn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    return cursor
