from flaskr import app
from flask import render_template, request, redirect, url_for
import sqlite3
DATABASE = 'database.db'

@app.route('/')
def index():
    return render_template(
        'index.html'
        )


@app.route('/form')
def form():
    return render_template(
        'form.html'
        )

@app.route('/register', methods=['POST'])
def register():
    title = request.form['title']
    detail = request.form['detail']
    due = request.form['due']

    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO todos (title, detail, due) VALUES(?, ?, ?)',
                [title, detail, due])
    con.commit()
    con.close()
    return redirect(url_for('todo'))

@app.route('/delete/<int:id>')
def delete(id):
    con = sqlite3.connect(DATABASE)
    con.execute('DELETE FROM todos WHERE todos.id=?', [id])
    con.commit()
    con.close()
    return redirect(url_for('todo'))

@app.route('/todo')
def todo():
    con = sqlite3.connect(DATABASE)
    db_todos = con.execute('SELECT id, title, detail, due FROM todos').fetchall()
    con.close()

    todos = []
    for row in db_todos:
        todos.append({'id': row[0], 'title': row[1], 'detail': row[2], 'due': row[3]})
    return render_template(
        'todo.html',
        todos = todos
        )

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    password = request.form['password']

    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO users (name, password) VALUES(?, ?)',
                [name, password])
    con.commit()
    con.close()
    return redirect(url_for('todo'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return redirect(url_for('index'))
   