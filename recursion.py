# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# number=int(input("enter the number"))
# print(factorial(number))

                          
def fib(f):
    if f==0:
        return f
    else:
        return fib(f-1)+fib(f-2)

print(fib(6))