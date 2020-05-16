
"""
Hands On

# Initialize `fahrenheit` dictionary 
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

1 Get the corresponding `celsius` values in list

2 Create the `celsius` dictionary

3 convert a dictionary of Fahrenheit temperatures into celsius

"""


"""
Code Challenge
  Filename: 
    map1.py
  Problem Statement:
import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

for i in range(len(names)):
    names[i] = random.choice(code_names)

print (names)

As you can see, this algorithm can potentially assign the same secret code name 
to multiple secret agents. 

Rewrite the above code using map and lambda.

"""


"""
Code Challenge
  Filename: 
    map2.py
  Problem Statement:

names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print (names)


(Hopefully, the secret agents will have good memories and won’t forget each 
other’s secret code names during the secret mission.)


Rewrite the above code using map.

"""



"""
Code Challenge
  Filename: 
    height.py
  Problem Statement:

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

    if height_count > 0:
        average_height = height_total / height_count

print (average_height)
    
Try rewriting the code below using map, reduce and filter. 
Filter takes a function and a collection. 
It returns a collection of every item for which the function returned True.
    

"""



"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number    Book Title              Author      Quantity    Price per Item
    34587           Learning Python         Mark Lutz   4           40.95
    98762           Programming Python      Mark Lutz   5           56.80
    77226           Head First Python       Paul Barry  3           32.95
    88112           Einführung in Python3   Bernd Klein 3           24.99    
    
    
    Write a Python program, 
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 

    Output:
    [('34587', 163.8), ('98762', 284.0), ('77226', 98.85), ('88112', 74.97)]
    
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.
    
    Output:
    [('34587', 163.8), ('98762', 284.0), ('77226', 108.85), ('88112', 84.97)]
    

# Step 1  Solve the problem using for loop

# Step 2  Refactor your Code  - remove the loop and use map and lambda

# Step 3  Refactor your Code  - use the concept of chaining  PYTHONIC CODE


  
  Hint: 
    Write a Python program using lambda and map.
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
      ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
      ["77226", "Head First Python, Paul Barry", 3,32.95],
      ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
    ]

"""