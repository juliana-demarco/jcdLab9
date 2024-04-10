# juliana demarco

def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def main():
    while True:
        print_menu()
        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        if option == "2":
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {decoded_password}, and the original password is {encoded_password}")


def encode(password):
    encoded_password = ""
    for i in password:
        i = int(i)
        i += 3
        encoded_password += str(i)
    return encoded_password


if __name__ == "__main__":
    main()
