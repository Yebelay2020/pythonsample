# variable
## Assign valures
x=12
y=23
z=x+y
print(z)

## Assign valures
x, y, z = 23,25,45 # assign in one line or
x=23
y=25
z=45 
print(x+y+z)
# also we can use like
x=y=z=50 # if they have equal value
# 

Fname="Yebelay"
Lname="Berehan"
print(Fname+ " " +Lname) # " " used as space

# Dtata Type
x=12
y=12.5
z="Yebelay"
w=True
student=["Yebelay", "Belachew"]
print(type(student))  # to know data type
# cast or change one data type to other data type
a=float(x)
print(a)

# String

x=""" This is my first
python program 
practice
"""
print(x)
print(x[1:16])
print(x.find("my"))
print(x[-2])
print(len(x))
print(dir(x))
print(x.upper())
# to get help about str
""" 
print(help(str))
"""
x="Your name is {} and Your Age is {}"
print(x.format('Yebelay', 30))