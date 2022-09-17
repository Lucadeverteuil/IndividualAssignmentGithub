import unittest
import numpy as np
from array import *

def createArry(): #creates an array for the user
    arry = [6,5,4,7,38,9,4,8,5,7]
    return arry

def sortArry(arry): # this will sort and return the array to the user
    arry.sort()
    return arry

arry = createArry() # gets function 

while True: #while loop to ask user how what tasks they want to be done
    print(("What would you like to do?")) 
    print("1: print the array")
    print("2: order the array")
    inp =input()
    if inp is "1":
        print(arry) # prints array   
    elif inp is "2":
        print(sortArry(arry))
    else: 
        break    





class MyTest(unittest.TestCase): #test cases for both creating an array and sort array
    def test_mkArry(self):
      self.assertEqual(createArry(), [6,5,4,7,38,9,4,8,5,7])
    def test_sortArray(self):
        arry = [6,5,4,7,38,9,4,8,5,7]
        self.assertEqual(sortArry(arry),[4, 4, 5, 5, 6, 7, 7, 8, 9, 38])
unittest.main()

        

 
  