from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Подключение к базе данных
def get_db_connection():
    conn = sqlite3.connect('hotel.db')
    conn.row_factory = sqlite3.Row
    return conn

# Маршрут для главной страницы
@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        # ... другие поля формы ...
        conn.execute('INSERT INTO guests (first_name, last_name, ...) VALUES (?, ?, ...)',
                     (first_name, last_name, ...))
        conn.commit()
        return redirect(url_for('index'))
    guests = conn.execute('SELECT * FROM guests').fetchall()
    conn.close()
    return render_template('index.html', guests=guests)


if __name__ == '__main__':
    app.run(debug=True)

