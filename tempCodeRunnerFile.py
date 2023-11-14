


class primecheck:
    def __init__(self,num):
        self.num=num
    def is_prime(self):
        if self.num<2:
            return False
        for i in range(2,int(self.num**0.5)+1):
            if self.num%i==0 :
                return False
        return True
class primeprint:
    def __init__(self,start,end):
        self.start=start 
        self.end=end
    def printprime(self):
        for num in range(self.start,self.end):
            primechecker=primecheck(num)
            if primechecker.is_prime():
                print(num)

start=3
end=45
result=primeprint(start,end)
print(result.printprime()) 