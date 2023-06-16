from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL connection
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'srepoc123'
app.config['MYSQL_DB'] = 'srepoc'

mysql = MySQL(app)

# Routes for CRUD operations and HTML forms
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET'])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM user')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/users', methods=['POST'])
def create_user():
    cur = mysql.connection.cursor()
    username = request.form['username']
    fname = request.form['fname']
    lname = request.form['lname']
    age = request.form['age']
    # Validate and sanitize input if necessary
    cur.execute("INSERT INTO user (username, fname, lname, age) VALUES (%s, %s, %s, %s)",
                (username, fname, lname, age))
    mysql.connection.commit()
    cur.close()
    return 'User created successfully'

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    cur = mysql.connection.cursor()
    fname = request.form['fname']
    lname = request.form['lname']
    age = request.form['age']
    # Validate and sanitize input if necessary
    cur.execute("UPDATE user SET fname = %s, lname = %s, age = %s WHERE id = %s",
                (fname, lname, age, user_id))
    mysql.connection.commit()
    cur.close()
    return 'User updated successfully'

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM user WHERE id = %s", (user_id,))
    mysql.connection.commit()
    cur.close()
    return 'User deleted successfully'

if __name__ == '__main__':
    app.run(debug=True)