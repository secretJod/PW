# l1=[234,23423,34234,234,324234,543,5,43523,4,23,454,5,34,2,34,23,4,5,43,]
# for i in l1:
#         print(i*2,end="*",sep="/")
# write a program to print odd number in range of  n?
# def is_prime(num):
#     if num <= 1:
#         return False
#     elif num <= 3:
#         return True
#     elif num % 2 == 0 or num % 3 == 0:
#         return False
#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def print_primes(limit):
#     if limit < 2:
#         print("There are no prime numbers in this range.")
#         return
#     print("Prime numbers up to", limit, "are:")
#     for num in range(2, limit + 1):
#         if is_prime(num):
#             print(num, end=" ")

# if __name__ == "__main__":
#     try:
#         upper_limit = int(input("Enter an upper limit to find prime numbers up to: "))
#         print_primes(upper_limit)
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
# l1=['karan','devansh','rane','suraj']

# a=""#EMPTY STRING WHICH STORE THE ELEMENT OF LIST 
# for ele in l1:
#     if ele!='':
#         a+=ele +" " #USING EMPTY STRING TO CREATE A GAP BETWEEN ELEMENT OF STRING
           
# print(a)
# 5*4+3*2+1
# n=int(input("enter"))
# print(n,end=" ")
# for i in range(n-1,0,-1):
    
#     if i%2==0:
#         print("*",i,end=" ")
#     else:
#         print("+",i,end=" ")


# Stickler Thief
# MediumAccuracy: 37.98%Submissions: 180K+Points: 4
# Learn Google Cloud with Curated Lab Assignments. Register, Earn Rewards, Get noticed by experts at Google & Land your Dream Job! 
# Stickler the thief wants to loot money from a society having n houses in a single line. He is a weird person and follows a certain rule when looting the houses. According to the rule, he will never loot two consecutive houses. At the same time, he wants to maximize the amount he loots. The thief knows which house has what amount of money but is unable to come up with an optimal looting strategy. He asks for your help to find the maximum money he can get if he strictly follows the rule. ith house has a[i] amount of money present in it.
# Example 1:
# Input:
# n = 5
# a[] = {6,5,5,7,4}
# Output: 
# 15
# Explanation: 
# Maximum amount he can get by looting 1st, 3rd and 5th house. Which is 6+5+4=15.
# Example 2:
# Input:
# n = 3
# a[] = {1,5,3}
# Output: 
# 5
# Explanation: 
# Loot only 2nd house and get maximum amount of 5.
# Your Task:
# Complete the functionFindMaxSum() which takes an array arr[] and n as input which returns the maximum money he can get following the rules.
# Expected Time Complexity:O(N).
# Expected Space Complexity:O(N).
# Constraints:
# 1 ≤ n ≤ 105
# 1 ≤ a[i] ≤ 104
# n = 5
# a = [6,5,5,7,4]
# # Output: 15
# t=0
# k=0
# for i in a[0::2]:
#     t+=i
# for j in a[1::2]:
#     k+=j
# if k>t:
#     print("k",k)
# else:
#     print("t",t)
# s=[12,34,12,4,3,2]
# k=0
# t=0
# for i in s[1::2]:
#     k+=i
# for j in s[0::2]:
#     t+=j
# if k>t:
#     print(k)
# else:
#     print(t)



# def  add(*nums):
#     result=0
#     for number in nums:
#         result+=number
#     return result

# print("sum=",add(2,3,4,3,24))

# to=lambda n:"no. is even" if n%2==0 else "no. is odd"
# print(to(3))
# big=lambda l,k:"k is greater  "if k>l else "k is smaller"
# print(big(2,3))

# sum=lambda a,b,c:a+b+c
# print(sum(2,3,4))


# ranges= [
# {'name':'product','price':56},
# {'name':'product','price':30},
# {'name':'product','price':23},
# {'name':'product','price':79}
# ]

# sp=sorted(ranges,key=lambda x:x['price'])
# print(sp)

# y=lambda :print("hello karan")
# print(y())


# l=['java','python','html']
# e=enumerate(l)
# print(list(e))
# a=[x for x in range(5)]
# print(a)

# l5=[]
# for i in range(1,11):
#     l5.append(i)
# print(l5)
# a=[x*2 for x in l5]
# print(a)




# l1=[3,4,2,5,65,8,5,4,6,23,4]
# def odd(b):
#     l=[]
#     for i in b:
#         if i%2!=0:
#             l.append(i) 
#         return (l)
# print(odd(l1))


# print(sum([i for i in l1 if i%2!=0]))
# a=lambda b:sum([i for i in b if i%2!=0])
# print (a(l1))


# def e(l1):
#     try:
#         l=[]
#         for i in l1:
#             if i%2==0:
#                 l.append(i)

#         return l
#     except:
#         pass
#     return 2

# print(e("1"))

# # Q.vendor machine problem?

# money=20
# biscuit=3
# pepsi=5
# coke=6
# chips=9
# while money>=5:
#     your_choice=int(input("enter your choice(1.Biscuit,2,pepsi,3.coke,4.chips)"))
#     if your_choice==1:
#         if money>biscuit:
#             print("take your buiscuit")
#             money=money-biscuit
#         else:
#             print("insufficient balance")

#     elif your_choice==2:
#         if money>pepsi:
#             print("take your pepsi") 
#             money-=pepsi
#         else:
#             print("insufficient balance for pepsi")
#     elif your_choice==3:
#         if money>coke:
#             print("take your coke")
#             money-=coke
#         else:
#             print("insufficient balance for pepsi")
#     elif your_choice==4:
#         if money>chips:
#             print("take your chips")
#             money-=chips
#         else:
#             print("insufficient balance for chips")
# else:
#     print("you exausted your all money")




# Q.make a login code?
# user_id="karan@gmail"
# passw="secret"
# n=3
# while n>0:
#     n=n-1
#     if user_id==input("enter user id") and passw==input("enter password"):
#         print("you are logged in")
        
#     else:
#         print("plz enter valid")
# else:
#     print("you are logged out")

# class bankaccount :
#     def openaccount(self,email,name):
#         print("open acount by taking name and email")
#         return name+email
    
#     def deposit(self,amount):
#         print("trying to deposit the amount")
    
#     def withdraw(self,amt_with):
#         print("withdraw the amount")
    
#     def update_the_details(self,name_update,email_update):
#         print("this function upadate mail and name")

# bank=bankaccount()
# print(bank.openaccount("karan@","karan"))

# class oops:
#     def __init__(self,l):
#         self.l1=l
        

#     def extractfromindex(self,l,index):
#         return index
    
#     def extractrange(self,l,start,end):
#         return l[start,end]
    
#     def extracteven(self,l):
#         l1=[]
#         for i in l:
#             if i%2==0:
#                 l1.append(i)
#         return l1
    
    
# # f=oops()
# # print(f.extracteven(f.l4))

# se=oops([34,2,34,54,3,234,5,4,2])
# print(se.l1)



# class book():
#     def __init__(self,name,title,pageno):
#         self.nameofbook=name
#         self.titleofbook=title
#         self.pageno=pageno
    
    
#     def extracrdetails(self):
#         print(self.nameofbook,self.titleofbook)
    
#     def print_page_no(self):
#         print(self.pageno)


# karan=book('data','practicaldsa',456)
# dev=book("datasci",'phy',67)
# print(karan.extracrdetails())
# print(karan.print_page_no())



# class gmail():
#     def __init__(self,userid,password):
#         self.userid=userid
#         self.password=password
#         self.url="https://mail.google.com/mail/inbox"
#     def login(self):
#         print("take your userid"+self.userid+)



# userid="karan123@gmail.com"
# password="karan123"
# userid_check=False
# counter=1

# while counter<=3:
#     userid1=input("enter your user id")
#     if userid1==userid:
#         userid_check=True
#     else:
#         print("user id is incorrect")
#     if userid_check==True:
#         counter1=1
#         while counter1<=3:
#             paswd=input("enter your password")
#             if paswd==password:
#                 print("you logged in successfully")
#                 break
#             counter1+=1
#         if counter1>3:
#             print("you've reached max limit of password")
#             break
#     counter+=1
# if counter>3:
#     print("you have attempted maxmium number of times")


# user="karan123"
# paw="karan"
# counter=1
# useridcheck=False
# while counter<=3:
#     userid=input("enter your userid")
#     if userid==user:
#         useridcheck=True
#     else:
#         print("you enter wrong user id")
#     if useridcheck==True:
#         counter1=1
#         while counter1<=3:
#             pas=input("enter your pass")
#             if pas==paw:
#                 print("you are logged in succesfully")
#                 break
#             counter1+=1
#         if counter1>3:
#             print("you have reached max limit of pass")
#             break
#     counter+=1
# if counter>3:
#     print("chal nikal")

# my_list=[]
# end_of_list=""
# while end_of_list!="no":
#     end_of_list=input("enter yes or no :")
#     if end_of_list=="yes":
#         add_iteam=input("enter iteam to add:")
#         my_list.append(add_iteam)
#     else:
#         break

# print(my_list)

    
# def fib(n):
#     if n==0:
#         return n
#     if n==1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(4))


# def sum_digit(n): 
#     if n<=9:
#         return n
#     else:
#         return n%10+sum_digit(n//10)   

# print(sum_digit(123))



# nu=123
# 
# aus=0
# while nu!=0:
#     d=nu%10
#     aus=aus*10+d
#     nu=nu//10
    
# print(aus)
# # sum of all odd nu upto n using recursion?

# def p(a,b):
#     if b==1:
#         return a
#     else:
#         return a*p(a,b-1)
# a=2
# b=5
# print(p(a,b))



# def maxi(l,i):
#     if i==0:
#         return l[0]
#     return max(l[i],maxi(l,i-1))




# l=[2,4,1,5,8,5,6]
# n=len(l)
# print(maxi(l,n-1))   
      

# def rever(l):
#     if len(l)<=1:
#         return l
#     else:
#         return rever(l[1:]+l[0])
    

# def rev(n):
#     if n=="":
#         return 0
#     else:
#         return 1 +rev(n[1:])

# k="karan"
# print(rev(k))             




# def revstr(n):
#     if n=="":
#         return ""
#     else:
#         return revstr(n[1:])+n[0]

# print(revstr("brock"))



# def maxi(l,i):
#     if i==0:
#         return l[i]
#     else:
#         return max(l[i],maxi(l,i-1))

# l=[3,234,12,4,455,3]
# n=len(l)
# print(maxi(l,n-1))


# def findlen(n):
#     if n=="":
#         return 0
#     else:
#         return 1+findlen(n[1:])

# print(findlen("heydevansh"))

# def countchar(s,n):
#     if s=="":
#         return 0
#     elif s[0]==n:
#         return 1+countchar(s[1:],n)
#     else:
#         return countchar(s[1:],n)


# y="lorddevanshhail"
# print(countchar(y,"a"))




# def odd(n):
#     if n==0:
#         return 0
#     else:
#         return n+odd(n-1)


# n=int(input("enter the number"))
# print(odd(n))


###ITER###
# n=[234,435,234,234,234]
# l1=iter(n)
# print(next(l1))
# print(next(l1))
# print(next(l1))


# def fib(n):
#     a,b=0,1
#     for  i in range (n):
#         yield a
#         a,b=b,a+b
# for i in range(fib(9)):
#     print(i)



###OOPS????
class bankaccount:
    def open_acc(self,name,email_id):
        print("enter your name and email_id")
        return name+email_id
    def deposit(self,amt_deposite):
        print("enter a amount to deopsite")
        return amt_deposite
    def withdraw(self,amt_withdraw):
        print("enter amount to withdraw")
        return amt_withdraw
    def update_email(self,update_name,email_id):
        print("write a new name")
        return update_name+email_id

a='karan'
b="@gmail.com"
c=20
d="karan123"    
bankaccount=bankaccount()
open1=bankaccount.open_acc(a,b)
print(open1)

deposite=bankaccount.deposit(c)
print(deposite)

update=bankaccount.update_email(d,b)
print(update)


class book:
    def __init__(self,name,title,pageno):
        self.name_of_book=name
        self.title_of_book=title
        self.page_no_of_book=pageno
    def extract_bookname(self):
        print(self.name_of_book)
    def extract_title(self):
        print(self.title_of_book)
    def extract_pageno(self):
        print(self.page_no_of_book)

karan=book("dabbe","horror",345)
# devansh=book()
# rane=book()
print("karan is reading")
print(karan.extract_bookname())
print(karan.extract_title())
print(karan.extract_pageno())

harsh=book("incidious","horror",767):
print("rane is reading")
print(harsh.extract_bookname)
print(harsh.extract_title)
print(harsh.extract_pageno)
    