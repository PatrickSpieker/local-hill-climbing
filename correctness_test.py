import unittest

from algos import patrick_algo, aaron_algo

class TestHillClimbingAlgo(unittest.TestCase):
    def test_start_edgecase(self):
        array = [90, -1, -50, -70]

        patrick_result = patrick_algo(array)
        aaron_result = aaron_algo(array) 
        
        self.assertEqual(0, patrick_result[0])
        self.assertEqual(0, aaron_result[0])
    
    def test_end_edgecase(self):
        array = [50, 70, 90, 100]

        patrick_result = patrick_algo(array)
        aaron_result = aaron_algo(array) 
        
        self.assertEqual(3, aaron_result[0])
        self.assertEqual(3, patrick_result[0])

    def test_basic(self):
        array = [50, 70, 90, 80]

        patrick_result = patrick_algo(array)
        aaron_result = aaron_algo(array) 
        
        self.assertEqual(2, aaron_result[0])
        self.assertEqual(2, patrick_result[0]) 

if __name__ == '__main__':
    unittest.main()