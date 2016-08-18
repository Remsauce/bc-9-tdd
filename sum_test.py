import unittest

from my_sum import my_sum

class MySumTests(unittest.TestCase):

	def test_sum_of_digits(self):
		
		#Test sum of digits or numbers
		
		result = my_sum(5,10)
		self.assertEqual(result, 15)
		self.assertEqual(
			my_sum(10, 15), 25,
			msg='should return sum of each')

		#assertEqual tests the sum of the numbers 
		#you'll pass. The last digit is where you give 
		#it the answer it should expect.

	def test_non_numbers(self):
		with self.assertRaises(TypeError):
			my_sum('1', '4', msg='arguements should be integers')

	

if __name__ == '__main__':
	unittest.main()
		#this ifmain function automates the testi.e. run the test
		#if and only if someone has run the function.. 