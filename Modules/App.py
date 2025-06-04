import converters #1
from converters import kgs_to_lbs, test_numbers as test_num #2
from utils import find_max
import converters as cvt #3

import sys

print(converters.kgs_to_lbs(70)) #1
print(kgs_to_lbs(70)) #2
print(cvt.kgs_to_lbs(70))  #3

numbers = [1, 3, 6, 2, 7, 10, 2, 5]
print(find_max(numbers))

print(converters.test_numbers) #1
print(test_num) #2
print(cvt.test_numbers) #3

print(sys.path)