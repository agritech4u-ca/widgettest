import pyodbc

server = 'agritech4u.database.windows.net'
database = 'dev'
username = 'agritech4uadmin'
password = 'Nepean@1612'

conn_str = f"""
DRIVER={{ODBC Driver 17 for SQL Server}};
SERVER={server};
DATABASE={database};
UID={username};
PWD={password};
"""

try:
    conn = pyodbc.connect(conn_str)
    print("✅ Connected successfully!")

    cursor = conn.cursor()
    cursor.execute("SELECT GETDATE()")
    row = cursor.fetchone()

    print("Server time:", row[0])

    conn.close()

except Exception as e:
    print("❌ Connection failed:")
    print(e)