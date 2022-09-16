import unittest
import numpy as np
from array import *

def createArry(): #creates an array for the user
    arry = {1,2,3,4,5,6,7,8,9}
    return arry

arry = createArry() # gets function 
print(arry) # prints array 

class MyTest(unittest.TestCase):
    def test_mkArry(self):
        self.assertEqual(createArry(), {1, 2, 3, 4, 5, 6, 7, 8, 9})
unittest.main()
        