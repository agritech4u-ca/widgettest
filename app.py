from flask import Flask, request, jsonify
import pyodbc
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 🔐 Replace with your Azure SQL details
server = 'agritech4u.database.windows.net'
database = 'dev'
username = 'agritech4uadmin'
password = 'Nepean@1612'

connection_string = f'''
DRIVER={{ODBC Driver 17 for SQL Server}};
SERVER={server};
DATABASE={database};
UID={username};
PWD={password};
'''

# -----------------------------
# GET PROFILE
# -----------------------------
@app.route('/api/profile', methods=['GET'])
def get_profile():
    microsoft_id = "test-user-001"

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT FirstName, LastName, BusinessName, Email, Phone,
                   Address1, Address2, City, State, PostalCode
            FROM Customers
            WHERE MicrosoftID = ?
        """, microsoft_id)

        row = cursor.fetchone()
        conn.close()

        if row:
            return jsonify({
                "FirstName": row[0],
                "LastName": row[1],
                "BusinessName": row[2],
                "Email": row[3],
                "Phone": row[4],
                "Address1": row[5],
                "Address2": row[6],
                "City": row[7],
                "State": row[8],
                "PostalCode": row[9]
            })
        else:
            return jsonify({}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -----------------------------
# SAVE PROFILE (INSERT OR UPDATE)
# -----------------------------
@app.route('/api/profile', methods=['POST'])
def save_profile():
    data = request.json

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Check if user exists
        cursor.execute("SELECT COUNT(*) FROM Customers WHERE MicrosoftID = ?", data['MicrosoftID'])
        exists = cursor.fetchone()[0]

        if exists:
            # UPDATE
            cursor.execute("""
                UPDATE Customers SET
                    FirstName=?,
                    LastName=?,
                    BusinessName=?,
                    Email=?,
                    Phone=?,
                    Address1=?,
                    Address2=?,
                    City=?,
                    State=?,
                    PostalCode=?
                WHERE MicrosoftID=?
            """,
            data['FirstName'], data['LastName'], data['BusinessName'],
            data['Email'], data['Phone'],
            data['Address1'], data['Address2'],
            data['City'], data['State'], data['PostalCode'],
            data['MicrosoftID'])
        else:
            # INSERT
            cursor.execute("""
                INSERT INTO Customers (
                    MicrosoftID, FirstName, LastName, BusinessName,
                    Email, Phone, Address1, Address2, City, State, PostalCode
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            data['MicrosoftID'], data['FirstName'], data['LastName'], data['BusinessName'],
            data['Email'], data['Phone'],
            data['Address1'], data['Address2'],
            data['City'], data['State'], data['PostalCode'])

        conn.commit()
        conn.close()

        return jsonify({"status": "success"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)