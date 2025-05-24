message = input(">")
words = message.split(" ")

emojis = {
    ":)" : "🙂",
    ":(" : "😔"
}
output_string = ""
for word in words:
    output_string += emojis.get(word, word) + " "

print(output_string)