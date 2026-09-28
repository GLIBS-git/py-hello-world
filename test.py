#!/usr/bin/python3

import sys

print ("Text 1 " \
       "Text 2")


sys.exit()



s = ("Text 1"
     "Text 2")

print (s)


class Test:
    tv = "Test!"
    __tv2 = ""
    def print_1(self):
        print (self.tv)
    @property
    def tv2(self):
        return self.__tv2
    @tv2.setter
    def tv2(self, tv2):
        self.__tv2 = tv2
    @staticmethod
    def print_2():
        print (Test.tv)

t1 = Test()
t2 = Test()

t1.tv = "New test!" 

t1.print_1()
t2.print_1()

Test.tv = "Test 2!"

t1.print_1()
t2.print_1()

t2.tv = "New another test!" 

t1.tv2 = "Some test!"
t2.tv2 = "Another test!"

t1.print_1()
t2.print_1()

print (t1.tv2)
print (t2.tv2)

print (Test.tv)




def sum(a, b = 5):
    return a + b

print (sum (1, 2))
print (sum (1))


class TestClass:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
    def s(self):
        return self.__a + self.__b
    def sb(self):
        return self.__a - self.__b
    def m(self):
        return self.__a * self.__b
    def d(self):
        return self.__a / self.__b
    
print (TestClass(2, 3).s())
print (TestClass(2, 3).sb())
print (TestClass(2, 3).m())
print (TestClass(2, 3).d())

cl = TestClass(2, 3)

print ()
print (cl._TestClass__a)


print ()
print (cl.s())
print (cl.sb())
print (cl.m())
print (cl.d())

i = 0

def f1():
##    global i
    i = 1
    def f2():
        nonlocal i
        i = 2
        print ("F2: ", i)
        print ("F2 global: ", i)
    f2()
    print ("F1: ", i)
    print ("F2 global: ", i)
f1()
print ("F0: ", i)


for i in (1, 2, 3):
##    if i == 2:
##        break
    print ("I = ", i, i + 1, end = "\n\n")
else:
    print (-1)
print (0)    


##a = float("fdddds")

check = False
while check != True :
    ai = input ("Input A: ")
    try:
        a = float(ai)
        check = True
    except ValueError:
        print (f"Value {ai} is not a number!")


print ("Test 1", "Test 2", "Test 3");
print (1, 2, 3);

a = float(input("Введите значение a= "))
b = float(input("Введите значение b= "))
c = float(input("Введите значение c= "))

result = (a + b**3) / (1 + c**2);

print(f"Ответ: {result:.4f}");


print (round(11.11111, 2));
print ("2");

for i in range(5) :
    print (i);

print ();

for i in range(3, 8) :
    print (i);
    

print (range(3, 8));



if 0 :
    print ("a");
    print ("b");

print ("c");
print ("d");


m = {1:"One", 2:"Two", 3:"Three", 1:"Four"};
print (m);


m = {1:"One", 2:"Two", 3:"Three"};

l = {0, 1, 2, 3, 4, 5};

n = {};
n[0] = 1;

print (m[1]);
print (m);
print (n);

print (l);


i = 1;
j = 3;
f = 10.0;
l = 10,1;

#del i;

print (i/j);
print (f);
print (l);



print ("Привет, Python!");

print ("Hello world!");

counter = 100;
miles   = 1000.0;
name    = "Джон";

print (counter);
print (miles);
print (name);
