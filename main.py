def bin2dec(bin_str):
    if not all(c in '01' for c in bin_str):
        raise ValueError("Not all provided values were 0's or 1's.")
    
    if len(bin_str) > 8:
        raise ValueError("Binary string must be 8 digits or less.")
    
    decimal = 0
    length = len(bin_str)

    for i, digit in enumerate(bin_str):
        decimal += int(digit) * pow(2, (length - 1 - i))


    return decimal

user_input = str(input("Please enter a number of 1's and 0's up to 8 characters long: "))
print(bin2dec(user_input))


