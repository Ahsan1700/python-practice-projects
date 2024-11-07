from art import logo

def caesar(original_message, shift_amount, encode_or_decode):
    res = ""
    if direction == "decode":
        shift_amount *= -1

    for char in text:
        if char.isalpha():
            shifted = (ord(char) + shift_amount - ord("a")) % 26 + ord("a")
            res += chr(shifted)
        else:
            res += char

    return res


finished = False
print(logo)

while not finished:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        msg = caesar(text, shift, direction)
        print(f"The encoded result is '{msg}'")
    elif direction == "decode":
        msg = caesar(text, shift, direction)
        print(f"The decoded result is '{msg}'")
    else:
        print("Invalid entry")

    restart = input("Go Again? [y/n]\n")
    if restart != 'y':
        finished = True

