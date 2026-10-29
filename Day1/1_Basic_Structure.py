#comments
#import statement
#logics to be created

#import statements
import math

#defining a function to calculate the area of a circle
def area_of_circle(radius):
    area = math.pi * radius ** 2
    return area

#defining a main function
def main():

    #take user input and convert it to float 
    radius = float(input("Enter the radius of the circle: "))
    area = area_of_circle(radius)
    print(f"The area of the circle with radius {radius} is: {area}")

#calling the main function
#special build-in variable __name__ is used to check 
# if the script is being run directly or imported as a module
if __name__ == "__main__":
    main()
  