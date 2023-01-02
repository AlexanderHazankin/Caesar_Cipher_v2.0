# Import the clear and art modules to clear the screen and display the art logo
from replit import clear
import art

# Display the art logo
print(art.logo)

# Create a list of all the characters that can be encoded/decoded
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^',
            '&', '*', '(', ')', ' ']


def cipher(text, shift, direction):
    """
    Encrypts or decrypts a message using a Caesar cipher.

    Parameters:
    text (str): The message to be encoded or decoded.
    shift (int): The number of characters to shift the message.
    cipher_direction (str): The direction of the cipher, either 'encode' or 'decode'.

    Returns:
    str: The encoded or decoded message.
    """
    # Initialize an empty string to store the cipher text
    cipher_text = ""

    # If the cipher direction is 'decode', negate the shift value
    if direction == "decode":
        shift *= -1

    # Iterate through each character in the text
    for char in text:

        # If the character is in the alphabet, shift its position and add it to the cipher text
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % len(alphabet)
            cipher_text += alphabet[new_position]

        # If the character is not in the alphabet, add it to the cipher text as is
        else:
            cipher_text += char

    # Print the encoded or decoded message
    print(f"Here's the {direction}d result: '{cipher_text}'")


# Initialize play_again variable to True to allow the loop to run at least once
play_again = True

# Run the loop as long as play_again is True
while play_again:

    # Clear the screen (function not shown)
    clear()

    # Prompt the user to choose whether to encode or decode a message
    cipher_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    # If the user inputs an invalid direction, continue to prompt them until they provide a valid input
    while cipher_direction != 'encode' and cipher_direction != 'decode':
        cipher_direction = input("Invalid direction. Please type 'encode' or 'decode':\n")

    # Get the message from the user and convert it to lowercase
    test_to_use = input("Type your message:\n").lower()

    # Get the shift number from the user
    # If the user inputs an invalid value (e.g. a non-integer), continue to prompt them until they provide a valid input
    while True:
        try:
            shift_amount = int(input("Type the shift number:\n"))
            break
        except ValueError:
            print("Invalid direction. Must to be a digit:\n")

    # Call the cipher function with the provided text, shift, and cipher direction
    cipher(text=test_to_use, shift=shift_amount, direction=cipher_direction)

    # Prompt the user to choose whether to run the program again
    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")

    # If the user inputs an invalid response, continue to prompt them until they provide a valid input
    while play_again != 'yes' and play_again != 'no':
        play_again = input("Invalid direction. Please type 'yes' or 'no':\n")

    # If the user chooses not to run the program again, set play_again to 'False' to exit the loop
    if play_again == "no":
        play_again = False
        print("Goodbye")
