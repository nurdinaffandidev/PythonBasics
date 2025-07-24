
"""
input = 'hello ##smile, what a good day!##laugh'
output = 'hello <img src="smile.jpg"/>, what a good day!<img src="laugh.jpg"/>'

what if I want my function to check if inputs are in correct format like
    - must have double # sign
    - followed by a String that is at exactly 5 characters long

    FOR LARGE FILES!!
"""

print()
import re

def convert_img_tags_in_line(line):
    pattern = r"##(\w{5})\b"  # Match ## followed by a word with exactly 5 characters

    def replacer(match):
        tag = match.group(1)
        return f"<img src='{tag}.jpg'/>"
    return re.sub(pattern, replacer, line)


def convert_file_with_img_tags(input_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
        print(f"lines: {lines}")

    converted_lines = [convert_img_tags_in_line(line) for line in lines]
    print(f"converted lines: {converted_lines}")

    return "".join(converted_lines)


if __name__ == "__main__":
    input_file = "input.txt"
    print(convert_file_with_img_tags(input_file))
