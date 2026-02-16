# Simple if statements:
# Question 1: Write a Python program that checks if a given number is even. If it is, print "Even number".
# Question 2: Write a Python program that checks if a given string contains the letter 'a'. If it does, print "String contains 'a'".
# Question 3: Write a Python program that checks if a given year is a leap year. If it is, print "Leap year".
# Question 4: Write a Python program that checks if a given number is positive. If it is, print "Positive number".
# Question 5: Write a Python program that checks if a given character is a vowel. If it is, print "Vowel".
# Question 6: Write a Python program that checks if a given number is greater than 100. If it is, print "Greater than 100".
# Question 7: Write a Python program that checks if a given string is empty. If it is, print "Empty string".
# Question 8: Write a Python program that checks if a given number is divisible by both 5 and 7. If it is, print "Divisible by 5 and 7".
# Question 9: Write a Python program that checks if a given list contains any negative numbers. If it does, print "List contains negative numbers".
# Question 10: Write a Python program that checks if a given word is a palindrome. If it is, print "Palindrome".

# 1)
num=12
if(num%2==0):
    print("Even Number")

# 2)
name="Prajyot"
num=name.count("a")
if(num>0):
    print("String contains \"a\"")

# 3)
year=2001
if(year %400==0 ):
    print("Leap Year")
elif(year%100==0):
    print("Not Leap Year")
elif(year%4==0):
    print("Leap Year")
else:
    print("Not Leap Year")

# 4)
num =10
if(num>0):
    print("Number is postive")
else:
    print("Negative number")

# 5)

char ='p'
if(char =='a' or char=='e' or char=='i' or char=='o' or char=='u' ):
    print("vowel")
else:
    print("not vowel")

