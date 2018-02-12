
choice = input("Enter 1 for encryption and 2 for decryption:")
encrypted = ''
shift_value = 5
if choice == "1":
    message = input("Enter the message you want to encrypt here:").upper()
    for character in message:
        if character == " ":
            encrypted += " "
        elif ord(character) + shift_value > ord("Z"):
            encrypted += chr(ord(character) + shift_value - 26)
        else:
            encrypted += chr(ord(character) + shift_value)
    print(encrypted)

if choice == "2":
    message = input("Enter the message you want to decrypt here:").upper()
    for character in message:
        if character == " ":
            encrypted += " "
        elif ord(character) - shift_value < ord("A"):
            encrypted += chr(ord(character) - shift_value + 26)
        else:
            encrypted += chr(ord(character) - shift_value)
    print(encrypted)
