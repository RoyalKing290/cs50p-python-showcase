# Ask the user for input and print the validity
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# Define a function to check validity
def is_valid(s):
    # 1. Length check (2-6 chars)
    if not (2 <= len(s) <= 6):
        return False

    # 2. Must start with at least two letters
    if not s[0:2].isalpha():
        return False

    # 3. Must be alphanumeric (no spaces/punctuation)
    if not s.isalnum():
        return False

    # 4. Check numbers
    for i in range(len(s)):
        if s[i].isdigit():
            # First number cannot be '0'
            if s[i] == '0':
                return False

            # Once a number starts, the REST of the string must be numbers
            if not s[i:].isdigit():
                return False

            # If the rest are digits, we are good!
            break

    return True


main()
