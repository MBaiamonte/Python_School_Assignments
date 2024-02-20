from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    db="email_validation_schema"
    def __init__(self, data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all_users(cls):
        query="SELECT * FROM users"
        results=connectToMySQL(cls.db).query_db(query)
        users=[]
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save_new_user(cls, data):
        query= """
        INSERT INTO users (first_name, Last_name, email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s);"""
        results=connectToMySQL(cls.db).query_db(query,data)
        return results

    @staticmethod
    def validate_new_user(user): 
        is_valid=True
        if len(user['first_name']) < 2:
            flash("First Name Must Be two charters long.", "user")
            is_valid=False
        if len(user['last_name']) <2:
            flash("Last Name Must Be two charters long.", "user")
            is_valid=False
        if len(user['email']) == 0:
            flash("email cnat be empty", "user")
            is_valid=False
        elif  not EMAIL_REGEX.match(user['email']):
            flash("email must be in proper format", 'user')
        return is_valid

        
    












