"""
    i. Create a function (without regex) to check if inputs are in correct format like
        - must have double # sign
        - followed by a String that can be of any characters long

    Test:
        input = 'hello ##smile, what a good day!##lol ##laugh ##smiling'
        output = 'hello <img src="smile.jpg"/>, what a good day!<img src="lol.jpg"/> <img src="laugh.jpg"/> <img src="smiling.jpg"/>'

    ii. Update solution from (i) so that it
        - must have double # sign
        - followed by a String that can be of at least 5 characters long

    Test:
        input = 'hello ##smile, what a good day!##lol ##laugh ##smiling'
        output = 'hello <img src="smile".jpg/>, what a good day!##lol <img src="laugh".jpg/> <img src="smiling".jpg/>'

    iii. Update above solutions so that it
        - must have double # sign
        - followed by a String that can is only 5 characters long

    Test:
        input = 'hello ##smile, what a good day!##lol ##laugh ##smiling'
        output = 'hello <img src="smile".jpg/>, what a good day!##lol <img src="laugh".jpg/> ##smiling'

    Solution:
        - update pattern matching

    iv. Update to read input text from file
    Solution:
        - Implement .read() to read input text from file.

    v. How would you implement reading of large files?
    Solution:
        - Implement .readlines() to store read lines as a list of lines
        - .readlines() is ideal for large files when:
            > You need to process the file line-by-line.
            > You want to avoid loading everything into memory as one big blob (as .read() would do).
"""

# Import the regular expressions module
import re

# Function to convert matched patterns to <img> tags
def convert_img_tag(text, line_index=None):
    # Define a regex pattern to match
    # pattern = r"##(\w+)" # (i.)
    # pattern = r"##(\w{5,})" # (ii.)
    pattern = r"##(\w{5})\b" # (iii.)

    if line_index != None:
        print(f"matches: (line {line_index}) {re.findall(pattern, text)}")
    else:
        print(f"matches: {re.findall(pattern, text)}")

    # Replace all matches in text with the result of replace_with_img()
    return re.sub(pattern, replace_with_img_tag, text)


# Replacement function for re.sub
def replace_with_img_tag(match):
    img_name = match.group(1)   # Extract the matched word (without ##)
    return f'<img src="{img_name}.jpg"/>'   # Return the formatted <img> tag


# Utility function to read input from a file (.iv)
def read_input_file(file_path):
    # Open and read the entire file content
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# Utility function to read lines from a file (.v)
def readlines_input_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        list_of_lines = file.readlines()
        return list_of_lines


if __name__ == "__main__":
    # without read
    print("\n====================")
    print("Manual input:")
    print("====================")
    input_text = "hello ##smile, what a good day!##lol ##laugh ##smiling"
    print(f"input text = {input_text}\n")
    print(f"converted text = {convert_img_tag(input_text)}")

    # with .read()
    print("\n====================")
    print("Read file input:")
    print("====================")
    input_file = "input.txt"
    print(f"input file = {input_file}")
    input_text = read_input_file(input_file)
    print(f"input text from file = {input_text}\n")
    print(f"converted input text = {convert_img_tag(input_text)}")

    # with .readline()
    print("\n====================")
    print("Read lines in file:")
    print("====================")
    input_file = "input.txt"
    print(f"input file = {input_file}")
    lines = readlines_input_file(input_file)
    print(f"lines from file = {lines}\n")
    converted_lines = [convert_img_tag(line, line_index=index) for index,line in enumerate(lines)]
    print(f"converted_lines = {converted_lines}")


'''
    If replaced the input sentence with a text file, what problems can occur? 
    -	UnicodeDecodeError  -> (Corrupted or Non-Text File)
    -	FileNotFoundError -> (File path do not exist)
    -	PermissionError -> (No permission to read/write)
    -	IsADirectoryError -> (Tried to open directory as if it is a file)
    -	Large file size
    -	Empty File
'''