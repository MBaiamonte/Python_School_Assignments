from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, redirect
from flask_app.controllers import users
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt= Bcrypt(app)
import re
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    db='recipes_schema'
    def __init__(self, data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.updated_at=data['updated_at']
        self.created_at=data['created_at']
        self.recipes=[]

    @classmethod
    def save_new_user(cls,data):
        query=""" INSERT INTO users (first_name, last_name, email, password)
            VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"""
        results=connectToMySQL(cls.db).query_db(query,data)
        print("results returned=",results)
        return results

    @classmethod
    def get_user_by_email(cls, data):
        query="SELECT * FROM users WHERE email=%(email)s"
        results=connectToMySQL(cls.db).query_db(query,data)
        if len(results) <1:
            print("no matching email in database. results returned=", results)
            return False
        return cls(results[0])
    
    @classmethod
    def get_user_by_id(cls, data):
        query="SELECT * FROM users WHERE id=%(id)s"
        results=connectToMySQL(cls.db).query_db(query,data)
        if len(results)<1:
            print("no matching id in database. results returned=", results)
            return False
        return cls(results[0])

    @staticmethod
    def validate_new_user_registration_form(data):
        is_valid=True
        some_user=User.get_user_by_email(data)
        if some_user:
            is_valid=False
            flash("Try a different Email address", 'registration')
        #^^^ email not already being used^^^^
        if len(data['first_name']) ==0:
            is_valid=False
            flash("First Name not entered", "registration")
        if len(data['first_name']) !=0 and len(data['first_name']) <2:
            is_valid=False
            flash("First Name must be at least 2 characters long", "registration")
        # ^^^first name validations^^^
        if len(data['last_name']) ==0:
            is_valid=False
            flash("Last Name not entered", "registration")
        if len(data['last_name']) !=0 and len(data['last_name']) <2:
            is_valid=False
            flash("Last Name must be at least 2 characters long", "registration")
        #^^^ last name validations
        if len(data['email']) ==0:
            is_valid=False
            flash("Email not entered", "registration")
        if len(data['email']) !=0 and not EMAIL_REGEX.match(data['email']):
            is_valid=False
            flash("Invalid Email format", "registration")
        # ^^^ email Validations (no matching email is at top of validations)
        if len(data['password']) ==0:
            is_valid=False
            flash("Password not entered", "registration")
        if len(data['password']) !=0 and len(data['password']) <8:
            is_valid=False
            flash("Password must be at least 8 characters long", "registration")
        if len(data['confirm_password'])==0 and len(data['password']) !=0:
            is_valid=False
            flash("Confirm password cant be empty", 'registration')
        if len(data['password']) !=0 and len(data['confirm_password'])!=0 and len(data['password']) <8  and data['password'] != data['confirm_password']:
            is_valid=False
            flash("Passwords dont match", 'registration')
        return is_valid

    @staticmethod
    def validate_user_login(data):
        is_valid=True
        registered_user=User.get_user_by_email(data)
        if len(data['email'])==0:
            is_valid=False
            flash("no email entered", "login")
        if len(data['email'])!=0 and len(data['password'])==0:
            flash('password not entered', 'login')
        if not registered_user:
            is_valid=False
            flash("No user with that email", 'login') #change to invalid cred. on real site
            return redirect("/")
        if not bcrypt.check_password_hash(registered_user.password, data['password']):
            is_valid=False
            flash("incorrect password", 'login')
            redirect("/")
        session['logged_in_user_id']=registered_user.id
        return is_valid
                

