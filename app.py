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
	parks = Parks.query.all()
	return render_template('main.html', parks = parks)

@app.route('/social')
def social():
    return render_template('social.html')

@app.route('/lost-pet')
def lost_pet():
    return render_template('lost-pet.html')

@app.route('/adopt')
def adopt():
    return render_template('adopt.html')


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


##########################
# adding park
class Parks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_of_park = db.Column(db.String(20))
    name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phone = db.Column(db.String(15))
    picture = db.Column(db.String(300))
    rating = db.Column(db.String(300))
    description = db.Column(db.String(1000))

    def __init__(self, type_of_shelter, name, address, phone, picture, rating, description):
        self.type_of_park = type_of_park
        self.name = name
        self.address = address
        self.phone = phone
        self.picture = picture
        self.rating = rating
        self.description = description

    def __repr__(self):
        return '<Park number %r>' % self.phone

# #LOGIN
# @app.route('/post_login', methods=['POST'])
# def post_login():
#     form_email = request.form['email']
#     form_pass = request.form['password']
#     user = modules.User.query.filter_by(email=form_email).first()
#     if user is None:
#         print("No user with this email")
#     elif user.check_password(form_pass):
#         return redirect(url_for('dashboard'))
#     else:
#         print("Invalid password")
#     #return redirect(url_for('home'))
#     return render_template('main/login.html')


if __name__ == '__main__': 
	app.run()