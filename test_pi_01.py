# Created : 2016.11.13#FFFFFF
# Python Learning Code

''' Begin Comment Block

ver_no = 0
greeting = "raspberry pi python:"
print(greeting.title())
print(greeting.upper())
print(greeting.lower())
long_message = greeting.title() + " \n" + greeting.upper() + " \n" + greeting.lower() + " \n"
print(long_message)
long_message = greeting.title() + " \t" + greeting.upper() + " \t" + greeting.lower() + " \t"
print(long_message)
print("Tabbed & Returned" + " -- =D\n\t")
long_message = "\t" + greeting.title() + " \n\t" + greeting.upper() + " \n\t" + greeting.lower() + " \n\t"
print(long_message)

#apostrophy test
message = "One of Python's strengths is its diverse community." 
print(message)

# message = 'One of Python's strengths is its diverse community.'  # this is should flag an error
# print(message)

#integers and floats birthday example
# age = 23 
# message = "Happy " + age + "rd Birthday!"  # this should flag a type error
# print(message)
age = 23 
message = "Happy " + str(age) + "rd Birthday!" # with string conversion function
print(message)

#integer and float operations 
#??? which will flag an error

print( 3/2 )
print( 3.0 / 2.0 )
print( 3.0 / 2 )
print( str(3/2 ))
print( str(3.0 / 2.0 ))
print( str(3.0 / 2 ))

# The Zen of Python
import this
print("\n")

# Lists
bicycles = ['huffy','trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[0].upper())
print(bicycles[1].upper())
print(bicycles[2].upper())
print(bicycles[-1].upper())
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
motorcycles[2] = 'BMW'
print(motorcycles)

# append() an item to a list @ last position
motorcycles.append('harley-davidson')
print(motorcycles)


motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# insert() an item in a list @ position in the list
motorcycles.insert(0, 'ducati')
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# pop() the last list item
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# remove list item
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'  # this could be a value passed from another process 
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.") # \A capitalizes the list items

# sorting a list -- permanently
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print("Sorted! >>>" + "\t"); print(cars) # multiple commands in a line via ; char

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(); print(cars); cars.sort(reverse=True); print(cars)

# sorting a list v-- temporarily
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# revrsing the list order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("There are "); print(len(cars)); print("cars in the list")

# access the last item in the list 
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1]) # <<< note a negative one index = last item

# the for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")

# for loop and numerical ranges
for value in range(1,5):
	print(value)
	
for value in range(1,6):
	print(value)

# even numbers list
even_numbers = list(range(2,11,2))
print(even_numbers)

even_numbers = list(range(2,1000,2))
print(even_numbers)

# list of squares
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

print("\nA more concise approach with the same result\n")
print("squares = []\nfor value in range(1,11):\n\t squares.append(value**2)\n")
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

# min and max values in a list 
print("\nMax & Minnie\n")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(digits)
print("Minnie:\t") ; print(str(min(digits)))
print("Max:\t") ; print(str(max(digits)))
print("The Sum:") ; print(sum(digits))

# list comprehension
squares = [value**2 for value in range(1,11)]
print("Comprehended List") ; print(squares)

# slicing lists
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])

# Loopping through a list
print("Here are the first three players on my team:")
for player in players[:3]:     
	print(player.title())

# copyimg a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:") 
print(friend_foods) 

# tuples 
dimensions = (200, 50)
print(dimensions[0]) ; print(dimensions[1])
for dimension in dimensions:
	print(dimension)

print("Original dimensions:")
for dimension in dimensions:
	print(dimension)	
dimensions = (400, 100)

# if statements
print("\nModified dimensions:")
for dimension in dimensions:
		print(dimension)

cars = ['audi', 'bmw', 'subaru', 'toyota'] 
for car in cars:
	if car == 'bmw':    # checking  for equality NOT equating a vaiable
		print(car.upper()) 
	else:     
		print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':     
	print("Hold the anchovies!")

# checking that a value is ot in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")

age = int(input("Your age, please?"))
#if age >= 18:
#	print("You are old enough to vote!")
	
# age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

# if-elif-else
age = int(input("Your age ?:  "))
# age = int(age)
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:     
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")
	
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age >= 65:    # eliminating the else-block
	price = 5
print("Your admission cost is $" + str(price) + ".")


# testing for multiple condtions
print("\n Makin a Pizza! \n")
requested_toppings = []
# asks = 0
for asks in range(0,3):
	asks = asks+1
	request=input("What would you like in it?:")
	requested_toppings.append(request)
	
	
# requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")
print("\nFinished making your pizza!")


# loop testing ???
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	requested_topping=input("What would you like in it?:")
	print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
print(requested_topping)



# DICTIONARIES

alien_0 = {'color': 'green', 'points': 5} 
print(alien_0['color']) 
print(alien_0['points'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# adding new keys to the dictionary
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25 
print(alien_0)



# Dynamically assembling a dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)


# Changing Key Values in a Dictionary

alien_0 = {'color': 'green'} 
print("The alien is " + alien_0['color'] + ".") 
alien_0['color'] = 'yellow' 
print("The alien is now " + alien_0['color'] + ".")


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast5'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# This must be a fast alien.
	x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# use the del statement to completely remove a key-value pair.Be aware that the deleted key-value pair is removed permanently.

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
5
# use a dictionary to store one kind of information about many objects

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

print("Sarah's favorite language is " +
	favorite_languages['sarah'].title() +
	".")

# looping through a dictionary

user_0 = {  'username': 'efermi', 
					'first': 'enrico',     
					'last': 'fermi',   }
					 
for k, v  in user_0.items(): 
		print("\nKey: " + k.title())     
		print("Value: " + v.title())



favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

for name in favorite_languages:		 # .keys():     
	print(name.title())
	
	
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print("  Hi " + name.title() +
		", I see your favorite language is " + 
		favorite_languages[name].title() + "!")
if 'erin' not in favorite_languages:     
		 print("Erin, please take our poll!")
for name in sorted(favorite_languages):
	print(name.title() + ", thank you for taking the poll.")
print("The following languages have been mentioned:")
for language in sorted(set(favorite_languages.values())):
	print(language.title())
''

# Nesting Dictionaries 


alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2] 
for alien in aliens:
       print(alien)


# Make 30 green aliens.

aliens=[]

for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# Show the first 5 aliens

for alien in aliens[:5]:
	print(alien)
	print("...")

# Show how many aliens have been created. 
print("Total number of aliens: " + str(len(aliens)))

for alien in aliens[0:3]:     
	if alien['color'] == 'green':         
		alien['color'] = 'yellow'         
		alien['speed'] = 'medium'   
		alien['points'] = 10

for alien in aliens[0:3]:     
	if alien['color'] == 'green':
		alien['color'] = 'yellow' 
		alien['speed'] = 'medium' 
		alien['points'] = 10     
	elif alien['color'] == 'yellow': 
		alien['color'] = 'red' 
		alien['speed'] = 'fast' 
		alien['points'] = 15

for alien in aliens[:5]:
	print(alien)
	print("...")


# user input + while loops
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
End Comment Block '''

height = input("How tall are you, in inches? ") 
height = int(height) 

if height >= 36:     	
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. 
# While loop follows
