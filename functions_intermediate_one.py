x = [ [5,2,3], [10,8,9] ]
for nest_list in x:
    if nest_list[0] > 9:
        nest_list[0] = 15
        print(x)
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'] = ['Andres', 'Ronaldo', 'Rooney']
print(sports_directory)
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(some_list):
    for index in range(len(students)):
        print("first_name - " + some_list[index]['first_name'] + ", last_name - " + some_list[index]['last_name'])
iterateDictionary(students) 

def iterateDictionary2(string, list):
    for index in range(len(students)):
        print(list[index][string])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key in some_dict:
        print(str(len(some_dict[key])) + " " + key.upper())
        for index in range(len(some_dict[key])):
            print(some_dict[key][index])
        print("")
printInfo(dojo)