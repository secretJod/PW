# #Q.1 find how many seconds are their in n minutes n seconds
# min=int(input("enter the number of minutes:"))
# sec=int(input("enter the number of seconds:"))
# total_seconds=(min*60)+sec
# print("total_seconds:",total_seconds)

# Q.2 find how many miles are their in n kilometers
# N=int(input("enter the number of kilometers:"))          #1km=0.621371 miles
# kilometer=0.621371
# miles=N*kilometer
# print("miles is equal to:",miles)

# Q.3 if you run 10kilometers race in 42 minutes 42 seconds what is your average time per mile in minutes and seconds.what is your average speed in miles per second what is your average speed miles perr hour
# no_of_minutes=42+(42/60)
# kilometer1=0.621371
# miles=10*kilometer1
# average_mile_min=miles/no_of_minutes
# print("the average miles are:",average_mile_min)
# # finding in hours
# distance=10*kilometer1
# no_of_hours=(42/60)+(42/3600)
# miles_hours=distance/no_of_hours
# print("average miles per hour:",miles_hours)

# Q.4 find the volume of sphere with radius n (volume=4/3 X pi X r3)
# import math
# r=int(input("enter radius:"))
# volume_sphere=4/3*math.pi*r**3
# print("volume_sphere:",volume_sphere)

#Q.5 cover price of book is $24.92 book store gets 40% discount shipping cost is $3 for 1st copy .find total 
# wholesale cost for 60 copies
# cover_price_dollar= 24.92
# discount_cover_price=40/100
# total_cover_price=cover_price_dollar*discount_cover_price
# shipping_cost=3
# shipping_discount=75/100
# total_shipping_cost=shipping_cost*shipping_discount
# whole_sale_cost_60_copies=60 * total_cover_price +  total_shipping_cost
# print("whole sale rate for 60 copies is:",whole_sale_cost_60_copies)

# Q.6 if i leave my house at 6:52am and run 1mile at an easy pace(8:15 per mile) then 3 mile at tempo
# (7:12 per mile) and 1 mile at easy pace again .what time do i get to home for breakfast?



# Q.7 print first 10 natural no. using while loop and for loop?
# i=1
# while i<=10:
#     print(i)
#     i+=1
# for n in range(1,11):
#     print(n)

# Q.8 print the pattern?
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#      print("*",end='')
#      j=j+1
# print( )
# i=i+1
# '''Q.9 write a program to accept the pecentage from the user and display the grade according to the following 
# criteria?
# grade   marks
# a        >=90 
# b        <90 and >=80
# c        <80 and >=60
# d        <60'''
# maths=int(input("enter the marks:"))
# chem =int(input("enter the marks:"))
# bio =int(input("enter the marks:"))
# phy=int(input("enter the marks:"))
# result=(maths+chem+bio+phy/400)%100
# if(result >=90):
#     print("you got grade 'A'congratulations")
# elif(result <90 and result >= 80):
#     print("you got  grade 'B' well done")
# elif(result < 80 and result >=60):
#     print("you got grade 'c'improve")
# else:
#     print("you are fail")


# # Q.10 write a program to accept the number from 1 to 7 and display the name of the days?
# N=int(input("enter any number between 1 to 7"))
# if(N==1):
#     print("today is sunday")
# elif(N==2):
#     print("today is monday")
# elif(N==3):
#     print("today is tuesday")
# elif(N==4):
#     print("today is wednesday")
# elif(N==5):
#     print("today is thusday")
# elif(N==6):
#     print("today is friday")
# else:
#     print("today is saturday")

# Q.11 write a program to check whether a number enter by the user is 3 digit number or not?
# num=input("enter any number ")
# l=len(num)
# if l!=3:
#     print("enter 3 digit number")
# else:
#     print("middle number :",int(num)%100//10)
# Q.12 write a program to check the number entered by user is positive or negative?
# a=int(input("enter any number:"))
# if(a>0):
#     print("the number is positive:")
# elif(a==0):
#     print("the number is neutral")
# else:
#     print("the number is negative")
# Q.13 write a program to know that the number input by the user is prime or not if prime then print "yes"
# if not prime print"not prime"
# number=int(input("enter the number to check whether it is prime or not:"))
# if number==1:
#     print("number is not prime")
# if number>1:
#     for i in range(2,n):
#         if n%i==0:
#             print("the number you entered is not a prime number")
#             break
#     else: 
#         print("the number you entered is prime")


# Q.14 print the table of number entered by the user?
# n=int(input("enter the number:"))
# for i in range(1,n):
#     for j in range(1,n):
#         print(i,"X",j,"=",i*j)
# write a python program to find those number whic are divisible and multiple of 5 between 1500 and 2700?
# for i in range(1500,2700+1):
#         print(i) 

# write a pythin program to covert  temperature to and from celsius and fahrenheit?
# formula=c/5=fi-32/9
# where c is temperature in celsius ad fi is temperature in fahrenheit?
# f=int(input("enter f:"))
# cel=((f-32)/9)*5
# print("your cel is:",cel)

# now converting f to c---
# c=int(input("enter c"))
# f=((c/5)+32)/9
# print(f)


# n = int(input("enter no."))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('* ',end="")
  

# write a program to find the maximum of 4 numbers?

# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=int(input("enter the number:"))
# d=int(input("enter the number:"))
# if (a>b) and (a>c) and (a>d):
#     print("a is bigger")
# elif(b>a)and(b>c)and(b>d):
#     print("b is bigger:")
# elif(c>a)and(c>b)and(c>d):
#     print("c is bigger")
# else:
#     print("d is bigger")

# def leap(year):
#     if(year == 0):
#         return
#     if(year % 4 == 0 ) and (year % 400 ==0 or year % 100 != 0 ):
#         print(year)
#     leap(year-1)
# leap(2023)    

# n=int(input("enter:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("* ",end=" ")
#     print()


# print fab series ?
# n=int(input("enter the number:"))
# a=0
# b=1
# for i in range(1,n):
#      print(a,end="")
#      next=a+b
#      a=b
#      b=next

# write a program to calculate the length of string using function?
# def string_length(str):
#     count=0
#     for char in str:
#         count+=1
#     return count
# print(string_length("uabsdiubjkd biub diuBKJDWBBD"))

# printthe pattern?
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(j,end=' ')
#     print()     

# calculate sum of all  number from 1 to a?
# a=int(input("enter the number:"))
# sum=0
# for i in range(a+1):
#      sum=sum+i
# print(sum)

# print the table of given 
# n=int(input("enter the number:"))
# for i in range(n+1):
#     for j in range(n):
#         print(i,"x",j,i*j)

# write a program to display only whose number ,the num which is div by 5 ,if it is greater 
# then150 then skip if number is greater the 500 then stop the loop?
# number=[12,75,150,180,145,525,50]
# for iteam in number:
#     if iteam>500:
#         break
#     elif iteam>150:
#         continue
#     elif iteam % 5==0:
#         print("iteam:",iteam)

# count the total number of digits in the number?
# num=74892348927483949
# count=0
# while num!=0:
#     num=num//10
#     count+=1
# print("total  number of digits are:",count)

# Q.write the program to display all prime numbers i range ?
# n=int(input("enter the number:"))
# primes=[]
# for num in range(2,n+1):
#     is_prime=True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         primes.append(num)
# print(primes)
# Q. Display fab series?
# n=int(input("enter the number:"))
# a,b=0,1
# count=0
# for i in range(n):
#     print(a,end=',')
#     count=a+b
#     a=b
#     b=count
# Q.fact?
# n=int(input("enter the number:"))
# factorial=1
# if n==1 or n==0:
#     print("no")
# else:
#     for i in range(1,n+1):
#         factorial=factorial*i
#     print(factorial)
# calculate the cube?
# n=int(input("enter the number:"))
# for i in range(n+1):
#     print(i**3)
# Q.sum sequence?
# n=int(input("enter the number:"))
# start=int(input("enter the number:"))
# sum_seq=0
# for i in range(n):
#     sum_seq+=start
#     start=start*10+2
# print(sum_seq)

# Q. print the prime numbers present in the list?\

# n=int(input("enter the number:"))
# list=[]
# for i in range(n):
#     element=int(input(""))
#     list.append(element)
# primes=[]
# for num in list:
#     is_prime=True
#     for j in range(2,num):
#         if num%j==0:
#             is_prime=False
#             break
#     if is_prime:
#         primes.append(num)
# print(primes)

# n=int(input("enter the number:"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
#     print("+",i,end='')
# print("=",sum)

# Q,print prime number in patterns?
# n=int(input("enter"))           
# num=2
# for i in range(n+1):
#     for j in range(i+1):
#         flag=1
#         for k in range(2,num):
#             if num%k==0:
#                 flag=0
#             break
#         if flag==1:
#             print(num,end=" ")
#         num+=1
#     print()

# Q.print the given square?
# n=int(input("enter:"))            
# sq=0
# for i in range(n+1):
#     sq+=i**2
#     print(i,end='^2 + ')
# print("=",sq,end='')
 


# swap first and last element of list
# def swaplist(newlist):
#     size=len(newlist)
#     temp=newlist[0]
#     newlist[0]=newlist[size-1]
#     newlist[size-1]=temp
#     return newlist
# n=int(input("enter"))
# l=[]
# for i in range(n+1):
#     e=int(input(""))
#     l.append(e)
# print(l)
# print(swaplist(l))

# n=int(input("enter:"))
# l=[]
# for i in range(n+1):
#     e=int(input(""))
#     l.append(e)
# print(l)
# a=len(l)
# for j in range(a-1,-1,-1):
#     print(l[j])

# print the following number series?
# n=int(input("enter:"))
# num=1
# prime=3
# print(1,end='')
# for i in range(2,n+1):
#     if num==1:
#         ch="+"
#         num+=1
#     elif num==2:
#         ch="-"
#         num+=1
#     elif num==3:
#         ch="*"
#         num+=1
#     else:
#         ch="/"
#         num=1
#     print(ch,prime,end='')
#     prime+=1
#     while(True):
#         flag=0
#         for k in range(2,prime):
#             if prime%k==0:
#                 flag=1
#                 break
#         if flag==0:
#             break
#         else:
#             prime+=1

# Q.check whether the number is pallindrome or not?
# n=int(input("enter:"))
# c=n
# sum=0
# while(n>0):
#     r=n%10
#     sum=r+(sum*10)
#     n=n//10
# if c==sum:
#     print("the number you entered is pallindrome")
# else:
#     print("chal nikal bahar")

# Q.check whether the string you entererd is palindrome or not?
# a=input("enter the string:")
# b=a[-1::-1]
# if b==a:
#     print("yes its is palindrome:",a)
# else:
#     print("no man try something else")

# Q.find the sum of first 5 number using recurssion?
# def sum(x):
#     if x==1:
#         return 1
#     else:
#         return x+sum(x-1)


# n=int(input("enter"))
# print (sum(n))

# Q. reverse the string using recursion?

# def re(x,y):
#     if y==0:
#         print(x[0])
#     else:
#         print(x[y],end="")
#         re(x,y-1)



# n=input("enter string")
# print(re(n,len(n)-1))

# find the square using Recursion?
# def po(x,y):
#     if y==0:
#         return 1
#     else:
#         return (x*po(x,y-1))



# x=int(input("enter"))
# y=int(input("enter"))
# z=po(x,y)
# print(z)


# 1. Declare two variables, `x` and `y`, and assign them integer values. Swap the
# values of these variables without using any temporary variable.
# a=int(input("enter the number")) 
# b=int(input("enter the number"))
# a=a+b
# b=a-b
# a=a-b
# print(a,b)


# # Q.find max of list?
# l=[]
# n=int(input('enter number'))
# for i in range(n):
#     e=int(input("enter element"))
#     l.append(e)
    
# max=0
# for x in l:
#     if x>max:
#         max=x
# print(max)

def sol(n):
    if n==0:
        return 
    
    
print(sol(5))





# Q.power using recursion?
# def power(a,b):
#     if b==0:
#         return 1
#     else:
#         return a*power(a,b-1)
    
# c=3
# d=4
# print(power(c,d))

# def absolute(n):
#     if n<0:
#         print(-n)
#     else:
#         print(n)

# print(absolute(-6))



my_budget=int(input("enter the amount"))
shirt_price=500
shirt_colour=['white','grey','purple']
colour_i_want='black'
pant_price=300
pant_colour=['white','light green','yellow']
colour_i_want_in_pant="yellow"
coat_price=800
coat_color=['neon','black']
colour_i_want_in_coat='red'
if my_budget>shirt_price:
    print("this is in my budget")
    if colour_i_want in shirt_colour:
        print("i am buying black shirt")
    else:
        print("plz bring black shirt soon")
else:
    print("not in my budget")
if my_budget>pant_price:
    print("i can buy a pant")
    if colour_i_want_in_pant in pant_colour:
        print("i would like to buy this panrt")
    else:
        print("why this colour pant is not available man")
else:
    print("pant bhi nahi kharid skta")
if my_budget>coat_price:
    print("coat is expensive but i want to buy it")
    if colour_i_want_in_coat in coat_color:
        print("this colour coat is fantastic and i am buying it")
    else:
        print("coat is expensive and the colour i wanted is also not available")
        
else:
    print("coat is out of my domain")




num=3
n=99
for i in range(2,num+1):
    if i %num:
        print("not")
        num+=1
    else:
        print(i)