class Solutionn():
    def sumOfMultiplies(self,n):
        sum=0
        for i in range(1,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                sum=sum+i
        return sum
                
        
c1=Solutionn()
print(c1.sumOfMultiplies(10))