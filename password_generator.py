import random


# Main function to start password generation
def main():
    generate_password()


# Function to generate passwords
def generate_password():
    char = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%&*()_+-=[]{}|;':,./<>?"

    while True:
        try:
            # Ask if the user wants to generate a password from a string
            generate_string_password = str(
                input(
                    "Do you want to generate a password from a string? (Y/N) "
                ).upper()
            )
            if generate_string_password == "Y":
                # If yes, input the string and ensure password length is sufficient
                string_password = remove_accents(str(input("Type the string: ")))
                while True:
                    length = int(
                        input(
                            f"Type the length of the password: (At least {len(string_password) + 3} characters) "
                        )
                    )
                    if length >= len(string_password) + 3:
                        break
            else:
                # If no, input the desired password length
                length = int(
                    input(
                        "Type the length of the password: (We recommend at least 8 characters) "
                    )
                )

            qty = int(input("Type the quantity of passwords: "))

        except ValueError:
            print("Invalid value, try again.")

        for _ in range(0, qty):
            generated_password = ""
            if generate_string_password == "Y":
                # Generate password based on user input string
                for _ in range(length - len(string_password)):
                    passchar = random.choice(char)
                    generated_password += passchar
                    string_password, percent = password_from_string(string_password)
                generated_password = f"{generated_password[:len(generated_password) // 2]}{randomize_uppercase(string_password, percent)}{generated_password[len(generated_password) // 2:]}"
            else:
                # Generate a random password
                for _ in range(length):
                    passchar = random.choice(char)
                    generated_password += passchar
                generated_password = randomize_uppercase(
                    generated_password, int(round(length * 0.3, 0))
                )

            # Print the generated password and keyboard side count
            print(
                f"Password: {generated_password}\n{keyboard_side_count(generated_password)}"
            )
        break


# Function to remove accents from a string
def remove_accents(string):
    accents = {
        "a": ["á", "à", "ã", "â", "ä"],
        "e": ["é", "è", "ê", "ë"],
        "i": ["í", "ì", "î", "ï"],
        "o": ["ó", "ò", "õ", "ô", "ö"],
        "u": ["ú", "ù", "û", "ü"],
        "c": ["ç"],
    }
    for char in string:
        for key, value in accents.items():
            if char in value:
                string = string.replace(char, key)
    return string.replace(" ", "").lower()


# Function to create part of password based on a given string
def password_from_string(string):
    replace = {
        "a": "@",
        "c": "(",
        "d": ")",
        "e": "3",
        "g": "9",
        "h": "#",
        "i": "!",
        "l": "1",
        "o": "0",
        "s": "$",
        "t": "7",
        "z": "2",
    }

    percent = int(round(len(string) * 0.3, 0))
    chars_present_in_replace = [char for char in string if char in replace.keys()]
    if len(chars_present_in_replace) >= percent:
        chars_to_replace = chars_present_in_replace
    else:
        chars_to_replace = chars_present_in_replace

    string_list = list(string)

    for char in chars_to_replace:
        index = string.index(char)
        string_list[index] = replace[char]

    string = "".join(string_list)

    return string, percent


# Function to randomize uppercase letters
def randomize_uppercase(string, percent):
    string_list = list(string)
    for _ in range(0, percent):
        index = random.randint(0, len(string_list) - 1)
        if string_list[index].isalpha():
            string_list[index] = string_list[index].upper()
    return "".join(string_list)


# Function to count characters on the left and right sides of the keyboard
def keyboard_side_count(string):
    left_side = "\"'1!¹2@²3#³4$£5%¢6¨¬qwertasdfg\\|zxcv"
    right_side = "7&8*9(0)-_=+§yuiop[{hjklç]}bnm,<.>;:/?"

    total_chars = len(string)
    total_left_side = sum([1 for char in string.lower() if char in left_side])
    total_right_side = sum([1 for char in string.lower() if char in right_side])

    left_side_percent = round((total_left_side / total_chars) * 100, 2)
    right_side_percent = round((total_right_side / total_chars) * 100, 2)

    difference = abs(left_side_percent - right_side_percent)

    return (
        f"Both sides are balanced"
        if difference <= 10
        else f"Left side is heavier"
        if left_side_percent > right_side_percent
        else f"Right side is heavier"
    ) + f" (Left side: {left_side_percent}% vs Right side: {right_side_percent}%)\n"


# Entry point of the script
if __name__ == "__main__":
    main()
