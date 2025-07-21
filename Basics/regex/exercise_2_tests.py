import unittest
from exercise_2 import convert_img_tag


class TestConversion(unittest.TestCase):
    def test_convert_img_tag_optimal(self):
        input_txt = "hello ##smile, what a good day!##lol ##laugh ##smiling"
        expected_output = 'hello <img src="smile.jpg"/>, what a good day!##lol <img src="laugh.jpg"/> ##smiling'
        result = convert_img_tag(input_txt)
        self.assertEqual(result, expected_output)

