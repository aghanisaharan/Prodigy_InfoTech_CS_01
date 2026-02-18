def caesar_cipher(text, shift, mode='encrypt'):
    # Normalize shift for letters and digits
    shift_letters = shift % 26
    shift_digits = shift % 10
    result = ""

    if mode == 'decrypt':
        shift_letters = -shift_letters
        shift_digits = -shift_digits

    for char in text:
        if char.isalpha():  # Shift alphabets
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_letters) % 26 + base)
        elif char.isdigit():  # Shift digits individually
            result += str((int(char) + shift_digits) % 10)
        else:
            # Preserve spaces and punctuation
            result += char
    return result


def print_banner():
    print("=" * 50)
    print("        🔐 Caesar Cipher Encryption Tool")
    print("=" * 50)


while True:
    print_banner()
    print("Choose an option:")
    print(" [e] Encrypt a message")
    print(" [d] Decrypt a message")
    print(" [q] Quit")
    print("-" * 50)

    # Validate choice input
    choice = ""
    while choice not in ['e', 'd', 'q']:
        choice = input("Enter your choice (e/d/q): ").lower()
        if choice not in ['e', 'd', 'q']:
            print("❌ Invalid choice. Please enter only 'e', 'd', or 'q'.")

    if choice == 'q':
        print("\n👋 Exiting program. Goodbye!\n")
        break

    # Message input (letters, digits, spaces, punctuation allowed)
    message = input("\nEnter your message: ")

    # Validate shift input (must be a number)
    while True:
        try:
            shift = int(input("Enter shift value (number): "))
            break
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")

    print("-" * 50)
    if choice == 'e':
        encrypted = caesar_cipher(message, shift, 'encrypt')
        print(f"✅ Encrypted message: {encrypted}")
    elif choice == 'd':
        decrypted = caesar_cipher(message, shift, 'decrypt')
        print(f"✅ Decrypted message: {decrypted}")
    print("-" * 50 + "\n")
