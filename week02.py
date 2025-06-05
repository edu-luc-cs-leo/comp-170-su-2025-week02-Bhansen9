
def greeting_function():
    name = input("What is your name: ")
    print("Hello",name,". How are you?")
#greeting_function()




def Greet_Friends(name, greeting):
    print("Hello "+ name +",")
    print(greeting)
    print()

my_friends = {
    "Ryan": "Its nice to see you.",
    "Henry": "Its nice to see you.",
    "Roise": "Its nice to see you."
}

for name, greeting in my_friends.items():
    Greet_Friends(name, greeting)
