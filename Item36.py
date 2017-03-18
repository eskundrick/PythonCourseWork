# -*- coding: cp1252 -*-

#1. Assign an integer to a variable
effort = 100
print effort

#2. Assign a string to a variable
name = "The Motivator"
print name

str = "Hello Y'all"
print str

#3. Assign a float to a variable
myfloat = float(5)
print myfloat

#4. Use the print function and .format() notation to print out the variable you assigned
print 'Hi my name is {} I live on the {} floor'.format('Luca', '32nd')

#5. Use each of these operators +, - , * , / , +=, ­= , %
x = 10
print x  

y = 2
print y

# uses the += operator
a = 35 
a += 5
print a 

# uses the -= operator
b = 20 
b -= 5
print b

# uses the % operator
print 5.2 % 2


print (x-y) # uses the - operator
print (x+y) # uses the + operator
print (x*y) # uses the * operator
print (x/y) # uses the / operator

#6. Use of logical operators: and, or, not
if 3>5 and 3>6:
    print("condition not met")

#7. Use of conditional statements: if, elif, else
coffee = 15
tea = 12
water = 3

if coffee > tea:
    print "Lets drink coffee."
elif coffee < tea:
    print "Lets drink tea."
else:
    print "Water it is"

#8. Use of a while loop
FirstName=""
while FirstName != "Marco":
    FirstName = input("To proceed, please enter the name 'Marco':")
    if FirstName == 'Marco':
        print("Hello, my good friend Marco!")
    else:
        print("I'm sorry where's Marco?")

#9. Use of a for loop
for counter in range(0,11):
    print(counter)

#10. Create a list and iterate through that list using a for loop to print each item out on a new line
colorList = ["red","blue","white","pink"]    
for each in colorList:
    print(each)

#11. Create a tuple and iterate through it using a for loop to print each item out on a new line
animals = ('eagle','salmon','cougar','rattle-snake')
print("The third animal is: " +animals[2])

print("\nThe list of animals includes:")
for animal in animals:
    print("- " + animal)

#12. Define a function that returns a string variable
def thisFunction(exampleHere):
    "This is the function that has been defined"
    print exampleHere
    return


#13. Call the function you defined above and print the result to the shell
def thisFunction(exampleHere):
    "This is the function that has been defined"
    print exampleHere
    return;
thisFunction("Athen Able ought to tie his shoes")
thisFunction("Lest Athen trip and get the blues")
