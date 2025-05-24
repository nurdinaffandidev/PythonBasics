is_hot = True
is_cold = True

if is_hot and not is_cold:
    print("It's a hot day")
elif is_cold and not is_hot:
    print("It's a cold day")
elif is_hot and is_cold:
    print("It's a confusing day")
else:
    print("It's a great day")

'''
Exercise:
    Price of a house is $1M. 
    If buyer has good credit, they need to put down 10%.
    Otherwise, they need to put down 20%.
    Print down payment.
'''
has_good_credit = False

if has_good_credit:
    print(f"Down payment required = ${str(int(1_000_000 * 0.1))}")
else:
    print(f"Down payment required = ${str(int(1_000_000 * 0.2))}")