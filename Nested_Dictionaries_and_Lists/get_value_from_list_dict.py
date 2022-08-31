students = [
    {'first_name' : 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}]

def iterateDictionary1(lists):
    for i in range(len(students)):
        print(students[i][lists])


iterateDictionary1('first_name')
iterateDictionary1('last_name')