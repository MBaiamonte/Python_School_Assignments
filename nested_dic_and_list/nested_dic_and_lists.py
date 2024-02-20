
print('Task 1  ---------------------------------------------------------------------------------')
x = [ [5,2,3], [10,8,9] ] 

x[1][0]=15
print(x)

print('Task 2  ---------------------------------------------------------------------------------')
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name']="Bryant"
print(students[0]['last_name'])

print('Task 3  ---------------------------------------------------------------------------------')
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0]='Andres'
print(sports_directory['soccer'])

print('Task 4  ---------------------------------------------------------------------------------')
z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z)


print('Task 5  ---------------------------------------------------------------------------------')
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(student_list):
    for student in student_list:
        for key in student:
            print(key,"-" ,student[key] )
        
iterateDictionary(students)
print('Task 6  ---------------------------------------------------------------------------------')
students_2 = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    for dict in some_list:
        if key_name in dict:
            print(dict[key_name])
        else:
            print("none")


iterateDictionary2("first_name", students_2)
iterateDictionary2("last_name", students_2)


print('Task 7  ---------------------------------------------------------------------------------')
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key.upper())
        for key_value in some_dict[key]:
            print(key_value)
        
    

print_info(dojo)