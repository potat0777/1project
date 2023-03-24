import random
a = random.randint(-1000,1000)
b = random.randint(-1000,1000)
c = random.randint(-1000,1000)
d = random.randint(-1000,1000)
rar = random.randint(-1000,1000)
print(a,b,c,d)
fir= a + rar
sec= b + rar
thi= c - rar
fot= d - rar
final = input("yes or no: ")
if final == "yes":
    print(fir,sec,thi,fot)
else:
    print("eror")