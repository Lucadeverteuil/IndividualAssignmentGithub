
import random
import unittest
import numpy as np
from array import *

def createArry(): #creates an array for the user
    arry = [6,5,4,7,38,9,4,8,5,7]
    return arry

def sortArry(arry): # this will sort and return the array to the user
    arry.sort()
    return arry

def randomValue(arry):
    size = len(arry)
    randNum = np.random.randint(0,size)
    return arry[randNum]

arry = createArry() # gets function 

while True: #while loop to ask user how what tasks they want to be done
    print(("What would you like to do?")) 
    print("1: print the array")
    print("2: order the array")
    print("3: choose a random value of the array")
    inp =input()
    if inp is "1":
        print(arry) # prints array   
    elif inp is "2":
        print(sortArry(arry))
    elif inp is "3":
        print(randomValue(arry))
    else: 
        break    





class MyTest(unittest.TestCase): #test cases for both creating an array and sort array
    def test_mkArry(self):
      self.assertEqual(createArry(),[6, 5, 4, 7, 38, 9, 4, 8, 5, 7] )
    def test_sortArray(self):
        self.assertEqual(sortArry(arry),[4, 4, 5, 5, 6, 7, 7, 8, 9, 38])
    def test_randomValue(self):
        x = randomValue(arry)
        y =0
        for i in arry:
            if x == arry[i]:
                y = i 
                break
        self.assertEqual(x,arry[y])  
       
unittest.main()