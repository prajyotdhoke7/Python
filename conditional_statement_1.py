# if-else statements:
# Question 1: Write a Python program that checks if a given number is positive. If it is, print "Positive number"; otherwise, print "Negative number".
# Question 2: Write a Python program that checks if a given string is empty. If it is, print "Empty string"; otherwise, print "Non-empty string".
# Question 3: Write a Python program that checks if a given number is even. If it is, print "Even number"; otherwise, print "Odd number".
# Question 4: Write a Python program that checks if a given character is a vowel. If it is, print "Vowel"; otherwise, print "Consonant".
# Question 5: Write a Python program that checks if a given year is a leap year. If it is, print "Leap year"; otherwise, print "Not a leap year".
# Question 6: Write a Python program that checks if a given number is divisible by 3. If it is, print "Divisible by 3"; otherwise, print "Not divisible by 3".
# Question 7: Write a Python program that checks if a given string is a palindrome. If it is, print "Palindrome"; otherwise, print "Not a palindrome".
# Question 8: Write a Python program that checks if a given list is empty. If it is, print "Empty list"; otherwise, print "Non-empty list".
# Question 9: Write a Python program that checks if a given number is greater than, less than, or equal to 50. Print the corresponding message.
# Question 10: Write a Python program that checks if a given character is an uppercase letter. If it is, print "Uppercase"; otherwise, print "Lowercase".



# 1)
num=12
if (num>0):print("number postive")
else:print("number negative")

# 2)
str1="prayot"
if(len(str1)==0):
    print("string is empty")
else:
    print("string is not empty")

# 3)
num=10
if(num%2==0):
    print("number is even")
else:
    print("number is odd")

# 4)
char='a'
if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
    print("vowel")
else:
    print("Consonant")

# 5)
year=2001
if(year %400==0 ):
    print("Leap Year")
elif(year%100==0):
    print("Not Leap Year")
elif(year%4==0):
    print("Leap Year")
else:
    print("Not Leap Year")

# 6)
num=12
if(num%3==0):
    print("divisbile by 3")
else:
    print("not divisbile by 3")


# 7)
num=121
new_num=str(num)

print(new_num)
if(new_num[::-1]==new_num):
    print("palemdrome number")
else:
    print("not palemdrome number")


# 8)
list=[1,2,3,4,5,6,7,89,2]

if(len(list)==0):
    print("empty list")
else:
    print("not empty list")


# 9)
num=49

if(num>50):
    print("number is greater than 50")
else:
    if(num<50):
        print("number is less than 50")
    else:
        print("number is equal to 50")


# 10)
char ='A'

if(char==char.upper()):
    print("character in uppercase")
else:
    print("character in lowercase")