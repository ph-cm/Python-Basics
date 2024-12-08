class Human:
    def __init__(self, age, name):
        #get acess to the age
        #_age stores the age
        self._age = age
        #get  acess to the name
        self._name = name
    
    def __str__(self):
        return "Name: " + self._name + " Age: " + str(self._age)
    
    def __repr__(self):
        return "Name: " + self._name + " Age: " + str(self._age)
        
    def older_younger_than(self, age):
        if(self._age > age):
            print("Our age is bigger than their age")
        elif self._age == age:
            print("Our age is equal")
        else:
            print("Our age is less than their age")   
             
h = Human(age=4, name='Pedro')

print(h)

print(h.__str__())

print(h.older_younger_than(5))
print(h.older_younger_than(4))
print(h.older_younger_than(3))