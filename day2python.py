# a = [[1,2],[1,2,3]]
# print(a)
#
# b = (1,2,3)
# print(b)
# print(a[0])
# print(b[0])
# b[0]=4

# d = {"key":{"key2":"bob"}}
# d['key3'] = 4
# print(d.get("key4",0))
# x=4
# if x>3:
#     print(x)
# elif x == 3:
#     print(x+1)
# else:
#     print(x-1)
# x=0
# while x<4:
#     print(x)
#     x+=1

def add(x,y):
    return x+y
#
# print(add(1,2))
# print(add(1.0,3.0))
# print(add("1",3.0))
# print(add("Hi ","bob"))
#
# b = "    a fun sentence for an example     "
# print(b.rstrip().lstrip() + "hello")

class Human:
    species="H. sapiens" #hopefully
    def __init__(self, name):
        self.name=name
        self.age=0
    def say(self,msg):
        return "{name}:{message}".format(name=self.name, message=msg)

class Student(Human):
    def __init__(self, name, year):
        Human.__init__(self,name)
        self.year = year

    def say(self,msg):
        return "{name}:{year}:{message}".format(name=self.name, year=self.year, message=msg)


H = Human("bob")
H2 = Student("Chris",2018)
print(H2.say("hello"))
