'''
Implement a state machine for conversion
'''

import re
from enum import Enum

class State(Enum):
    START = "START"
    TEXT = "TEXT"
    IMG_TAG = "IMG_TAG"

class Parser:
    def __init__(self):
        self.state = State.START


    def transition(self, line):
        converted_line_words = []
        for word in line.split(" "):
            match self.state:
                case State.START:
                    if "##" in word:
                        self.state = State.IMG_TAG
                        converted_line_words.append(self.handle_img_tag(word))
                    else:
                        self.state = State.TEXT
                        converted_line_words.append(self.handle_text(word))

                case State.TEXT:
                    if "##" in word:
                        self.state = State.IMG_TAG
                        converted_line_words.append(self.handle_img_tag(word))
                    else:
                        converted_line_words.append(self.handle_text(word))

                case State.IMG_TAG:
                    if "##" in word:
                        converted_line_words.append(self.handle_img_tag(word))
                    else:
                        self.state = State.TEXT
                        converted_line_words.append(self.handle_text(word))

        converted_line = ' '.join(word for word in converted_line_words)
        return converted_line


    def handle_img_tag(self, word):
        pattern = r"##(\w{5}\b)"
        def replacer(match):
            tag = match.group(1)
            return f"<img src='{tag}.jpg'/>"

        return re.sub(pattern, replacer, word)


    def handle_text(self, word):
        return word


if __name__ == "__main__":
    # Usage
    parser = Parser()
    with open("input.txt", encoding='utf-8') as file:
        list_of_lines = file.readlines()
        # print(list_of_lines)
        converted_lines = [parser.transition(line) for line in list_of_lines]
        # print(converted_lines)

        print("\nResult:")
        print("======================")
        print("".join(converted_lines))
