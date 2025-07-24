# This code runs only in python 3.10 or above versions
def number_to_string(argument):
    match argument:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case default:
            return "failed to convert"


head = number_to_string(1)
print(head)