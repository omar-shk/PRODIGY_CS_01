def encrypt(text, shift):
    """
    Encrypt the text using Caesar Cipher with the given shift.
    """
    encrypted_text = ""
    shift = shift % 26  # Normalize shift to be within 0-25
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters are not changed
    return encrypted_text

def decrypt(text, shift):
    """
    Decrypt the text using Caesar Cipher with the given shift.
    """
    return encrypt(text, -shift)

def get_shift_value():
    while True:
        try:
            shift = int(input("\033[96mEnter a magical shift number (positive for right, negative for left): \033[0m"))
            return shift
        except ValueError:
            print("\033[91mOops! That wasn't a number. Please try again.\033[0m")

def save_to_file(message, operation):
    with open("secret_log.txt", "a") as f:
        f.write(f"{operation.capitalize()} message: {message}\n")

def main():
    print("\033[94m✨ Welcome to the Secret Message Encrypter-Decrypter! ✨!\033[0m")
    print("\033[94mLet’s make your messages look mysterious or unveil the secrets! ✨!\033[0m")
    
    history = []
    
    while True:
        operation = input("\nWould you like to \033[92mencrypt 🔒\033[0m or \033[93mdecrypt 🔓\033[0m a message? (Enter 'e' for encrypt, 'd' for decrypt, or 'q' to quit): ").lower()
        
        if operation == 'q':
            print("\n\033[91mThanks for using the Secret Message Encrypter-Decrypter! 🛡️ Stay safe out there!\n\033[0m")
            if history:
                print("\n\033[94mHere's a summary of your past actions:\033[0m")
                for entry in history:
                    print(f"\033[93m- {entry}\033[0m")
            break
        
        elif operation in ['e', 'd']:
            message = input("\033[96mEnter the message that holds your secrets: \033[0m")
            shift = get_shift_value()
            
            if operation == 'e':
                result = encrypt(message, shift)
                print(f"\n\033[92m🔐 Encrypted message: {result}\033[0m")
                history.append(f"Encrypted message: {result}")
                save_to_file(result, "Encrypted")
            else:
                result = decrypt(message, shift)
                print(f"\n\033[93m🔓 Decrypted message: {result}\033[0m")
                history.append(f"Decrypted message: {result}")
                save_to_file(result, "Decrypted")
                
        else:
            print("\033[91mHmm... I didn't catch that. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.\033[0m")

if __name__ == "__main__":
    main()