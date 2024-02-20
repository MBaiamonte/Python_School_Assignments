from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja


class Dojo:
    db="dojos_and_ninjas_crud"
    def __init__(self,data):
        self.id=data['id']
        self.location=data['location']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.ninjas=[]

    @classmethod
    def save(cls,data):
        query= "INSERT INTO dojos (location) VALUES (%(location)s);"
        results=connectToMySQL(cls.db).query_db(query,data)
        return results

    @classmethod
    def get_all(cls):
        query="SELECT * FROM dojos;"
        results=connectToMySQL(cls.db).query_db(query)
        all_dojos=[]
        for dojo in results:
            all_dojos.append(cls(dojo))
        return all_dojos

    @classmethod
    def get_dojo_with_ninjas(cls, dojo_id):
        data={'id':dojo_id}
        query= 'SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id=dojos.id WHERE dojos.id=%(id)s'
        results = connectToMySQL(cls.db).query_db(query, data)
        dojo=cls(results[0])
        for row_from_db in results:
            ninja_data={
                'id':row_from_db['ninjas.id'],
                'first_name': row_from_db['first_name'],
                'last_name':row_from_db['last_name'],
                'age':row_from_db['age'], 
                'created_at':row_from_db['ninjas.created_at'],
                'updated_at':row_from_db['ninjas.updated_at'],
                'dojo_id':row_from_db["dojo_id"]
                }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo
        #moved data dict from controller to here, switched paramerter on line 30 from data to dojo_id
#also switched results from data to dojo_id on .query_db