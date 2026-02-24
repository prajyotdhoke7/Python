# // if-elif-else statements:
# // Question 1: Write a Python program that checks if a given number is positive, negative, or zero. Print the corresponding message.
# // Question 2: Write a Python program that compares two numbers and prints the larger number.
# // Question 3: Write a Python program that determines whether a given temperature is hot, warm, or cold. Print the corresponding message.
# // Question 4: Write a Python program that checks if a given year is a leap year, a century year, or neither. Print the corresponding message.
# // Question 5: Write a Python program that categorizes a given character into uppercase letter, lowercase letter, digit, or special character. Print the corresponding message.
# // Question 6: Write a Python program that calculates the discount percentage based on the purchase amount. Print the corresponding discount percentage.
# // Question 7: Write a Python program that checks if a given number is divisible by 2, 3, 5, or none of them. Print the corresponding message.
# // Question 8: Write a Python program that determines the grade based on the percentage obtained. Print the corresponding grade.
# // Question 9: Write a Python program that checks if a given number is within a specific range. Print the corresponding message.
# // Question 10: Write a Python program that checks if a given string is an English word, a number, or a combination of both. Print the corresponding message.


# # 1)
# num=-0
# if(num>0):
#     print("positive number")
# elif(num<0):
#     print("negative number")
# else:
#     print("zero")

# # 2)

# num1=int(input("Enter number one"))
# num2=int(input("Enter number 2"))

# if(num1>num2):print(f"{num1} is greater than {num2}")
# elif(num1<num2):print(f"{num2} is greater than {num1}")
# else:print(f"{num2} is equal to {num1}")

# # 3)
# temp=int(input("Enter temp in C"))

# if(temp>25):
#     print("Hot")
# elif(temp<25):
#     print("Cold")
# else:
#     print("Normal")

# # 4)

# year=int(input("enter year"))
# if(year%400==0):
#     print("Leap Year")
# elif(year%100==0):
#     print("not Leap Year")
# elif(year%4==0):
#     print("Leap year")
# else:
#     print("not leap year")



# # 5)
# value=input("enter value")

# if(value.islower()):
#     print("is lower")
# elif(value.isupper()):
#     print("is upper")
# elif(value.isdigit()):
#     print("is digit")
# else:
#     print("is speacial character")


# 6)
amount=float(input("Enter amount"))
if(amount>500):
    print(f"10 % discount")
elif(amount>300):
    print(f"5 % discount")
else:
    print("Add more for discount")