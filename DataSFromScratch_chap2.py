"""try:
    print(0/0)
except ZeroDivisionError:
    print("cannot divide by zero!")


def minValue(list=[]):
    n = len(list)
    min = list[0]
    counter = 1
    while counter < n:
        if list[counter] < min:
            min = list[counter]
            index = counter
        counter = counter + 1
    return min, index
"""
"""def sortList(list=[]):
    n = len(list)
    list2 = []
    counter = 0
    while counter < n:
        unpack = minValue(list)
        del list[unpack[1]]
        list2.append(unpack[0])
        n = n - 1
    return list2        
sortList([1, -2, 3, -3, 4])"""

"""b = eval(input("type in anything: "))
print(type(b))
a = int(input("Enter your Exam Score: "))

if a >= 70:
    print("Grade: A")
elif a < 70 and a >=60:
    print("Grade: B")
elif a >=50 and a < 60:
    print("Grade: C")
elif a >= 45 and a < 50:
    print("Grade: D")
elif a >= 40 and a < 45:
    print("Grade: E")
else:
    print("Grade: F")"""

a = int(eval(input("Enter a decimal number:")))
if a > 0:
    if a % 2 == 0:
        print("Input is an even number")
    else:
        print("Definitely odd")
else:
    print("Invalid input")