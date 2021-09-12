# Using single quote n midddle of string
course = "Python's course for Beginner"
print (course)
course = 'Python course for "Beginners"'
print (course)

 #For multiple lines you may use single three quotes / double three quotation marks

email = ''' 
Hi John,

This is our first email to you.

Thank you

'''
print(email)

email = """ 
Hi John,

This is our first email to you.

Thank you

"""
print(email)

#Accesssing index in String
course = 'Python for Beginners'
print(course[0])

# if we use negative index,  we can get characters from reverse direction
print(course[-1])
print(course[0:3]) # will return Pyt,  3 is not included
print(course[0:]) # will return all characters in the string
print(course[1:]) # will return all characters in the string starting from index 1 o/p will be ython for Beginners
print(course[:5]) # interpreter will assumer start index zero as starting value o/p will Pytho
print(course[:]) # here, interpreter will assume zero as start index and length of string as last index

another = course[:] # help us to create copy of already existed variable
print(another)

name = "Jennifer"
print(name[1:-1]) # output will be ennife excluding chac at index -1





