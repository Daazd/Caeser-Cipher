
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            else:
                alphabet = 'abcdefghijklmnopqrstuvwxyz'
            index = alphabet.find(char)
            shifted_index = (index + shift) % 26
            result += alphabet[shifted_index]
        else:
            result += char
    return result

# Example Usage:
text = "Thank you for checking out my code"
shift = 8
encrypted_text = caesar_cipher(text, shift)
print("Encrypted:", encrypted_text)

# to decrypt use a negative shift
decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted:", decrypted_text)