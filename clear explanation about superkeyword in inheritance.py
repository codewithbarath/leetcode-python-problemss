class dog():
    def __init__(self,name):
        self.name=name

#the work of the sueprkeyword is to access the upper class value to lower class valuues so inam using the super() then
#here the upper class only consist the self value not prointing the value so i am access the upper class to lower class 
#note that the super keyword only used in the inheritance

class cat(dog):
    def __init__(self,name,spelling):
        super().__init__(name)
        self.name=name
        self.spelling=spelling
        print("the name is :",name)
        print("the spelling is :",spelling)
    
c1=cat("barber","babababba")




#another method  when you using only the __init__ means u can put the vlaues in object but when you call the def function you should put
#the value in the def calling area



class bubble():
    def speed(self):
        print("the speed is ishowspeed")

class ronaldo():
    def ron(self):
#this area calls the upper def function area you also print without putting super().speed()beacause the parent class connect with lowerclass
        super().speed()
        print("siuuuuuuuuuuuuuuuu")

c1=ronaldo()
c1.speed()


#another method
class A:
    def show(self):
        print("A class method")

class B(A):
    def show(self):
        print("B class method")
        super().show()

class C(B):
    def show(self):
        print("C class method")
        super().show()

c = C()
c.show()
