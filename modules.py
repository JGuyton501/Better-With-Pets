from app import *
from datetime import datetime
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

class Lost_pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(75))
    phone = db.Column(db.String(15))
    type_of_pet = db.Column(db.String(20))
    name = db.Column(db.String(50))
    breed = db.Column(db.String(50))
    picture = db.Column(db.String(300))
    size = db.Column(db.String(15))
    color = db.Column(db.String(15))
    location = db.Column(db.String(100))
    found = db.Column(db.String(5))
    spotted = db.Column(db.Integer)

    def __init__(
    	self,
    	first_name, 
    	last_name, 
    	email, phone, 
    	type_of_pet, 
    	name, 
    	breed, 
    	picture, 
    	size, 
    	color, 
    	location, 
    	found, 
    	spotted
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.type_of_pet = type_of_pet
        self.name = name
        self.breed = breed
        self.picture = picture
        self.size = size
        self.color = color
        self.location = location
        self.found = found
        self.spotted = spotted

    def __repr__(self):
        return '<Pet %r>' % self.name

class Found_pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(75))
    phone = db.Column(db.String(15))
    type_of_pet = db.Column(db.String(20))
    name = db.Column(db.String(50))
    breed = db.Column(db.String(50))
    picture = db.Column(db.String(300))
    size = db.Column(db.String(15))
    color = db.Column(db.String(15))
    location = db.Column(db.String(100))
    found = db.Column(db.String(5))
    spotted = db.Column(db.Integer)

    def __init__(
    	self,
    	first_name, 
    	last_name, 
    	email, phone, 
    	type_of_pet, 
    	name, 
    	breed, 
    	picture, 
    	size, 
    	color, 
    	location, 
    	found, 
    	spotted
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.type_of_pet = type_of_pet
        self.name = name
        self.breed = breed
        self.picture = picture
        self.size = size
        self.color = color
        self.location = location
        self.found = found
        self.spotted = spotted

    def __repr__(self):
        return '<Pet %r>' % self.name

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
