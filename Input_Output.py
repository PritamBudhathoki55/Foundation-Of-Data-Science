# filename: Input_Output.py
# Topic name: Input_Output 
# Description: This program shows the tecnique to take input and output in python.
name = input("Enter your name: ") #Takes input
age = int(input("Enter your age: "))

print("Name:", name) #Gives output
print("Age:", age)

#Another method using f-string for Output(Best practice).
print(f"My name is {name} and I am {age} years old.")