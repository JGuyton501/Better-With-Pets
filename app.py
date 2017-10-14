import os,sys
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.debug = True

db = SQLAlchemy(app)
import modules

# PostgreSQL for Heroku
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/bwphack'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/social')
def social():
    return render_template('social.html')

@app.route('/lost-pet')
def lost_pet():
    return render_template('lost-pet.html')


# modules below
# post new user
@app.route('/new_user', methods=['POST'])
def new_user():
    user = modules.User(
        request.form['first_name'],
        request.form['last_name'],
        request.form['email'],
        request.form['password'],
        request.form['pet_owner']
        )

    db.session.add(user)
    db.session.commit()
    return redirect('/')



if __name__ == '__main__': 
	app.run()