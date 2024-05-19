import logging
from flask import Flask, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
# Corrected import statement
from forms import LoginForm, RegistrationForm
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-secret-key')

# Initialize the database
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Initialize the login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Define the User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Define routes for the application
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            app.logger.info(f'User {user.username} logged in successfully.')
            # Redirect to image page after login
            return redirect(url_for('image_page'))
        else:
            flash('Invalid username or password', 'error')
            app.logger.warning(f'Failed login attempt for username: {form.username.data}')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user is None:
            # Corrected hash method to 'sha256'
            hashed_password = generate_password_hash(form.password.data, method='sha256')
            new_user = User(username=form.username.data, password=hashed_password)
            try:
                db.session.add(new_user)
                db.session.commit()
                # Display success message after registration
                flash('Account created successfully! Please log in.', 'success')
                return redirect(url_for('login'))
            except Exception as e:
                db.session.rollback()
                flash('An error occurred during registration. Please try again.', 'error')
                app.logger.error(f'Registration error: {e}')
        else:
            flash('Username already exists.', 'error')
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    # This page is only accessible to authenticated users
    return render_template('dashboard.html')

@app.route('/image_page')
@login_required
def image_page():
    # This page displays an image after a successful login
    return render_template('image.html')

# Test route to trigger flash message
@app.route('/test_flash')
def test_flash():
    flash('This is a test flash message!', 'info')
    return redirect(url_for('home'))

# Check if the script is the main application and run it
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5001)
