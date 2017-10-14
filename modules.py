from app import *
from datetime import datetime
# registering users into database
# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(80))
#     last_name = db.Column(db.String(80))
#     email = db.Column(db.String(120), unique=True)
#     password = db.Column(db.String(250))
#     pet_owner = db.Column(db.String(5))
   
#     def __init__(
#         self,
#         first_name,
#         last_name,
#         email,
#         password,
#         pet_owner
#     ):

#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.password = password
#         self.pet_owner = pet_owner

#     def __repr__(self):
#         return '<Name %r>' % self.email



# # adding park
# class Parks(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     type_of_park = db.Column(db.String(20))
#     name = db.Column(db.String(50))
#     address = db.Column(db.String(50))
#     phone = db.Column(db.String(15))
#     picture = db.Column(db.String(300))
#     rating = db.Column(db.String(300))
#     description = db.Column(db.String(1000))

#     def __init__(self, type_of_shelter, name, address, phone, picture, rating, description):
#         self.type_of_park = type_of_park
#         self.name = name
#         self.address = address
#         self.phone = phone
#         self.picture = picture
#         self.rating = rating
#         self.description = description

#     def __repr__(self):
#         return '<Park number %r>' % self.phone
