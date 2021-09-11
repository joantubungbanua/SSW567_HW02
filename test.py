import unittest
import math

from classify_triangle import classify_triangle



class TestTriangles(unittest.TestCase): 
    def test_equilateral(self): 
        side1 = 1
        side2 = 1
        side3 = 1
        result = classify_triangle(side1,side2,side3)
        self.assertEqual(result,"equilateral triangle")
    def test_isoceles(self): 
        side1 = 2
        side2 = 2
        side3 = 4
        result = classify_triangle(side1,side2,side3)
        self.assertEqual(result,"isoceles triangle")
    def test_isoceles_right(self): 
        side1 = 1
        side2 = 1
        side3 = math.sqrt(2)
        result = classify_triangle(side1,side2,side3)
        self.assertEqual(result,"isoceles right triangle")
    def test_scalene(self): 
        side1 = 2
        side2 = 3
        side3 = 5
        result = classify_triangle(side1,side2,side3)
        self.assertEqual(result,"scalene triangle")
    def test_scalene_right(self): 
        side1 = 24
        side2 = 10
        side3 = 26
        result = classify_triangle(side1,side2,side3)
        self.assertEqual(result,"scalene right triangle")
    def test_bug(self): 
        side1 = 3
        side2 = 3
        side3 = 3
        result = classify_triangle(side1,side2,side3)
        self.assertEqual(result,"scalene triangle")
    
    



if __name__== '__main__': 
    unittest.main()