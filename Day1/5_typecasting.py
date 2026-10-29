# Typecasting in Python
x = "25"
y=int(x)  # Convert string to integer
print(y)  # Output: 25
print(type(x))  # Output: <class 'str'>
print(type(y))  # Output: <class 'int'>

#string to float
x = "25.5"
y=float(x)  # Convert string to float
print(y)  # Output: 25.5 

#number to string
x = 25
y=str(x)  # Convert integer to string
print(y)  # Output: "25"



age= 11  #input("Enter your age: ")
age=int(age)  # Convert string input to integer
print(age)  # Output: integer value of the entered age
print(type(age))  # Output: <class 'int'>


#implicit/explicit typecasting, from smaller data type easily converted to larger data type

#implicit typecasting example
x = 10  # integer
y = 20.5  # float
z = x + y  # x is implicitly converted to float
print(z)  # Output: 30.5
print(type(z))  # Output: <class 'float'>

#explicit typecasting example
x="100"
y=int(x)  # Convert string to integer
print(y)  # Output: 100
print(type(y))  # Output: <class 'int'>