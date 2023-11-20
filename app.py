from flask import Flask, render_template, url_for, redirect, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
import sqlite3
import markdown

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    username = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not bcrypt.check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login'))  # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('profile'))


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/about', methods=['GET', 'POST'])
# @login_required
def about():
    return render_template('about.html')


@app.route('/create', methods=('GET', 'POST'))
def create():
    conn = get_db_connection()

    if request.method == 'POST':
        content = request.form['content']
        id = current_user.id
        if not content:
            flash('Content is required!')
            return redirect(url_for('index'))
        conn.execute('INSERT INTO notes (content, user_id) VALUES (?, ?)', (content, id))
        conn.commit()
        conn.close()
        return redirect(url_for('notes'))

    return render_template('create.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():

    name = request.form.get('name')
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    hashed_password = bcrypt.generate_password_hash(password)
    new_user = User(name=name, username=username, password=hashed_password)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('login'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@app.route('/notes')
@login_required
def notes():
    conn = get_db_connection()
    # filter by user id
    id = current_user.id
    # only if user is logged in and user id matches notes will be displayed
    db_notes = conn.execute('SELECT created, content, user_id FROM notes WHERE user_id = ?', (id,)).fetchall()
    conn.close()

    notes = []
    for note in db_notes:
        note = dict(note)
        note['content'] = markdown.markdown(note['content'])
        notes.append(note)

    return render_template('notes.html', notes=notes)


@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
@login_required
def edit(note_id):
    conn = get_db_connection()

    if request.method == 'POST':
        # Update the note content in the database
        new_content = request.form['content']
        conn.execute('UPDATE notes SET content = ? WHERE id = ? AND user_id = ?;', (new_content, note_id, current_user.id))
        conn.commit()
        conn.close()
        flash('Note updated successfully!', 'success')
        return redirect(url_for('notes'))

    # Fetch the current note content for the user
    db_note = conn.execute('SELECT created, content FROM notes WHERE id = ? AND user_id = ?;', (note_id, current_user.id)).fetchone()

    if db_note is None:
        flash('Note not found or you do not have permission to edit this note.', 'danger')
        conn.close()
        return redirect(url_for('notes'))

    note = dict(db_note)
    note['content'] = markdown.markdown(note['content'])
    conn.close()

    return render_template('edit.html', note=note)

if __name__ == "__main__":
    app.run(debug=True)
