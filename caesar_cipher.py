alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("type 'encode' to encrypt and 'decode' to decrypt: \n")
text = input("type your message: \n").lower()
shift = int(input("type the shift number: \n"))
shift = shift % 26
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded code is {cipher_text}")
    


# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The decoded message is {plain_text}")
    
    
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
    
    
def caesar(start_text, direction_taken, shift_amount):
    end_text = ""
    if direction == "decode":
        shift_amount = shift_amount * -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text = end_text + alphabet[new_position]
        else:
            end_text = end_text + char
    print(f"The {direction_taken}d message is {end_text}")       
            

caesar(start_text=text, direction_taken=direction, shift_amount=shift)
        
    