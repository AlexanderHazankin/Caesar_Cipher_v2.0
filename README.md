# Caesar Cipher version 2.0
This program allows users to encode and decode text using a Caesar cipher.

## Modification
This modified version of the original code includes a few changes:

The 'encode' and 'decode' functions have been combined into a single cipher function, which takes in a string of text,
an integer shift value, and a string representing the direction of the cipher ('encode' or 'decode').

The cipher function converts the text to lowercase before iterating through the characters.

The cipher function allows any character that is not in the alphabet to be passed through unmodified.

The cipher function negates the shift value if the cipher direction is 'decode',
which allows it to work in both directions without the need for separate functions.

The main function has been updated to import the clear and art modules, display the art logo,
and prompt the user for input to determine the cipher direction and shift value.
It also includes a loop that allows the user to run the program multiple times until they choose to exit.

The main function has been updated to validate the user's input for the cipher direction and whether to
run the program again. If the input is invalid, it continues to prompt the user until they provide a valid response.

The main function has been updated to print a goodbye message when the program is exited.

## Features
Encrypt and decrypt text using a Caesar cipher

User can specify the shift to use in the cipher

Alphabet can be customized to include any combination of characters

## Usage
Run the program

Choose to either encode or decode a message

Enter the message

Enter the shift value

View the resulting encoded or decoded message

## Customization
The alphabet used in the cipher can be customized by modifying the alphabet list in the main() function.
Simply add or remove any characters you wish to include or exclude from the alphabet.

## Requirements
Requires Python 3.x to run.

## Credits
Created by Alexander Hazankin.

## Contact
For any questions or comments, you can reach me at:

https://www.linkedin.com/in/hazankin

https://github.com/AlexanderHazankin

https://replit.com/@Hazankin

## License
This project is licensed under the MIT License.

Copyright (c) 2022 Alexander Hazankin.

Permission is hereby granted, free of charge.

## NOTE:
This is one of my exercises from Udemy online Course: "100 Days of Code: The Complete Python Pro Bootcamp for 2022" by Dr. Angela Yu
