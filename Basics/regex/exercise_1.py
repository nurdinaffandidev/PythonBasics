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
"""

# Import regex module
import re

# Function to convert ##word patterns into <img src="word.jpg"/>
def convert_img_tag(text):
    print(f"\ninput text = {text}")
    # Define a regex pattern to find substrings starting with '##' followed by word characters (alphanumeric + underscore)
    # pattern = r"(##\w+)" # (i.)
    # pattern = r"(##\w{5,})" # (ii.)
    pattern = r"(##\w{5}\b)" # (iii.)

    # Find all matching patterns in the text
    list_to_convert = re.findall(pattern, text)
    print(f"list_to_convert = {list_to_convert}")

    if list_to_convert:
        converted_text_list = []
        # For each matched item like ##smile
        for item in list_to_convert:
            prefix_new_text = "<img src=\"" # Start HTML img tag
            remaining_text = item[2:]       # Remove leading '##' (e.g., 'smile' from '##smile')
            suffix_new_text = remaining_text + "\".jpg/>"   # Complete img tag
            converted_text_list.append(prefix_new_text + suffix_new_text)

        # Start with the original text
        new_text = text
        # Replace each original ##word with corresponding <img src="word.jpg"/>
        for i in range(len(list_to_convert)):
            new_text = re.sub(list_to_convert[i], converted_text_list[i], new_text)
        return new_text
    else:
        return text # Return original text if nothing to replace


if  __name__ == "__main__":
    input_text = "hello ##smile, what a good day!##lol ##laugh ##smiling"
    print(f"converted text = {convert_img_tag(input_text)}")