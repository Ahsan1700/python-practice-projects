from art import logo

def find_highest(my_dict):
    highest_val = 0
    highest_key = ""
    for key in my_dict:
        if my_dict[key] > highest_val:
            highest_key = key
            highest_val = my_dict[key]

    return highest_key

bidders = {}
highest_bidder = ""
continue_bid = True

print(logo)

while continue_bid:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))

    bidders[name] = bid

    cont = input("Are there any other bidders? [y/n] \n")
    if cont != 'y':
        continue_bid = False
        highest_bidder = find_highest(bidders)
        print(f"The winner of the auction is {highest_bidder}!")
    else:
        print("\n"*20)