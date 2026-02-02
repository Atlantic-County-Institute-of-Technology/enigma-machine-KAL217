# Katie Lopez
def encode_vigenere(message, key):
    message = message
    key = key.upper()
    encoded_message = ""
    key_index = 0

    for char in message:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                encoded_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encoded_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encoded_message += encoded_char


            key_index += 1
            if key_index == len(key):
                key_index = 0
        else:
            encoded_message += char

    return encoded_message


def decode_vigenere(message, key):
    message = message
    key = key.upper()
    decoded_message = ""
    key_index = 0

    for char in message:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                decoded_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decoded_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decoded_message += decoded_char

            key_index += 1
            if key_index == len(key):
                key_index = 0
        else:
            decoded_message += char

    return decoded_message


def write_file(filename, content):
    file = open(filename, "w")
    file.write(content)
    file.close()
    print("Message saved to", filename)


def read_file(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        file.close()
        return content
    except:
        print("File not found.")
        return None


def main():
    while True:
        print("\n--- Menu ---")
        print("1. Write and encode a message")
        print("2. Encode a message from a file")
        print("3. Decode a message from a file")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            message = input("Enter your message: ")
            key = input("Enter your key: ")
            encoded = encode_vigenere(message, key)
            print("Encoded message:")
            print(encoded)
            save = input("Save to file? (y/n): ")
            if save.lower() == "y":
                filename = input("Enter filename: ")
                write_file(filename, encoded)

        elif choice == "2":
            filename = input("Enter filename to read: ")
            content = read_file(filename)
            if content != None:
                key = input("Enter your key: ")
                encoded = encode_vigenere(content, key)
                print("Encoded message:")
                print(encoded)
                save = input("Overwrite file? (y/n): ")
                if save.lower() == "y":
                    write_file(filename, encoded)
                else:
                    new_file = input("Enter new filename: ")
                    write_file(new_file, encoded)

        elif choice == "3":
            filename = input("Enter filename to read: ")
            content = read_file(filename)
            if content != None:
                key = input("Enter your key: ")
                decoded = decode_vigenere(content, key)
                print("Decoded message:")
                print(decoded)
                save = input("Overwrite file? (y/n): ")
                if save.lower() == "y":
                    write_file(filename, decoded)
                else:
                    new_file = input("Enter new filename: ")
                    write_file(new_file, decoded)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


main()

