from math import sqrt

length = input("Please enter the length of the first side: ")
length2= input("Please enter the length of the second side: ")

print("Your hypotenuse is: " + str((sqrt(((float(length))**2) + ((float(length2))**2)))))







from statistics import mean
f=(input("Enter 3 numbers:"))


arr = [float(x) for x in f.split(' ')]

print(max(arr))
print(min(arr))
print(mean(arr))





row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

tot = (app_data_set [0][4]) + (app_data_set [1][4]) + (app_data_set [2][4]) + (app_data_set [3][4]) + (app_data_set [4][4])

avg_rating = tot/5




x=input("Insert a number: ")

greater = int(x) > 2
print( greater )
smaller = int(x) < 2
print(smaller)
equal = int(x) == 2
print(equal)




x=input("Insert a number: ")

if (int(x))%2 == 1:
    print("You chose an odd number")
else:
    print("You chose an even number")





score = input("Enter your score: ")
if int(score) >= 70.0:
    grade = ' First '
elif int(score) >= 60.0:
    grade = ' 2:1 '
elif int(score) >= 50.0:
    grade = ' 2:2 '
elif int(score) >= 40.0:
    grade = ' Third '
else:
    grade = ' Fail '







x = input("Supply a string: ")
count = 0
if ("a" in x) or ("A" in x):
    count += 1
if ("e" in x) or ("E" in x):
    count += 1
if ("i" in x) or ("I" in x):
    count += 1
if ("o" in x) or ("O" in x):
    count += 1
if ("u" in x) or ("U" in x):
    count += 1

if count == 0:
    print("There are no vowels")
if count == 1:
    print("There is one vowel")
else:
    print("The number of vowels is", count)





x = input("Supply a string: ")
count = 0
if ("a" in x) or ("A" in x):
    count += 1
    print("There are", (x.count("a" or "A")), "A")
if ("e" in x) or ("E" in x):
    count += 1
    print("There are", (x.count("e" or "E")), "E")
if ("i" in x) or ("I" in x):
    count += 1
    print("There are", (x.count("i" or "I")), "I")
if ("o" in x) or ("O" in x):
    count += 1
    print("There are", (x.count("o" or "A")), "O")
if ("u" in x) or ("U" in x):
    count += 1
    print("There are", (x.count("u" or "U")), "U")

if count == 0:
    print("There are no vowels")
if count == 1:
    print("There is one vowel")
else:
    print("The number of vowels is", count)




x = input("Supply a number: ")

if int(x) < 3:
    value = ("Small")
    if int(x)<2:
        value = ("Very small")
elif int(x) >3:
    value = ("Big")
    if int(x) >100:
        value= ("Very big")
else:
    value = ("The number is three")

print(value)





num = 1
while num <= 9:
    if num % 2 == 1:
        print( str(num) + "is odd")
    num += 2

print( "Done" )




#WHILE LOOP




from pcinput import getInteger
total = 0
count = 0
 while count < 5:
	total += getInteger( "Please give a number: " )
	count += 1
print( "Total is", total )








total = 0
count = 0
while count < 5:
    nome = "Enter value number" + " " + str(count) + ":"
    total += int(input( nome ))
    count += 1
average = total/5
print( "Total is", total )
print("Average is", average)





from pcinput import getInteger
number = 10

while number != 0:
    print(number)
    number -= 1
print("Blast Off!")




#FACTORIAL

from pcinput import getInteger

x = getInteger(" Insert a Value: ")
n = 1
while x != 0:
    n = n * x
    x -= 1
print(n)






total = 0
number = 1
for x in  range(1,6):
    sentence = "Give value of number: " + str(number)  + ": "
    number += 1
    value = int(input(sentence))
    total += value
print("Your total is", total)



#OR



from pcinput import getInteger

x = getInteger(" Insert a Value 1: ")
y = getInteger(" Insert a Value 2: ")
z = getInteger(" Insert a Value 3: ")

sum = 0
for number in (x,y,z):
    sum += number
print("Your total is: ", sum)








total = 0
number = int(input("select a number: "))
for x in  range(number, 0, -1):
    print(number)
    number -= 1
print("Blast off!")





#remember, continue takes back to while loop, so it cannot run i+= 1, so there is an endless loop

i = 0
while i < 10:
    if i == 3:
        continue   #here goes back up to while
    i += 1

print( grade )






sum = 0
for value in ( 12, 4, 3, 33, -2, -5, 6, 22, 4 ):
    if value == 0:
        print("Done")
        break
    if value < 0:
        continue
    sum += value
else:
    print(sum)








for i in range( 4 ):
    for j in range( 4 ):
        for z in range(4):
            print( "({} ,{}, {})".format( i, j, z) )





n = 1
while n > 0:
    n += 1
    if n % 12 != 0:
        continue
    if n % 15 != 0:             #MINIMO COMUNE MULTIPLO
        continue
    if n % 18 != 0:
        continue
    print(n)
    break



from pcinput import getInteger
x = getInteger( "Enter number 1: " )
y = getInteger( "Enter number 2: " )
z = getInteger( "Enter number 3: " )
n = 1
while n < int(z):
    n += 1
    if x % n != 0:
        continue
    if y % n != 0:          #MASSIMO COMUN DIVISORE(sbagliato)
        continue
    if z % n != 0:
        continue
    print(n)
    break






from pcinput import getInteger
from sys import exit
while True:                                    #it means that the loop is executed until the boolean evaluates to false
    x = getInteger( "Enter number 1: " )
    if x == 0:
        break
    y = getInteger( "Enter number 2: " )
    if y == 0:
        break
    if (x < 0 or x > 1000) or (y < 0 or y > 1000):
        print( "The numbers should be between 0 and 1000" )
        continue
    if x%y == 0 or y%x == 0:
        print( "Error: the numbers cannot be dividers" )
        exit()                                                    #means that the whole code is ended, not just the while loop (this is why print(goodbye) is not executed)
    print( "Multiplication of", x, "and", y, "gives", x * y )
print( "Goodbye!" )






from pcinput import getInteger
from sys import exit

while True:
    x = getInteger("Enter a number: ")
    if x < 0:
        print("You need to insert a positive number")
        continue
    print("The number is", x)
    break







from random import randint
TESTS = 10000
success = 0
for i in range( TESTS ):
    d1 = randint( 1, 6 )
    d2 = randint( 1, 6 )
    d3 = randint( 1, 6 )
    d4 = randint( 1, 6 )
    d5 = randint( 1, 6 )
    if d1 == 6 and d2 == 6 and d3 == 6 and d4 == 6 and d5 == 6:
        success += 1
print( "Chance at five sixes is", success / TESTS )




from random import randint
TESTS = 10000
success = 0
for i in range( TESTS ):
    for j in range( 5 ):
        if randint( 1, 6 ) != 6:
            break
        else:
            success += 1
print("Chance at five sixes is", success / TESTS)




#7.1



from pcinput import getInteger
x = getInteger( "Enter number 1: " )

for i in range (1,11):
    print("The multiplication of ", str(i), "by", str(x), "is", i * x)



#7.2


from pcinput import getInteger
x = getInteger( "Enter number 1: " )
value = 1
while value < 11 :
    print("The multiplication of ", value, "by", str(x), "is", value * x)
    value += 1



#7.3


from pcinput import getInteger
max_number = 0
min_number = 10000
divisor_three = []
divisor = 0
items = 0
while items < 3:
    x = getInteger( "Enter number: " )
    if x > max_number:
        max_number = x
    if x < min_number:
        min_number = x
    if x % 3 == 0:
        divisor = x
    divisor_three.append(divisor)
    items += 1
print(max_number)
print(min_number)
print(divisor_three)


#I put which are dividable by 3, not how many


max_number = 0
min_number = 10000

from pcinput import getInteger
TOTAL = 3
largest = 0
smallest = 0
div3 = 0
for i in range( TOTAL ):
    num = getInteger( "Please enter number "+str( i+1 )+": " )
    if num%3 == 0:
        div3 += 1
    if i == 0:
        smallest = num
        largest = num
        continue
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
print("Smallest is", smallest)
print("Largest is", largest)
print( "Dividable by 3 is", div3 )




#7.4



for i in range (10, -1, -1):
    if i != 1:
        print(str(i), "bottles of beer on the wall,", str(i), " bottles of beer. Take one down, pass it around,", str(i-1), "bottles of beer on the wall.")
    else:
        print(str(i), "bottle of beer on the wall,", str(i), " bottle of beer. Take one down, pass it around,", str(i - 1), "bottles of beer on the wall.")



# OR


bottles = 10
s = "s"
while bottles != "no":
    print( "{0} bottle{1} of beer on the wall , "\
        "{0} bottle{1} of beer.".format( bottles , s ) )
    bottles -= 1
    if bottles == 1:
        s = ""
    elif bottles == 0:
        s = "s"
        bottles = "no"
    print( "Take one down , pass it around , {} bottle{} "\
        "of beer on the wall.".format( bottles , s ) )






sequence = []
num1 = 0
num2 = 1
print ( "1")
while True:
    num3 = num1 + num2                #FIBONACCI
    if num3 > 100:
        break
    num1 = num2
    num2 = num3
    sequence.append(num3)
print(sequence)



#7.6





word1 = input("Please enter the first word: ")
word2 = input("Please enter the second: ")
doubles = ""
for letter in word1:
    if (letter in word2) and (letter not in doubles):
        doubles += letter
print(doubles)


#7.8

from random import randint
from pcinput import getInteger
tries = 0
value = randint(1,1000)
print(value)
while True:
    x = getInteger( "Enter a number: " )
    if x > value:
        print("Higher")
    if x < value:
        print("Lower")
    tries += 1
    if x == value:
        print("Correct, it took you", str(tries), "attempts")
        break





 continue
    if input(type) == "H":
        x = randint(1, x)
        print(x)
        attempts += 1
        continue
    if input(type) == "C":
        break
print("Correct after", str(attempts), "attempts")






from random import randint
x = randint(1, 100)
print(x)
lowest = 0
highest = 100
count = 1
while True:
    type = input("Enter the type: ")
    if type == "L":
        y = randint(x+1, 100)          #Works best with small ranges, as it does not narrow down the range as it goes
        print(y)
        count += 1
    elif type == "H":
        z = randint(1, x-1)
        print(z)
        count += 1
    elif type == "C":
        print("Correct")
        break
print("It took", str(count), "guesses" )




#7.9

from pcinput import getLetter
from sys import exit
count = 0
lowest = 0
highest = 1001
print( "Take a number in mind between 1 and 1000." )
while True:
    guess = int( (lowest + highest) / 2 )
    count += 1
    prompt = "I guess "+str( guess )+". Is your number"+\
        " (L)ower or (H)igher , or is this (C)orrect? "
    response = getLetter( prompt )
    if response == "C":
        break
    elif response == "L":
        highest = guess
    elif response =="H":
        lowest = guess
    else:
        print( "Please enter H, L, or C." )
        continue
    if lowest >= highest -1:
        print( "You must have made a mistake ,",
            "because you said that the answer is higher than",
                lowest , "but also lower than", highest )
        print( "I quit this game" )
        exit()
if count == 1:
    print( "I needed only one guess! I must be a mind reader." )
else:
    print( "I needed", count , "guesses." )




from random import randint
x = 50
print(x)
lowest = 0
highest = 100
count = 1
type = ""
while ("L" and "H") not in type:
    type = input("Enter the type: ")
    if type == "L":
        highest = x
        y = randint(lowest, highest)
        print(y)
        count += 1
    elif type == "H":
        lowest = x
        z = randint(lowest, highest)
        print(z)
        count += 1                                  #WRONG
    elif type == "C":
        print("Correct")
        break
while (highest - lowest) > 5:
    if type == "L":
        highest = x
        y = randint(x+1, 100)
        print(y)
        count += 1
    elif type == "H":
        lowest = x
        z = randint(1, x-1)
        print(z)
        count += 1
    elif type == "C":
        print("Correct")
        break



#7.10


from pcinput import getInteger
from sys import exit
x = getInteger( "Enter number 1: " )
divisor = x-1
prime = ""
if x == 1:
    print("The number is not prime")
    exit()
if x == 2:
    print("The number is prime")
    exit()
while divisor != 1:
    if int(x) % divisor != 0:
        divisor -= 1
    elif int(x) % divisor == 0:
        prime = "False"
        break
if prime == "False":
    print("The number is not prime")
if prime != "False":
    print("The number is prime")





Trials = 10000
die = 5
success = 0
for i in range(Trials):
    previous = 0
    for j in range(die):     #previous rebecomes 0 at the beginning of every dice roll
        x = randint(1, 6)
        if x < previous:
            break
        previous = x
    else:
        success += 1                          #Note that when a break statement is encountered, and the loop also has an else clause, the code block for the else will not be executed
print( "The probability of an increasing sequence",
"of five die rolls is {}".format( success/Trials ) )



coconuts = 10000
success = 0
while coconuts != 0:
    if coconuts % 5 != 1:
        break
    else: coconuts -= (coconuts / 5) + 1
    success += 1




PIRATES = 5
coconuts = 0
while True:
    coconuts += 1
    pile = coconuts
    for i in range( PIRATES ):
        if pile % PIRATES != 1:
            break
        pile = pile - ((pile -1)/5) - 1
    if pile % PIRATES == 1:
        break
print( coconuts )


ADDING A NEW COLUM FREE OR NOT TO A DATABASE CALLED APPS_DATA:

apps_data[0].append("free_or_not") 





83 
 74 
 67 
 68 
 80 
 47








from collections import Counter

text = input("please insert text: ")              #count repetitions
text_to_list = text.split()



print(Counter(text_to_list))






