import unittest

from tdd_sum import super_sum

class SuperSumTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_sum_of_integers(self):
		
		#Test sum of integers
		
		self.assertEqual(super_sum(10, 5, 6, 9), 30)


	def test_sum_of_list_and_integers(self):
		
		#Test sum of list and integers

		self.assertEqual(super_sum([10, 5], 5), 20)


	def test_sum_of_2lists_and_integers(self):
		
		#Test sum of two list and integers

		self.assertEqual(super_sum([5, 6], [4, 5], 10), 30)


	def test_empty_argument(self):

		#Test if empty argument. 

		self.assertIsNone(super_sum(), msg='Should have argument')


	def test_string(self):

		#Test if string is present

		with self.assertRaises(TypeError):
			super_sum('a', 'z')



if __name__ == '__main__':
	unittest.main()