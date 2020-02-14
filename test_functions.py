import unittest
from functions import *

class TestFunctions(unittest.TestCase):

	def test_derive_coordinates(self):
		# Creates 3 list test subjects
		list1 = ['f1','b1']
		list2 = ['f1','l1','b1','r1']
		list3 = ['F1' ,'R1', 'B2','L1','B3' ]

		# Derives 3 sets of coordinates from test subjects
		x1,y1 = derive_coordinates(list1, 0, 0)
		x2,y2 = derive_coordinates(list2, 0, 0)
		x3,y3 = derive_coordinates(list3, 0, 0)

		# Checks if tested values are corret
		self.assertEqual(x1, 0)
		self.assertEqual(y1, 0)
		self.assertEqual(x2, 0)
		self.assertEqual(y2, 0)
		self.assertEqual(x3, 0)
		self.assertEqual(y3, -4)

	def test_find_distance(self):
		# Tests 3 distance problems and retrieves distance
		dist1 = find_distance(0,0,1,5)
		dist2 = find_distance(0,0,-1,-5)
		dist3 = find_distance(1,-1,0,0)

		# Checks if tested values are correct
		self.assertEqual(dist1, 6)
		self.assertEqual(dist2, 6)
		self.assertEqual(dist3, 2)

if __name__ == '__main__':
	unittest.main()