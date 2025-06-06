"""  ## Function to greet a person

Write a function named `greet` that takes one argument, say `name`, and **returns** a greeting string. For example, `greet("Thomas")` should **return** the string:
```
Hello Thomas. How are you?"""
def greeting_function():
    name = input("What is your name: ")
    print("Hello",name,". How are you?")
#greeting_function()


"""## Greet a few friends

Create a simple list (not a dictionary) with the names of some friends. For example:
```python
my_friends = ["Frodo", "Sam", "Gandalf"]
```
Then write a function that takes the list of friends and **prints** a greeting for every one of them using function `greet(name)` from earlier.
"""

def Greet_Friends(name, greeting):
    print("Hello "+ name +",")
    print(greeting)
    print()

my_friends = {
    "Ryan": "Its nice to see you.",
    "Henry": "Its nice to see you.",
    "Roise": "Its nice to see you."
}

#for name, greeting in my_friends.items():
 #   Greet_Friends(name, greeting)


"""## Solve an equation

The quadratic equation is defined as $ax^2+bx+c=0$. When $b^2-4ac< 0$ the equation has no solutions among real numbers (and we don't want to deal with *complex numbers,* at least not yet. """
import math

def solve_quadratic():
    a = float(input("Give value for A: "))
    b = float(input("Give value for B: "))
    c = float(input("Give value for C: "))
    if b**2 - 4*a*c < 0:
     print("Equation has no solution")
    else:
        x_1 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        x_2 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        print("The first solution to this problem is:", x_1)
        print("The secound solution to this problem is:", x_2)

#solve_quadratic()






"""To run each program delete the "#" before the run commands for each function then replace "#" """