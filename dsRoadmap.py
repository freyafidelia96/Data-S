import math
"""birthYear = 2002
currentYear = 2023
print("Age: ", currentYear - birthYear)"""

"""firstName = "Fidelia"
middleName = " Oreoluwa"
lastName = " Achi"

print(firstName + middleName + lastName)"""

"""length = 92
width = 48.8
area = length * width
print(area)"""

"""noOfPackets = 9
pricePerPacket = 1.49
totalCost = noOfPackets * pricePerPacket
moneyGiven = 20
moneyLeft = moneyGiven - totalCost
print(moneyLeft)"""

"""length = 5.5
areaOfSquare = length ** 2
tilesCost = 500
totalCost = areaOfSquare * tilesCost
print(totalCost)"""

"""num = 17
print("The binary equivalent of " + str(num) + " is", format(num, 'b'))"""

"""street = "14, olaoluwa, Egan"
city = "Lagos"
country = "Nigeria"

address = street + '\n' + city + '\n' + country
print(address)
address1 = f'{street}\n{city}\n{country}'
print(address1)"""

"""store = "Earth revolves round the sun"
print(store[6:14])
print(store[-3:])
"""

"""numOfVeggies = 3
numOfFruits = 6

print(f"I eat {numOfVeggies} veggies and {numOfFruits} fruits daily")

s = "Maine 200 banana khaye"
s = s.replace('banana', 'samosa').replace('200', '10')
print(s)"""

"""monthlyExpenses = [2200, 2350, 2600, 2130, 2190]
print("Dollars spent in Feb compared to Jan is ", monthlyExpenses[1] - monthlyExpenses[0], "$")
print("Total expenses in first quarter is", monthlyExpenses[0] + monthlyExpenses[1] + monthlyExpenses[2], "$")
print("is 2000$ in monthly expenses: ", 2000 in monthlyExpenses)
monthlyExpenses.append(1980)
print(monthlyExpenses)
monthlyExpenses[3] = monthlyExpenses[3] - 200
print(monthlyExpenses)

heros = ['spider-man', 'thor', 'hulk', 'iron man', 'captain america']
print("Length of list heros: ", len(heros))
heros.append('black panther')
print(heros)
del heros[-1]
heros.insert(3, 'black panther')
print(heros)
heros[1:3] = ['doctor strange']
print(heros)
heros.sort()
print(heros)"""

india = ['mubai', 'banglore', 'chennai', 'delhi']
pakistan = ['lahore', 'karachi', 'islamabad']
bangladesh = ['dhaka', 'khulna', 'rangpur']

"""cityName = input("Enter a city name: ")

if cityName.lower() in india:
    print(str(cityName) + " is in India")
elif cityName.lower() in pakistan:
    print(str(cityName) + " is in Pakistan")
elif cityName.lower() in bangladesh:
    print(str(cityName) + " is in bangladesh")
else:
    print("Not in database")
"""
"""x = input("Enter two city names: ")
y = input()

if x  in india and y in india:
    print(str(x) + " and " + str(y) + " are both in India")
elif x  in pakistan and y in pakistan:
    print(str(x) + " and " + str(y) + " are both in Pakistan")
elif x  in bangladesh and y in bangladesh:
    print(str(x) + " and " + str(y) + " are both in Bangladesh")
else:
    print(str(x) + " and " + str(y) + " don't belong to same Country" )
"""
"""
sugarLevel = eval(input("Enter sugar level: "))

if sugarLevel < 80:
    print("Sugar level is low")
elif sugarLevel > 100:
    print("Sugar level is high")
else:
    print("Sugar level is normal")"""

"""result = ["heads", "tails", "tails", "heads", "tails","heads", "heads", "tails","tails"]
count = 0

for heads in result:
    if heads == "heads":
        count = count + 1
print("Number of heads is: ", count)

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i * i)

expenseList = [2340, 2500, 2100, 3100, 2980]
expAmount = eval(input("Enter an expense amount: "))

for i in range(len(expenseList)):
    if expAmount == expenseList[i]:
        print("Month is: ", i + 1, "for expense: ", expenseList[i])
    elif i == len(expenseList) - 1 and expAmount != expenseList[i]:
        print("Not found in expense list")"""


"""for i in range(1, 6):
    print("You have completed ", i, "km")
    j = input("Are you tired (yes or no)?: ")
    if j == "yes":
        print("You didn't finish the race")
        break
    elif j == "no":
        if i == 5:
            print("Congratulations you've finished the race!")
        continue

for i in range(1, 6):
    print("*" * i)    """

"""def areaTriangle(base, height):
    area = 0.5 * base * height
    return area

n = areaTriangle(4, 16)
print(n)

def findArea(base, height, shape="triangle"):
    if shape == "rectangle":
        area = base * height
    else:
        area = 0.5 * base * height
    return area

def printPattern(n):
    for i in range(1, n + 1):
        print("*" * i)

x = findArea(7, 4)
print(x)

printPattern(6)"""

"""population = {"china": 143, "india": 136, "USA": 32, "pakistan": 21}

def printPopulation():
    for k, v in population.items():
        print(k, "==>", v)

def add():
    y = input("Enter country to add: ")
    if y in population:
        print("Country already exists.")
    else:
        population[y] = eval(input("Enter population parameter: "))
        printPopulation()

def remove():
    z = input("Enter country to remove: ")
    if z in population:
        del population[z]
        printPopulation()
    else:
        print("Country does not exist")

def query():
    y = input("Enter country to query: ")
    if y in population:
        print(y, "==>", population[y])
    else:
        print("Country does not exist")

x = input("Enter any of these (print, add, remove, query): ")

if x == "print":
    printPopulation()
elif x == "add":
    add()
elif x == "remove":
    remove()
elif x == "query":
    query()
else:
    print("Invalid input!")"""

"""stocks = {"info": [600, 630, 620], "ril": [1430, 1490, 1567], "mtl": [234, 180, 160]}

def printStocks():
    total = 0
    for k, v in stocks.items():
        for i in range(len(v)):
            total = total + v[i]
        avg = round((total) / len(v), 2)
        print(k, "==>", v, "==> avg:", avg)
        total = 0

def addStocks():
    x = input("Enter stock ticker: ")
    y = eval(input("Enter price: "))

    if x in stocks:
        stocks[x].append(y)
        printStocks()
    else:
        stocks[x] = [y]
        ask = input("Do you want to add more prices to stock (yes or no)?: ")
        while ask == "yes":
            y = eval(input("Enter price: "))
            stocks[x].append(y)
            ask = input("Do you want to add more prices to stock (yes or no)?: ")
        printStocks()


x = input("Enter one of these (print, add): ")

if x == "print":
    printStocks()
elif x == "add":
    addStocks()
else:
    print("Invalid input!")"""

"""def circleCalc(r = 0):
    area = round(math.pi * pow(r, 2), 2)
    circumference = round(2 * math.pi * r, 2)
    diameter = round( 2 * r, 2)
    return diameter, circumference, area

x, y, z = circleCalc(4)

print("Diameter:", x, "\nCircumference:", y, "\narea:", z)
"""

"""word_stats={}

with open("c:\\Data\\poem.txt", "r") as f:
    for line in f:
      words=line.split(' ')
      for word in words:
        if word in word_stats:
          word_stats[word]+=1
        else:
          word_stats[word] = 1

print(word_stats)

word_occurances = list(word_stats.values())
max_count = max(word_occurances)
print("Max occurances of any word is:",max_count)

print("Words with max occurances are: ")
for word, count in word_stats.items():
    if count==max_count:
        print(word)

"""

"""class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


    def display(self):
        print(f"ID: {self.id} \nName: {self.name} ")

employee = Employee(1, "caller")
employee.display()

del employee.id

try:
    employee.display()
except Exception as e:
    print(f"Exception:", e)

del employee

try:
    employee.display()
except Exception as e:
    print(f"Exception:", e)
"""
"""
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    
    def teach(self):
        print(f"I teach {self.subject}")

class Youtuber:
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain

    def uploadVideo(self):
        print(f"I'm uploading a video on {self.domain}!")
    

class Student(Teacher, Youtuber):
    def __init__(self, name, subject, domain):
        super().__init__(name, subject)
        self.domain = domain


s = Student("ore", "maths", 'lifestyle')
s.teach()
s.uploadVideo()"""

"""class AdultException(Exception):
    def printException(self):
        print("Custom adult Exception")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getMinorAge(self):
        if self.age > 18:
            print("He is major")
        else:
            try:
                raise AdultException
            except AdultException as e:
                e.printException()
    
    def displayPerson(self):
        print(f"Name: {self.name} \nAge: {self.age} ")


p = Person("ore", 17)
p.getMinorAge()
p.displayPerson()
"""

"""class FibonacciSequence:
    def __init__(self, limit):
        self.limit = limit
        self.n = 0
        self.a = 0
        self.b = 1
    
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.n < self.limit:
            if self.n == 0:
                print(self.a)
                self.n += 1
            self.a, self.b = self.b, self.a + self.b
            self.n += 1
            return self.a
        else:
            raise StopIteration
        
f = FibonacciSequence(10)

while True:
    try:
        print(next(f))
    except StopIteration:
        break

"""
"""
def squareSequence():
    i = 1
    while True:
        yield i * i
        i += 1

for i in squareSequence():
    if i > 25:
        break
    print(i, end=' ')"""

integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]

z = zip(integer, binary)

binaryDict = {integer:binary for integer, binary in z}
print(binaryDict)

integer1 = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [-1, 1, -2, -3, -5, 0, 7]

print(integer1 + additive_inverse)
