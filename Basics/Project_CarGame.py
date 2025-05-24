command = ""
is_started = False
while True:
    command = input("Enter command > ").lower()
    match command:
        case "start":
            if is_started:
                print("Car already started")
            else :
                is_started = True
                print("Car started....")
        case "stop":
            if not is_started:
                print("Car already stopped")
            else :
                is_started = False
                print("Car stopped....")
        case "quit":
            print("Bye....")
            break
        case "help":
            print("""start - to start the car
stop - to stop the car
quit - to quit the game""")
        case _:
            print("Invalid command")
