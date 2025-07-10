# The Binary Input String
binary_input = input("Enter a Binary Number: ")

# Removes Spaces from Input to Avoid Converting ' ' to Integer
cleaned_binary = binary_input.replace(' ', '')

def binary_to_decimal(binary):
    decimal = 0
    # The Conversion Algorithm
    for i in range(len(binary)):
        decimal += int(binary[-(i+1)]) * 2 ** i
    return decimal 

# The Main Function: Checks for Invalidity Before Converting
def main():
    ## INVALIDITY CHECKS

    # Checks if Alphabetical Characters Have Been Used
    if not cleaned_binary.isdigit():
        print("Error: Input must contain only digits (0 or 1).")
        return

    invalid_digits = [i for i in cleaned_binary if i not in ('0', '1')] # Stores the Non-Binary Digits
    # Checks The Appearance of Non-Binary Digits
    if invalid_digits:
        print("The Numbers", invalid_digits,"Are Not 0s nor 1s. Try Another Input")
        return
    
    ## CONVERSION

    decimal = binary_to_decimal(cleaned_binary)

    ## OUTPUT

    print(f"The decimal equivalent of {binary_input} is {decimal}")

if __name__ == "__main__":
    main()