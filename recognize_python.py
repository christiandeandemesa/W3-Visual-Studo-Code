num1 = 42 # variable declaration, number
num2 = 2.3 # variable declaration, number
boolean = True # variable declaration, boolean
string = 'Hello World' # variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, list initalize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit)) # log statement, type check
print(pizza_toppings[1]) # log statement
pizza_toppings.append('Mushrooms')
print(person['name']) # log statement
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2]) # log statement

if num1 > 45: # if
    print("It's greater")
else: # else
    print("It's lower")

if len(string) < 5: # length check, if
    print("It's a short word!")
elif len(string) > 15: # length check, else if
    print("It's a long word!")
else: # else
    print("Just right!")

for x in range(5): # for loop
    print(x)
for x in range(2,5): # for loop
    print(x)
for x in range(2,10,3): # for loop
    print(x)
x = 0 # number
while(x < 5): # while loop
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person) # log statement
person.pop('eye_color')
print(person) # log statement

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': # if
        continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': # if
        break

def print_hello_ten_times(): # function
    for num in range(10): # for loop
        print('Hello') # log statement

print_hello_ten_times() # log statement

def print_hello_x_times(x): # function
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_times(4) # log statement

def print_hello_x_or_ten_times(x = 10): # function
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_or_ten_times() # log statement
print_hello_x_or_ten_times(4) # log statement


"""
Bonus section
"""

# print(num3) # NameError: name <variable name> is not defined
# num3 = 72 # Tuples
# fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean) # IndentatioError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has not attribute 'append'
# fruit.pop(1) # AttributeError: 'tuple' object has not attribute 'pop'