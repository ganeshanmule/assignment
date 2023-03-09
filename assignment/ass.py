'''score=int(input("enter nuber"))
name= str(input("enter your name"))
marks=[100,35.5,45,50,]
if score>100 or score<0:
    print("score is invalied")
elif score>50:
    print("you have passed")
else:
    print("you have failed")
for num in marks:
    print(num)'''
# import xmljson


'''x="jack"
for char in x:
    print(char)

number=int(input("enter number:"))

for count in range(1,20):
    product=number*count
    print(number,"*",count ,"=", product)'''

# num=[1,2,3,2,3,23,2,3,3]
'''xyz=["red","green","yello"]
#print(list(range(1,8)))
for i in range(0,3 ):
    print("i like",xyz[i])'''
'''student_name="asd"
student_name=str(input("enter name "))
marks={"ram":50,"anu":100,"ga":132}
for exam_marks in marks:
    if exam_marks == student_name
        print(marks[exam_marks])
        break
        else:
        print("name not found in list")'''
'''num=int(input("enter numbet:"))
num=5

i=0
while i<num:
    if i==2:
        i+=1
        continue
        print(i)
        i+=1
        print(num)'''
'''n=int(input("enter number"))
n=3
sum=0
i=5
while i<=n:
    sum=sum+i
    print("the sum is", sum)
    i=i+1

  if i <= 1:
      break

else:
    print("good by")'''

'''x,y=input("enter two values:").split()
print("x value:" ,x)
print("y value:",y)
if(x>y):
    print("is true")
else:
    print("is  false")'''

'''for val in "string":
    if val== "i":
        break
        print(val)'''
# print("end")


'''my_list=["hai",24,"hello",34]
print("lenth of the list",len(my_list))
#for x in my_list:
 #   for x2 in
  #  print(x)'''
'''user=str(input("enter your age:"))
string=" my age is "
print(string,+ user)'''

'''def greeting(name):
    print(name + "hello")



    greeting("nagesh")'''

'''import mymodule
mymodule.greeting("nagesh")'''

'''f=open("C:/Users/Nagesh/Desktop/sccl.xlsx", "r")
print(f.read())'''

'''count=0
while count <2:
    print("hai hello goodmorning:")
    count= count + 1
else:
    print("sorry for trouble:")'''

'''def getInteger(message):
    while True:
        try:
            userInt = int(input(message))
            return


        except ValueError:
            print('You must enter an integer')


getInteger('What is your age? ')
getInteger('How many players in the game? ')'''

'''def values():
    x="ram"
    y=20

    return [x,y]

    data=values()
    #print(data[3])
    print(type(values()))'''

# import statistics as st
# return st.


'''def val():
    g="ram"
    y=20
    return [g,y] #list
    data=val()
    print(data)
   # print(type(val()))'''

'''def dic1():
    dct=dict()
    dct["hai"]="hello"
    dct["ghgh"]="jjkk"
    dct[4]= 8
    return dct
    ghfh= dic1()
    print(ghfh)'''

# print("nahagah")

'''class car:
    wheel=4             #class attributs


    def __init__(self,color,style):            #instances attributes
        self.color=color                       #attributes  assign to variabels
        self.style=style

        def change_color(self,color):#method1
            self.color=color
                                       #create objects
        c=car("red",'benze')
        c.change_color("white")
        #creating new objct of class by calling the class name and pass the arguments

        #access attributes
        print(c.color)
        print(c.style)'''

'''class student:
   # name="jack"
   # age=16
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myclass(self):
        print("my name:",self.name)
        print("age is:",self.age)
        s=student("jack",20)
        print(s.name)
        print(s.age)

       s.myclass()'''

'''class dog:
    animal='dog'

    def __init__(self,breed,color):
        self.beard=breed
        self.color=color

        andro=dog("murre","white")
        print(andro.animal)
        print(dog.animal)'''

'''class complex:
    def __init__(self,real,image):
        self.real=real
        self.image=image
        #method
    def add(self,number):
        real=self.real + number.real
        image=self.image + number.image
        result=complex(real,imge)
        return result
        n1=complex(5,6)
        n2=complex(-4,3)
        result=n1.add(n2)
        print("real",result.real)
        print("image",result.image)'''

'''class cart:

    def __init__(self,apple,orange):
        self.apple= apple
        self.orange= orange
        def apple_check(self):
            if self.apple > 5:
                return "apples are good"
            else:

                return "apples are bad"

                def orange_check(self):

                    if self.orange > 10:
                        return "oranges are good"
                    else:
                        return "oranges are bad"
                        def main():
                            fruits=cart(11,3)
                            retutned_apple_meassage= fruits.apple_check()
                            retutned_orange_meassage= fruits.orange_check()
                            print(f"apple is {retutned_apple_meassage}")
                            print(f"orange is { retutned_orange_meassage}")
                            if __name__ == "__main__":
                                main()'''

'''class person:
    def __init__(self,name,id_number):
        self.name= name
        self.id_number= id_number

        def display(self):
            print(self.name)
            print(self.id_number)


class employee(person):
         def __init__(self,name,id_number,salary,post):
                    self.salary= salary
                    self.post= post
                    person.__init__(self,name,id_number)

                    a= employee("jack",8080,20000,"driver")
                    a.display()'''

# apartments = [
#     {        "location": "Seattle",
#              "price": 1200,
#              "size": 800,
#              "bedrooms": 1
#              },
#     {        "location": "San Francisco",
#              "price": 2500,
#              "size": 1000,
#              "bedrooms": 2
#              },
#     {        "location": "Los Angeles",
#              "price": 1500,
#              "size": 700,
#              "bedrooms": 1
#              },
#     {        "location": "New York",
#              "price": 3500,
#              "size": 1200,
#              "bedrooms": 3
#              }
# # ]
blocks = [
    {
        "gym": False,
        "school": True,
        "store": False,
    },
    {
        "gym": True,
        "school": False,
        "store": False,
    },
    {
        "gym": True,
        "school": True,
        "store": False,
    },
    {
        "gym": False,
        "school": True,
        "store": False,
    },
    {
        "gym": False,
        "school": True,
        "store": True,
    },
]


def appartmentHunting(blocks, reqs):
    maxDistance_Blocks = [float('-inf') for block in blocks]
    for i in range(len(blocks)):
        for req in reqs:
            closestReqDistance = float('inf')
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closestReqDistance = min(closestReqDistance, distanceBetween(i, j))
            maxDistance_Blocks[i] = max(maxDistance_Blocks[i], closestReqDistance)
    return getIndexAtMinValue(maxDistance_Blocks)


def distanceBetween(i, j):
    return abs(i - j)


def getIndexAtMinValue(array):
    idx_MinValue = 0
    minValue = float('inf')
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            idx_MinValue = i
            minValue = currentValue
    return idx_MinValue


reqs = ["gym", "school", "store"]

print(appartmentHunting(blocks, reqs))
#
# nums = [2, 0, 1, 2, 0, 3, 1, 4]
#
# new_list = []
# non_zeros = []
#
# for i in nums:
#     if i == 0:
#         new_list.append(i)
# for i in nums:
#     if i != 0:
#         non_zeros.append(i)
#
# print(non_zeros + new_list)

#
# class Solution:
#     def moveZeroes(self, nums: int):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#
#         z = 0
#
#         for i in range(len(nums)):
#
#             if nums[i] != 0:
#                 nums[i], nums[z] = nums[z],nums[i]
#                 z += 1
#         return nums
#


# nums = [2, 0, 1,2,1,0,0,2,0,234]
# obj = Solution()
# print(obj.moveZeroes(nums))
#
#
#
# L1 = [1,2,3,4,5]
# L2 = ['a','b','c','d','e']
# L3 = [1,2,3,4,5]
#
# zip_L1L2 = zip(L1,L2,L3)
# print(list(zip_L1L2))


# import re

# compile

# a = 'abc'
# print(type(a))

# re.compile('')
# print(type(re.compile(a)))
# print(a)


# print(type(a))
# print(re.compile(a))
# print(type(re.compile(a)))


# pattern = input("Enter the pattern :")
# string_obj = input("Enter the string :")
# for i in re.finditer(pattern, string_obj):
#     print(i.start(), '....', i.end()-1, '....', i.group())

# print(type(re.compile("abd")))

# a = input("Enter the string :")
# string_obj = input('Enter the string :')

# b= re.match(a, string_obj)
#
# if b == None:
#     print("Pattern is not matched at the begining of the string ")
# else:
#     print("Pattern is matched at the beginig of the string ")
#     print(b.start(), '....', b.end(), '....', b.group())
#
# a = input("Enter the string :")
# string_obj = input('Enter the string :')
#
# a = re.fullmatch(a, string_obj)
# if a == None:
#     print("Match is not available")
# else:
#     print("MAtch is available")
#     print(a.start(), '....', a.end(), '....', a.group())
#
# # Python program to convert uppercase to lowercase
#
# # take input
# string = input('Enter any string: ')
#
# # convert uppercase to lowercase
# new_string =''
# for i in range(len(string)):
#     if(string[i] >= 'A' and string[i] <= 'Z'):
#         new_string = new_string + chr((ord(string[i]) + 32))
#     else:
#         new_string = new_string + string[i]

# print lowercase string
# print('In Lower Case:',new_string)


# Python program to convert lowercase to uppercase

# take input
# string = input('Enter any string: ')
#
# # upper() function to convert lowercase to uppercase
# print('In Upper Case:', string.upper())


# import openpyxl
# from openpyxl import Workbook
# from pathlib import Path
#
# xlsx_file = Path('D:\python', 'SENGARENI SCL.xlsx')
# wb_obj = openpyxl.load_workbook(xlsx_file)
#
# # Read the active sheet:
# sheet = wb_obj.active


import random

print(random.randint(0, 10))

# def f(n):
#     if n==0 or n==1:
#         return 1
#
#     else:
#         return n*(f(n-1))
#
# n=int(input('enter number'))
# print(f(n))


a, b = "italic", "ITALIC"

print(a.title())
print(b.title())

s = 'aabssedf'
l = []
for i in s:
    if s.count(i) == 1:
        l.append(i)
print(''.join(l))

# import urllib.request
# import json
#
# def getResponse(url):
#     operUrl = urllib.request.urlopen(url)
#     if(operUrl.getcode()==200):
#         data = operUrl.read()
#         jsonData = json.loads(data)
#     else:
#         print("Error receiving data", operUrl.getcode())
#     return jsonData
#
# def main():
#
#     urlData = "https://icd.who.int/browse10/2019/en/JsonGetRootConcepts?useHtml=true"
#     jsonData = getResponse(urlData)
#     # print the state id and state name corresponding
#     # for i in jsonData["states"]:
#     #     print(f'State Name:  {i["state"]["state_name"]} , State ID : {i["state"]["state_id"]}')
#     #
#     for i in jsonData:
#        print(i)
#        #print(i[1])
#
#
# if __name__ == '__main__':
#     main()
#
#
# #import xmltodict
# import xmltojson
# import json
# import requests
#
#
#
# url='https://icd.who.int/browse10/2019/en#'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
#     (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
# }

# Sample URL to fetch the html page
# url = "https://geeksforgeeks-example.surge.sh"

# Headers to mimic the browser
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
#     (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
# }

# Get the page through get() method
# html_response = requests.get(url=url, headers=headers)

# Save the page content as sample.html
# with open("D:\python\mypython\sample.html", "w") as html_file:
#     html_file.write(html_response.text)


# with open("D:\python\mypython\sample.html", "r") as my_file:
#
#     html = my_file.read()
#     json_=xmltojson.parse(html)
#
#
# with open("D:\python\mypython\data.json", "w") as file:
#     json.dump(json_, file)
# print(json_)

#
#
#
# import urllib.request, json
# #
# # response = urllib.request.urlopen(url)
# # data = json.loads(response.read())
# # print (data)
#
#
# #
# # # import urllib library
# # from urllib.request import urlopen
# #
# # # import json
# # import json
# # # store the URL in url as
# # # parameter for urlopen
# # url='https://icd.who.int/browse10/2019/en#'
# #
# # # store the response of URL
# # response = urlopen(url)
# #
# # # storing the JSON response
# # # from url in data
# # data_json = json.loads(response.read())
# #
# # # print the json response
# # print(data_json)
#
#
# # import sys
# #
# # num = int(input('enter number'))
# # small = sys.maxsize
# # second_small = sys.maxsize
# #
# # while num > 0:
# #     remainder = num % 10
# #     if small >= remainder:
# #         second_small = small
# #         small = remainder
# #
# #     elif remainder <= second_small:
# #         second_small = remainder
# #     num = num // 10
# # # print(second_small)
# # import request
# #
# # myvar='http://example.com/blah/?myvar=123&myvar=567'
# # for var in request.get['myvar']:
# #     print(myvar)
#
#
# lst_years = [2003 , 2004 , 2007 , 2008 , 2020 , 2022]
#
# lst_leap_years = list(filter(lambda x: (x % 4 == 0) , lst_years))
#
# print(lst_leap_years)
#
#
# # def product(x,y):
# #     return x*y
# #
# #
# # l=[1,2,3]
# # res=reduce(product,l)
# # print(res)
#
#
#
# # import pandas as pd
# #
# # url="https://onedrive.live.com/edit.aspx?resid=93F65C9CD5C8445F!136&ithint=file%2cxlsx&authkey=!ANbBfZbd8lkpsv8"
# # c=pd.read_html(url)
# #
# # print(c)


import pandas as pd
import os
from datetime import datetime


def Transform(path1, path2):
    # read the CSV file from path1
    df = pd.read_csv(os.path.join(path1, 'F:\\pythonProject\\assignment\\file.csv'))
    print(df)

    # remove duplicates based on column1 and keep only the first occurrence
    df = df.drop_duplicates(subset=['Name'], keep='first')

    # sort by column2 in descending order
    df = df.sort_values(by=['Date'], ascending=False)

    # copy the row with the maximum date from column2 and change the date to today's date
    max_date = df['Date'].max()
    today_date = datetime.today().strftime('%d-%m-%Y')
    new_row = df[df['Date'] == max_date].iloc[0].copy()
    new_row['Date'] = today_date

    # append the new row to the dataframe
    df = df.append(new_row)

    # change the date format of the entire dataframe to dd-mm-yyyy
    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%d-%m-%Y')

    # write the dataframe to the CSV file in path2
    df.to_csv(os.path.join(path2, 'F:\\pythonProject\\assignment\\new.csv'), index=False)


Transform(path1='F:\\pythonProject\\assignment\\file.csv', path2='F:\\pythonProject\\assignment\\new.csv')
