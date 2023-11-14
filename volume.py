# # # # # l=[1,34,5,5,6,7,]
# # # # # # print(type(l))
# # # # # # print(l[:2])
# # # # # l2=[1,3,5,6,4,46]

# # # # # new=l+l2
# # # # # print(new)
# # # # # a=list("karan")
# # # # # print(a)
# # # # # k=l.sort()
# # # # # print(k)

# # # # l="""the whole sum perophsajbduajsbduasbdubasuidbsuiduhasdnsadhn"""
# # # # s=l.split(',')
# # # # print(s)
# # # # l=[1,2,4,4,3,32,3]
# # # # a=l.pop()
# # # # l.insert(0,a)
# # # # print(l)

# # # def sum(a,b):
# # #     if a==1 and b==2:
# # #         return a+b
# # #     elif a>1 and b>1:
# # #         return a*b
    
# # #     elif a<10 and b<10:
# # #         return a/b
# # #     else:
# # #         a-b

# # # n=int(input("enter the number"))
# # # m=int(input("enter the number"))
# # # print(sum(n,m))

# # # Q.1 print the fabonacchi series upto nth terms?

# # # n=12   #assigning value 12 to  n or whatever you want to assign
# # # a,b=0,1  #taking a and b var and assigning value 0 and 1 to them
# # # nextterm=0   #taking nextterm as a varaible to get the next term of fab series intializing the nextterm by zero
# # # print("fab series:")
# # # for i in range(n+1):#looping till term n+1 to get the fab series upto nth value
# # #     print(a)  
# # #     nextterm=a+b
# # #     a=b
# # #     b=nextterm


# # sr="vasjdvasv djsadvhasfvdhv SADHJvasdv savdei oueiouto  euoo  aooeiroies"
# # vowel="aeiou"
# # count=0
# # for char in sr.lower():
# #     if char in     vowel:
# #         count+=1
# # print(count)
# # a=''.join(sr.split())
# # print(a)
# # print(sr.replace(" ",""))
# # print(sr.split())


# # you have been given a no. of stairs intially you are at zero stair and you need to 
# # reach the nth stair each time you can either climb one step or two step print the 
# # number of distinct ways in which you can climb from zero to n stair 
# # input=2 3 4 5 ,out=2,3,5 8
# # 0 1 1 2 3 5 8 13 21 34 55
# n=int(input("enter"))
# a,b=0,1
# nxt=0

# for i in range(n):
#     print(a)
    
#     nxt=a+b
    
#     a=b
#     b=nxt

# l=[1,24,352,324,234]
# max=0
# for a in l:
#     if a>max:
#         max=a
# print(max)


# l=[2 ,3 ,2 ,1 ,4]
# l2=[]
# def k():
#     for i in l:
#         if i%2==0:
#             l2.append(i)
#             return i


# b=lambda n:"even " if n%2==0 else "not even"
# print(b(4))

# str1=""
# password="karanshejal"
# while str1!=password:
#     str1=input("enter")
# if str1==password:
#     print("you guessed")

# budget=int(input("enter budget"))
# shirt=100
# shirt__size=['m','l','t']
# my_shirt__size='q'
# pant=200
# pant_size=['m','l','t']
# my_pant_size='l'
# jeans=300
# jeans_size=[12,20,35]
# my_jeans_size=35
# if budget>shirt:
#     print("let's try it ")
#     if my_shirt__size in shirt__size:
#         print("lets buy")
#     else:
#         print("mine size not available")
# else:
#     print("out of budget")        
# if budget>pant:
#     print("lets try pants")
#     if my_pant_size in pant_size:
#         print("is there more colour available")
#     else:
#         print("my size is not here")
# else:
#     print("out of my budget")
# if jeans<budget:
#     print("i want jeans")
#     if my_jeans_size in jeans_size:
#         print("give me that black one")
#     else:
#         print("no not avail")
# else:
#     print("out of budget")


# import time
# s=int(input("enter time"))
# Stop=int(input("enter break"))

# while s>0:
#     print(s)
#     time.sleep(1)
#     if s==Stop:
#         break
#     s-=1
# print("break de do sir")
    



# l=[]
# end="n"
# while end != "y":
#     t=input("enter")
#     l.append(t)
#     end=input("n  and y")
# print(l)

a=10
l=iter(a)
print(next(a))