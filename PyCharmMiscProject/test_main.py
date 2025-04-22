import unittest

import main


class TestMain(unittest.TestCase):

    def setUp(self):
        print("Some set up before run the test")

    def test_add_five_to_num(self):
        test_param = 10
        result = main.add_five_to_num(test_param)
        self.assertEqual(result, 15)

    def test_add_five_to_num_with_string_param(self):
        test_param = "text"
        result = main.add_five_to_num(test_param)
        self.assertIsInstance(result, ValueError)

    def test_add_five_to_num_with_float_param(self):
        test_param = 3.257
        result = main.add_five_to_num(test_param)
        self.assertEqual(result, 8.26)

    def test_add_five_to_num_with_none_param(self):
        test_param = None
        result = main.add_five_to_num(test_param)
        self.assertEqual(result, "Enter a number")

    def test_add_five_to_num_without_param(self):
        result = main.add_five_to_num()
        print(result)
        self.assertEqual(result, "Enter a number")

    def tearDown(self):
        print("Cleaning up")


if __name__ == '__main__':
    unittest.main()
