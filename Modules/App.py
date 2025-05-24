import converters #1
from converters import kgs_to_lbs #2
from utils import find_max

print(converters.kgs_to_lbs(70)) #1
print(kgs_to_lbs(70)) #2

numbers = [1, 3, 6, 2, 7, 10, 2, 5]
print(find_max(numbers))