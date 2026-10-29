#Data Structures in Python are used to store multiple values in a single variable
# and organize data in a way that allows for efficient access and manipulation. 
# Python provides several built-in data structures, including lists, tuples, sets, and dictionaries.
#Use case:
#Lists are useful when you need to maintain an ordered collection of items, 
  # such as a list of names or numbers.
#Sets are useful when you need to store unique items, 
# such as a collection of unique words     
#Tuples are useful when you need to store a 
 # fixed collection of items that should not be changed, such as the coordinates of a point in space.
#Dictionaries are useful when you need to store key-value pairs, 
 # such as a mapping of names to phone numbers or a mapping of product IDs to product details.

#list(ordered, mutable, allows duplicate values)
#whatever order will give value in that order, 
# we can change the value of list, 
# we can have duplicate values in list
#square brackets are used to define a list
#WHen data is more it grow in size, we can add more data to it, it is dynamic in nature
#When data is less it shrink in size, we can remove data from it, it is dynamic in nature
my_list = [1, 2, 3, None, 4, 5,2,1,None]
print(f"List: {my_list}")  # Output: List: [1, 2, 3, 4, 5,2,1,None]
my_list[0] = 10  # Change the first element of the list
print(f"Updated List: {my_list}")  # Output: Updated List: [10, 2, 3, 4, 5,2,1,None]


#tuple(ordered, immutable, allows duplicate values)
#ordered means the order of elements is maintained,
# we cannot change the value of tuple,
# we can have duplicate values in tuple
#parentheses are used to define a tuple
my_tuple = (1, 2, 3, 4, None, 5,2,1)
print(f"Tuple: {my_tuple}")  # Output: Tuple: (1, 2, 3, 4, None, 5,2,1)
#my_tuple[0] = 10  # This will raise an error because tuples are immutable


#set(unordered, mutable, no duplicate values)
#unordered means the order of elements is not guaranteed,
# we can change the value of set,
# we cannot have duplicate values in set
#  curly braces are used to define a set
my_set = {1, 2, 3, 4, 5,2,1,None,None}
print(f"Set: {my_set}")  # Output: Set: {1, 2, 3, 4, 5}

my_set.add(6)  # Add an element to the set
print(f"Updated Set: {my_set}")  # Output: Updated Set: {1, 2, 3, 4, 5, 6}



#dictionary(ordered, mutable, no duplicate keys)
#ordered means the order of elements is maintained,
# we can change the value of dictionary,
# we cannot have duplicate keys in dictionary, but values can be duplicated
#curly braces are used to define a dictionary
my_dict = {"name": "Alice", 
           "age": 30, 
           "city": "New York"
          }
print(f"Dictionary: {my_dict}")  # Output: Dictionary: {'name': 'Alice', 'age': 30, 'city': 'New York'}
my_dict["age"] = 31  # Change the value of a key in the dictionary
print(f"Updated Dictionary: {my_dict}")  # Output: Updated Dictionary: {'name': 'Alice', 'age': 31, 'city': 'New York'}
myd_dic=[{"name": "Alice", "age": 30, "city": "New York"},
          {"name": "Bob", "age": 25, "city": "Los Angeles"},
          {"name": "Charlie", "age": 35, "city": "Chicago"}]


#list - shopping list
#tuple - coordinates of a point
# set - unique words in a document
#dictionary - storing student records with name as key and age, grade, college as values