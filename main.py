import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, cipher_direction):
    cipher_text = ""

    for char in plain_text:
        if char not in alphabet:
            cipher_text += char
        elif cipher_direction == "decode":
            position = alphabet[::].index(char)
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        elif cipher_direction == "encode":
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter

    print(f"the {direction}d text is {cipher_text.title()}\n")


active = True

while active:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("would you like to try "
                   "another cipher input, 'no' or 'yes': ").lower()
    if result == "no":
        active = False
        print("\nGoodbye!")
