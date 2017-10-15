import os,sys
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.debug = True

db = SQLAlchemy(app)
import modules

# PostgreSQL for Heroku
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/bwphack'

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
	allLocations = modules.Parks.query.all()
	parks = modules.Parks.query.filter_by(type_of_park="Dog").all()
	shelters = modules.Parks.query.filter_by(type_of_park="Shelter").all()
	return render_template('main.html', allLocations = allLocations, parks = parks, shelters = shelters)

@app.route('/social')
def social():
    return render_template('social.html')

@app.route('/lost-pet')
def lost_pet():
	lost_pets = modules.Lost_pet.query.all()
	return render_template('lost-pet.html', lost_pets = lost_pets)

@app.route('/adopt')
def adopt():
	pets = modules.Pets.query.all()
	return render_template('adopt.html', pets = pets)

@app.route('/admin-main')
def admin_main():
	new_proposals = modules.Pet_Adopt.query.filter_by(status="new").all()
	recent_proposals = modules.Pet_Adopt.query.filter_by(status="recent").all()
	return render_template('admin-main.html', new_proposals = new_proposals, recent_proposals = recent_proposals)

@app.route('/pet/<petname>')
def pet(petname):
	pet = modules.Pets.query.filter_by(name=petname).first()
	pics = modules.Pet_Profile.query.filter_by(name=petname).order_by("id asc").all()
	return render_template('pet.html', pet = pet, pics = pics)

@app.route('/updatePicLikes/<picID>/<likes>', methods=['POST'])
def updatePicLikes(picID, likes):
	pic = modules.Pet_Profile.query.filter_by(id=picID).first()
	pic.likes = likes
	db.session.commit()
	return "Like Success"

@app.route('/updateProposalStatus/<proposalID>/<status>', methods=['POST'])
def updateProposalStatus(proposalID, status):
	proposal = modules.Pet_Adopt.query.filter_by(id=proposalID).first()
	modules.Pets.query.filter_by(name=proposal.pet_name).delete()
	proposal.status = status
	db.session.commit()
	return redirect('/admin-main')

@app.route('/deleteProposal/<proposalID>', methods=['POST'])
def deleteProposal(proposalID):
	modules.Pet_Adopt.query.filter_by(id=proposalID).delete()
	db.session.commit()
	return redirect('/admin-main')

@app.route('/lost_found_pet/<lostID>', methods=['POST'])
def lost_found_pet(lostID):
	found = modules.Lost_pet.query.filter_by(id=lostID).first()
	pet = modules.Found_pet(
		found.first_name,
		found.last_name,
		found.email,
		found.phone,
		found.type_of_pet,
		found.name,
		found.breed, 
		found.picture,
		found.size,
		found.color,
		found.location,
		found.found,
		found.spotted
	)
	db.session.add(pet)
	modules.Lost_pet.query.filter_by(id=lostID).delete()
	db.session.commit()
	return redirect('/admin-main')

@app.route('/updateSpots/<lostID>/<spots>', methods=['POST'])
def updateSpots(lostID, spots):
	doggie = modules.Lost_pet.query.filter_by(id=lostID).first()
	doggie.spotted = spots
	db.session.commit()
	return "Like Success"

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

# post new doggie
@app.route('/new_lost_pet', methods=['POST'])
def new_lost_pet():
	# print (request.form['first_name'],request.form['last_name'],request.form['email'],request.form['phone'],request.form['previous_owner'],request.form['first_time_adopt'],request.form['pet_safe'],request.form['other_pets'],request.form['other_pets_list'],request.form['why_adopt'],request.form['notes'],request.form['pet_name'],request.form['pet_color'],request.form['pet_age'],request.form['pet_picture'])
	doggie = modules.Lost_pet(
        request.form['first_name'],
        request.form['last_name'],
        request.form['email'],
        request.form['phone'],
        request.form['type_of_pet'],
        request.form['name'],
        request.form['breed'],
        request.form['picture'],
        request.form['size'],
        request.form['color'],
        request.form['location'],
        "no",
        1
        )
	db.session.add(doggie)
	db.session.commit()
	return redirect('/lost-pet')


##########################CLASSES################


if __name__ == '__main__': 
	app.debug = True
	app.run()