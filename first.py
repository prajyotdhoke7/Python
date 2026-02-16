# import requests

# response = requests.get('https://google.com')
# print(response.status_code)
# 
###############################################
"""
age = 10 
print(age)
age=12
print(age)

"""

#{
###############################################
#Number

# # integer
# age=10
# print(age)

# #floats
# sal=10.5
# print(sal)
# total=5+5
# print(total)
# }

###############################################
"""String"""

# my_long_text="""
# hello
# my name is 
# prajyot 
# dhoke
# """

# """o/p=
# hello
# my name is
# prajyot
# dhoke"""
# print(my_long_text)

# my_long_string="hello
# hsdbjh" error

# firstName="prajyot"
# lastName="dhoke"

# fullName=firstName +" "+ lastName
# print(fullName)

# long_dash="//"*10
# print(long_dash)
# o/p=////////////////////

# print(len(firstName)) // 7


################################################

"""Booleans"""

# is_logged_in=True
# print(is_logged_in) #True

# age=18
# can_vote=age>=18
# print(can_vote) #True

# age=16
# can_vote=age>=18
# print(can_vote) #False

# equal = 12==12
# print(equal)
 
################################################ 

"""Logical Operater"""

# Calculate: +, -, *, /
# Compare: >, <, ==
# Combine: and, or, not

# age =25
# has_license=True

# can_drive =age>= 16 and has_license
# print(can_drive) 

# age = 25
# can_play=age>=26 or age<=20

# print(can_play)

# can_drink=True
# print(not can_drink)

################################################ 

"""Assignment Shortcuts"""

# score=10

# score+=20
# print(score)
# score-=10
# print(score)
# score*=10
# print(score)
# score/=10
# print(score)

################################################ 

"""String Manipulation"""

# name="prajyot"

# index=f"Hey! Well-Come {name}"

# print(index) ##O/P=Hey! Well-Come prajyot
################################################ 

"""String method"""

# name="Prajyot"

# print(name.lower()) #prajyot
# print(name.upper()) #PRAJYOT

# Sentance="hi my name is prajyot"

# print(Sentance.title()) #Hi My Name Is Prajyot

""""
if you dont write "()" in print method after lower it will 
give you <built-in method lower of str object at 0x000001B32AFC1710>
"""

################################################ 

"""Conditional Statement"""

# temp =26

# if temp>25:
#     print("hot")

# temp1 =25

# if temp1>25:
#     print("hot")
# else:
#     print("cold")

# score=91

# if score>95:
#     print("A")
# elif score>90:
#     print("B")
#     print("hey")
# elif score>80:
#     print("C")
# else :
#     print("Fail")


# has_ticket=True
# age=15

# if has_ticket :
#     if age>=18:
#         print("Enjoy th moive")
#     else:
#         print("parents needed")
# else:
#     print("Buy ticket")


################################################ 

"""LOOPS"""

# for i in range(5):
#     print("hello")


# for i in range(5):  
#     print(i)

# for i in range(2  ,6):
#     print(i)

# for i in range(0,10,4):
#     print(i)

# name="Prajyot"
# for alpa in name:
#     print(alpa)

# colors=["red","blue","green","white","pink"]
# for color in colors:
#     print(f"I like {color}")

# count=0
# while count<5:
#     print(count)
#     count=count+1

################################################ 

"""DATA STRCUTURE"""

#1)Lists:Ordered,Chnageable Collections
#2)Dictionaries:Key value pairs
#3)Tuples: ordered Unchangeable
#4)Sets:Unique values only

################################################ 

"""LISTS"""

my_lists=[] #empty list decl
fruits=["apple","banana","orange"] # String List
number=[1,2,3,4,5] #interger List
mixed=["hello",1,True,3.14] # mixed List

print(fruits[0]) #apple
print(number[0])#1
print(mixed[0])#hello
print(fruits[0:3])#['apple', 'banana', 'orange']
print(fruits[1:])#['banana', 'orange']


#####ADD in to list##### 
my_lists.append("peru")
my_lists.append("12")
my_lists.append("as")

print(my_lists)
#####remove from the list#######
# my_lists.remove("12")
# print(my_lists)

# #######insert in the list#####

# my_lists.insert(2,1223)
# print(my_lists)

# #######pop the element#####

# my_lists.pop()
# print(my_lists)

# ###### remove by the index#####

# del my_lists[0]
# print(my_lists)


#######Length of list########

listLen=len(my_lists)
print(listLen)


#######find number in element  the list########

count=my_lists.count("as")
print(count)

#######find index of elemet###########

pos=my_lists.index("12")
print(pos)

#############sort the list###########
new_list=[2,4,6,2,58,2,5,4,3,25,85]

list2=new_list.sort
print(list2)




