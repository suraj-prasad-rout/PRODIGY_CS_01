import string

# Create a list of lowercase alphabets using string.ascii_lowercase
alphabet_list = list(string.ascii_lowercase)

# Function to encrypt or decrypt the plain text based on the mode (encrypt or decrypt)


def encrypt_decrypt(plain_text, shift_key, mode):
    result_text = ""
    for char in plain_text:
        if char in alphabet_list:  # Check if the character is a lowercase alphabet
            # Get the index of the character in the alphabet list
            position = alphabet_list.index(char)
            if mode == "encrypt":
                # Calculate new position for encryption
                new_position = (position + shift_key) % 26
            elif mode == "decrypt":
                # Calculate new position for decryption
                new_position = (position - shift_key) % 26
            # Append the encrypted or decrypted character to result_text
            result_text += alphabet_list[new_position]
        else:
            result_text += char  # Append non-alphabet characters directly
    return result_text


# Main program loop to interact with the user
wana_do = True
while wana_do:
    what_to_do = input(
        "Type 'encrypt' for encryption, type 'decrypt' for decryption:\n").lower()

    if what_to_do == "encrypt" or what_to_do == "decrypt":
        # Get user input for the text to encrypt or decrypt
        text = input("Enter your text:\n").lower()
        # Get user input for the shift key
        shift = int(input("Enter shift key:\n"))

        if what_to_do == "encrypt":
            encrypted_text = encrypt_decrypt(
                text, shift, mode='encrypt')  # Encrypt the text
            # Print the encrypted text
            print(f"Encrypted text: {encrypted_text}")

        elif what_to_do == "decrypt":
            decrypted_text = encrypt_decrypt(
                text, shift, mode='decrypt')  # Decrypt the text
            # Print the decrypted text
            print(f"Decrypted text: {decrypted_text}")

    else:
        print("Invalid input")  # Inform user of invalid input

    play_it_again = input(
        "Type 'yes' to go again. Otherwise type 'no':\n").lower()
    if play_it_again != "yes":
        # End the program if user does not want to continue
        print("Have a good day bye...")
        wana_do = False  # Set wana_do to False to exit the loop
