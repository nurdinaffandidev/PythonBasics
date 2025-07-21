'''
    Update exercise 2(v.):
    - instead of using regex, how can we proceed a large file for the same method
'''

def convert_img_tag_line_by_line(file_path):
    # Open the file in read mode with UTF-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        # Init list for storing processed lines
        processed_lines = []

        # Process each line in the file one by one (memory efficient)
        for index, line in enumerate(file):
            # Process the line using the helper function
            processed_line = process_line(line, index)
            # Print the processed line with image tags inserted
            processed_lines.append(processed_line)

    return "\n".join(processed_lines)

def process_line(line, index=None):
    print(f"line number: {index}, line: {line}")
    # Split the line into individual words (based on spaces)
    words = line.split()
    result = []  # This will store the modified words for the output line

    # Iterate over each word
    for word in words:
        # Check if the word starts with '##' and has at least 5 characters after it
        if word.startswith("##") and len(word) >= 7:  # "##" + "abcde" = 7
            print(f"matched word = {word}")
            tag = word[2:]  # Remove the '##' prefix → e.g., '##smile,' becomes 'smile,'

            # Remove any non-alphanumeric characters from the tag (e.g., commas, punctuation)
            clean_tag = ''.join(filter(str.isalnum, tag))  # e.g., 'smile,' → 'smile'
            print(f"clean word = {clean_tag}")

            # Check if the cleaned tag is exactly 5 characters long
            if len(clean_tag) == 5:
                # Construct the image tag using the cleaned word
                img_tag = f'<img src="{clean_tag}.jpg"/>'

                # Preserve the original punctuation after the clean tag
                punct = word[len("##" + clean_tag):]  # extract punctuation after the valid tag

                # Append the final formatted image tag + punctuation
                result.append(img_tag + punct)
            else:
                # If not 5 characters, keep the original word unchanged
                result.append(word)
        else:
            # If word doesn't start with '##', just add it as is
            result.append(word)

    # Join all the processed words back into a single string
    print(f"updated list: {result}\n")
    return " ".join(result)


if __name__ == "__main__":
    print(f"\nconverted_text:\n{convert_img_tag_line_by_line("input.txt")}")


