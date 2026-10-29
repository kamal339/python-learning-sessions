#NOTE :Python automatically detects the type of variable based on the value assigned to it

#variables must start with a letter or an underscore
#Cannot contain spaces or special characters
#case sensitive name=Name is different from name=name
#variable should be descriptive and meaningful

name="John Doe"
age=30
salary=50000.50

#multiple assignment 
a, b, c = 10, 20, 30
#this will assign 10 to a, 20 to b and 30 to c

#same value for multiple variables
x = y = z = 100

#change the value of a variable
age = 31  # age is now updated to 31
age = 50  # age is now updated to 50
print(age)  # Output: 50



#type of variable can be checked using type() function
print(type(name))  # Output: <class 'str'>
print(type(age))   # Output: <class 'int'>
print(type(salary))  # Output: <class 'float'>


#student record example
student_name = "Alice"
student_age = 20
student_grade = "A" 
student_college = "XYZ University"

print(student_name, student_age, student_grade, student_college)  # Output: Alice 20 A XYZ University

print("Example of changing variable type:")
z = 10 # z is now an integer
print(z)  # Output: 10
print(type(z))  # Output: <class 'int'>
z= "Hello, World!"  # z is now a string 
print(z)  # Output: Hello, World!
print(type(z))  # Output: <class 'str'>