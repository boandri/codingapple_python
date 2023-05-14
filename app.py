# name = 'hihi'
# print(name[0:2])
# print(123)
# print(name[1:2])
# #print(name * 100)
# print("whoami")
stock = ['K5', 'BMW', 'Tico']

if 'BMW' in stock  :
    print("can order now")
else :
    print("Not available at the moment")



for i in stock :
    print(i)



def fly() :
    print("hi my name is beautiful fly")


car = ['k5', 'white', 5000]
car2 = {
    'brand' : 'BMW', 
    'model' : '520d'
    }
print(car)
print(car2['brand'])
car[1] = 'black'
print(car)
car.pop()
print(car)

fly()

def magicHat(i) :
    print(i)

magicHat(13321)


def function():
    return 10

print(function())