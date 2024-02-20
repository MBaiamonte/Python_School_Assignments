from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# from flask_app.controllers import users  //////dont need since redirecting in validation would result in no flashed messages besides bduplicate user


class User:
    db="login_and_registration_schema"
    def __init__(self, data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def save_new_user(cls, data):
        query="""
            Insert INTO users (first_name, last_name, age, email, password)
            VALUES (%(first_name)s,%(last_name)s, %(age)s, %(email)s, %(password)s);""" #these values need to match the value/name on the registration form in order to pas request.form in other wise youll need a data dictionary to convert the values with key-val pairs
        results= connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def get_all_users(cls):
        query="SELECT * FROM users"
        results= connectToMySQL(cls.db).query_db(query)
        all_users=[]
        for one_user in results:
            all_users.append(cls(one_user))
        return all_users

    @classmethod
    def get_user_by_email(cls,data):
        query="SELECT * FROM users WHERE email=%(email)s" #able to use login_email instead of email since were just passing in reqest.form to get the email value
        results= connectToMySQL(cls.db).query_db(query, data)
        if len(results) <1:
            print("No user with that email in DB,", "query returned=",results)
            return False
        return cls(results[0])

    @classmethod
    def get_user_by_id(cls, data):
        query="SELECT * FROM users Where id=%(id)s;"
        results= connectToMySQL(cls.db).query_db(query,data)
        if len(results) <1:
            return False
        return cls(results[0])



    @staticmethod
    def validate_user(data):
            # user=User.get_user_by_email(data) <--to get mapping error put data['registration_email']
            # if user:
            #     is_valid=False                                        
            #     flash("Email already in use", 'registration')
        #          return redirect ("/") #<---idk might not need this, would result in other validations not getting flashed if it failed because it would redirect and not continue through
        #^^^ this is set up correctly, its erroring out because i have defined "email" as two different variable names in my login vs registration forms. in the future keep form names generic and not specific for a form since the classmethod will have issues distingusing. or you could create a duplacuate classmethod for each form but that would violate the 'keep it simple stupid'/dont repeat the same code approch
            is_valid=True
            if len(data['registration_first_name'])==0:     
                flash("First name not entered", 'registration')
                is_valid=False
            elif len(data['registration_first_name']) <2:
                flash("First name must be at at least 2 characters long", 'registration')
                is_valid=False
            if len(data['registration_last_name'])== 0:     
                flash("Last name not entered", 'registration')
                is_valid=False
            elif len(data['registration_last_name']) <2:
                flash("Last name must be at at least 2 characters long", 'registration')
                is_valid=False
            # if int(data['registration_age'])  ==12:
            #     flash("not old enough to register", 'registration')
            #     is_valid=False
            # ^^this one works but will give error if age felid in from is submitted empty
            if len(data['registration_age']) ==0:
                flash("Age not entered", 'registration')
                is_valid=False
            if len(data['registration_age']) !=0 and int(data['registration_age']) <16:
                flash("Must be at least 16 years old","registration" )
                is_valid=False
            #^^^^ This version (chained conditions) will not error out if  age in form is submitted empty but will only flash the message if both conditions are true (so other validation was needed to flash for empty submission)
            if len(data['registration_email'])== 0:     
                flash("Email name not entered", 'registration')
                is_valid=False
            elif not EMAIL_REGEX.match(data['registration_email']):
                flash('Invalid email format','registration')
                is_valid=False
            if len(data['registration_password'])<8:
                flash("Password not entered", 'registration')
                is_valid=False
            if data['confirm_registration_password'] != data['registration_password']:
                flash("Passwords dont match", 'registration')
                is_valid=False
            return is_valid

    # @staticmethod
    # def validate_login(user_login_credentials):
    #     is_valid_login=True
    #     if not EMAIL_REGEX.match(user['login_email']):
    #         flash('Invalid email format','login')
    #         is_valid_login=False
    #     if not one_user:
    #         flash('email does not exist in DB', 'login') # should be flash("invalid credentials", 'login') for real project as to not give hoodlums extra implied information (aka unnecessary security risk)
    #         is_valid_login=False
    #     return is_valid_login

#^^^ not yet finished is only here to try log in validation on the model side, currently set validations are in controller

