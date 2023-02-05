# variable
name = 'julie'
age = 10
sentence = f'Hi my name is {name} and i am {age} years old'
todayIsCold = False
year = 2010

# conditional statement
''' multilinecomment
if 2000 <= year < 2100:
    # singleLineComment
    print('Welcome to the 21st century!')
else:
    print('You are before or after the 21st century')
'''

# function
def hello(name='shawn', age=17):
    #print(f'hello {name} you are {age} years old')
    return f'hello {name} you are {age} years old'

# list

dognames = ['fido', 'sean', 'sally', 'mark']
'''
dognames.insert(1, 'jane')
print(dognames)
print(dognames[2]) #access specific item
del(dognames[2]) #delete list
print(dognames)
print(len(dognames))
dognames[1] = 'sean' #changes list item
print(dognames)
'''

# loops
'''
for dog in dognames:
    print(dog)

while age < 18:
    print(age)
    age += 1

numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]
for number in numbers:
    if number > 90:
        print(number)
'''

# dictionary
'''
dogs = {'fido':8, 'sally':17, 'sean':2}
dogs['fido'] = False;
print(dogs['fido'])

words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]

cooldictionary = {}
for i in range(0,3):
    cooldictionary[words[i]] = definitions[i]

print(cooldictionary)
'''

# classes
'''
class Dog:
    # method: func inside class

    def __init__(self, name, age, furColor):
        self.name = name
        self.age = age
        self.furColor = furColor

    dogInfo = 'Hey my dogs are cool'

    def bark(self, str): 
        print('gukguk! '+str)

mydog = Dog()
mydog.bark('shshsh')
mydog.name = 'fido' 
print(mydog.name)

mydog = Dog('fido', 17, 'red')
print(mydog.furColor)
'''

class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        return 2023 - self.year

mycar = Car(1998, 'good', 'toshiba')
print(mycar.age())