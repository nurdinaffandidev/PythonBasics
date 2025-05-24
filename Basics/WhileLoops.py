i = 1
while i <= 5:
    print("*" * i)
    i += 1
print("Done")

# Guessing game
# Guess number within 3 attempts
secret_number = 9
attempt = 0
while attempt < 3:
    attempt += 1
    input_number = int(input("Enter number: "))
    if input_number == secret_number:
        print(f"You WON! Secret number: {secret_number}")
        break
    elif attempt == 3:
        print("You Lost..")
        break
