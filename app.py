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
	pets = Pets.query.all()
	return render_template('adopt.html', pets = pets)

@app.route('/admin-main')
def admin_main():
	new_proposals = Pet_Adopt.query.filter_by(status="new").all()
	recent_proposals = Pet_Adopt.query.filter_by(status="recent").all()
	return render_template('admin-main.html', new_proposals = new_proposals, recent_proposals = recent_proposals)

@app.route('/pet/<petname>')
def pet(petname):
	pet = Pets.query.filter_by(name=petname).first()
	pics = Pet_Profile.query.filter_by(name=petname).order_by("id asc").all()
	return render_template('pet.html', pet = pet, pics = pics)

@app.route('/updatePicLikes/<picID>/<likes>', methods=['POST'])
def updatePicLikes(picID, likes):
	pic = Pet_Profile.query.filter_by(id=picID).first()
	pic.likes = likes
	db.session.commit()
	return "Like Success"

@app.route('/updateProposalStatus/<proposalID>/<status>', methods=['POST'])
def updateProposalStatus(proposalID, status):
	proposal = Pet_Adopt.query.filter_by(id=proposalID).first()
	proposal.status = status
	db.session.commit()
	return redirect('/admin-main')

@app.route('/deleteProposal/<proposalID>', methods=['POST'])
def deleteProposal(proposalID):
	print(Pet_Adopt.query.filter_by(id=proposalID).first())
	Pet_Adopt.query.filter_by(id=proposalID).delete()
	db.session.commit()
	return redirect('/admin-main')


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

# post new proposal
@app.route('/new_proposal', methods=['POST'])
def new_proposal():
	# print (request.form['first_name'],request.form['last_name'],request.form['email'],request.form['phone'],request.form['previous_owner'],request.form['first_time_adopt'],request.form['pet_safe'],request.form['other_pets'],request.form['other_pets_list'],request.form['why_adopt'],request.form['notes'],request.form['pet_name'],request.form['pet_color'],request.form['pet_age'],request.form['pet_picture'])
	proposal = modules.Pet_Adopt(
        request.form['first_name'],
        request.form['last_name'],
        request.form['email'],
        request.form['phone'],
        request.form['previous_owner'],
        request.form['first_time_adopt'],
        request.form['pet_safe'],
        request.form['other_pets'],
        request.form['other_pets_list'],
        request.form['why_adopt'],
        request.form['notes'],
        request.form['pet_name'],
        request.form['pet_color'],
        request.form['pet_age'],
        request.form['pet_picture'],
        "new"
        )
	db.session.add(proposal)
	db.session.commit()
	return redirect('/main')


##########################CLASSES################
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

    def __init__(self, type_of_park, name, address, phone, picture, rating, description):
        self.type_of_park = type_of_park
        self.name = name
        self.address = address
        self.phone = phone
        self.picture = picture
        self.rating = rating
        self.description = description

    def __repr__(self):
        return '<Park number %r>' % self.phone

class Pets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_of_pet = db.Column(db.String(20))
    name = db.Column(db.String(50))
    breed = db.Column(db.String(50))
    age = db.Column(db.String(15))
    picture = db.Column(db.String(300))
    banner = db.Column(db.String(300))
    size = db.Column(db.String(15))
    color = db.Column(db.String(15))
    description = db.Column(db.String(1000))
    location = db.Column(db.String(100))

    def __init__(self, type_of_pet, name, breed, age, picture, banner, size, color, description, location):
        self.type_of_pet = type_of_pet
        self.name = name
        self.breed = breed
        self.age = age
        self.picture = picture
        self.banner = banner
        self.size = size
        self.color = color
        self.description = description
        self.location = location

    def __repr__(self):
        return '<Pet %r>' % self.name

class Pet_Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    picture = db.Column(db.String(300))
    caption = db.Column(db.String(300))
    likes = db.Column(db.Integer)

    def __init__(self, name, picture, caption, likes):
        self.name = name
        self.picture = picture
        self.caption = caption
        self.likes = likes

    def __repr__(self):
        return '<Park id %r>' % self.id

class Pet_Adopt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(75))
    phone = db.Column(db.String(15))
    previous_owner = db.Column(db.String(15))
    first_time_adopt = db.Column(db.String(5))
    pet_safe = db.Column(db.String(5))
    other_pets = db.Column(db.String(5))
    other_pets_list = db.Column(db.String(200))
    why_adopt = db.Column(db.String(1000))
    notes = db.Column(db.String(1000))
    pet_name = db.Column(db.String(50))
    pet_color = db.Column(db.String(15))
    pet_age = db.Column(db.String(15))
    pet_picture = db.Column(db.String(250))
    status = db.Column(db.String(10))

	
    def __init__(
    	self, 
    	first_name, 
    	last_name, 
    	email, 
    	phone,
    	previous_owner,
    	first_time_adopt,
    	pet_safe,
    	other_pets,
    	other_pets_list,
    	why_adopt,
    	notes,
    	pet_name,
    	pet_color,
    	pet_age,
    	pet_picture,
    	status
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.previous_owner = previous_owner
        self.first_time_adopt = first_time_adopt
        self.pet_safe = pet_safe
        self.other_pets = other_pets
        self.other_pets_list = other_pets_list
        self.why_adopt = why_adopt
        self.notes = notes
        self.pet_name = pet_name
        self.pet_color = pet_color
        self.pet_age = pet_age
        self.pet_picture = pet_picture,
        self.status = status

    def __repr__(self):
        return '<Pet %r>' % self.first_name


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
	app.debug = True
	app.run()