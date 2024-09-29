from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('health_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            blood_pressure INTEGER,
            exercise_hours INTEGER,
            diet TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_data', methods=['POST'])
def submit_data():
    user_id = request.json.get('user_id')
    blood_pressure = request.json.get('blood_pressure')
    exercise_hours = request.json.get('exercise_hours')
    diet = request.json.get('diet')

    conn = sqlite3.connect('health_data.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO user_data (user_id, blood_pressure, exercise_hours, diet)
        VALUES (?, ?, ?, ?)
    ''', (user_id, blood_pressure, exercise_hours, diet))
    conn.commit()
    conn.close()

    return jsonify({"message": "Data submitted successfully!"}), 200

@app.route('/view_data', methods=['GET'])
def view_data():
    conn = sqlite3.connect('health_data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM user_data')
    data = c.fetchall()
    conn.close()

    return render_template('view_data.html', data=data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
