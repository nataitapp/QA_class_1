__author__ = 'nata'
"""
1. Generate list 'l' with 30 random int elements in range from 0 to 99;
2. Compute the number of even ints in the given list 'l'; print the result."""

import random

randoms = range(100)
random.shuffle(randoms)
numbers = randoms[:31]

for number in numbers:
    if number % 2 == 0:
        # number.sort()  optional, if we want numbers to display nicely, we can also sort them.
        print number
 #=====================================================================================================
"""
1. Generate list 'l' with 30 random int elements in range from 0 to 99;
2. Compute the difference between the largest and smallest values in the list, without using min(), max()."""

import random

randoms =  range(100)
random.shuffle(randoms)
numbers = randoms[:31]
print numbers

count = 0
smallest = 0
largest = 0

for number in numbers:
    if smallest == 0 or number < smallest:
        smallest = number
    elif largest == 0 or number < smallest:
        largest = number
        difference = largest - smallest
print smallest, largest
print difference
#=======================================================================================================
"""
Return the number of times that the string 'qa' appears anywhere in the given string include upper case letters. For
example 'Qa' and 'QA' count.
String: 'fwerfgwfqawefwQafgeQfwefaqfeq' """


word = 'fwerfgwfqawefwQafgeQfwefaqfeq'
w = word.lower()
name = w.count('qa')
print name
#====================================================================================================
"""
1. Read about all new material. Look up for examples, play with it(3 hours);
2. Write a small program which will do the following(1.5 hour):
Generate list 'l' with 200 random elements from 0 to 99 each;
Take an input from user. Input should be a number from 0 to 99;
If user provides non-number print an error;
If user provides number less then 0 or bigger then 99 print an error;
3. Find all instances of that number in a list and print the amount and indexes of those instances. If nothing found - print it.
"""
import random

l = []
for r in range(200):
    l.append(random.randint(0,100))

while True:
    try:
         question = int(raw_input('enter a number:'))
         if question in range(100):
             number = l.count(question)
             indexes = ''
             for i in range(len(l)):
                if l[i] == question:
                    indexes = indexes + str(i) + ','
             if number == 0:
                print '--'
             else:
                indexes = indexes[:-1]
                print "Entered number appearce ", number, " times in the list at following index:", indexes, '.'
         elif question < 0 or question > 99 :
             print "number is out of range"
         break
    except ValueError:
             print "Error! Wrong entry."



