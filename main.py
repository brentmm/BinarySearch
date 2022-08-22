from random import randint
import math

#generates list if 10 random numbers
def test():
    a = []
    for p in range(0, 10):
      a.append(randint(0, 10))
    return a

def insertionSort(c):
    n = len(c)
    for i in range(0,n):
        count = i
        while count > 0:
            if c[count] < c[count-1]:
                c[count], c[count-1] = c[count-1], c[count] #moves index to front of list
                count = count - 1
            else:
                count = 0
    return c

def binarySearch(d):
    userInput = int(input("Pick an Integer: "))  #user Chooses a number to search for
    n = len(d)
    t = 0   
    for x in range(t,n):
        mid = math.floor((n-(n - t)//2))
        if mid == userInput:  #checks if list index value = userInput
            indexNum = d.index(mid) #storing what index userInput is
            found = True  #if number is found
            return userInput, indexNum, found
        elif mid > userInput:
            n = mid
        elif mid < userInput:
            t = mid
        else:
          indexNum = False  #stores false if userInput is not found
          found = False  #if userInput is not found

b = test()
c = insertionSort(b)
print(c)
d = binarySearch(c)

if d[2] == True:
    print("Found " + str(d[0]) + " at index " + str(d[1]) + ".")
else:
    print(str(d[0]) + " not found.")