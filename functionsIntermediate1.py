# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

# x = [ [5,2,3], [10,8,9] ] 
# x[1][0] = 15
# print(x)

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]

# students[0]['last_name'] = 'Bryant'
# print(students)

# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# sports_directory['soccer'][0] = "Andres"
# print(sports_directory)

# z = [ {'x': 10, 'y': 20} ]
# z[0]['y'] = 30
# print(z)



# def iterateDictionary(some_list):
#     for i in some_list:
#         print(f'first_name -{i["first_name"]}, last_name-{i["last_name"]}')

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# # iterateDictionary(students) 
# # # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # # bonus to get them to appear exactly as below!)
# # first_name - Michael, last_name - Jordan
# # first_name - John, last_name - Rosales
# # first_name - Mark, last_name - Guillen
# # first_name - KB, last_name - Tonel


# def iterateDictionary2(key_name, some_list):
#     for i in some_list:
#         print(i[key_name])

# iterateDictionary2("first_name", students)
# iterateDictionary2("last_name", students)

def printInfo(some_dict):
    for i in some_dict:
        print(len(some_dict[i]), i.upper())
        for y in some_dict[i]:
            print(y)


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon