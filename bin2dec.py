def bin2dec(binary_str):
    """
    Convert a binary string (up to 8 digits of 1's or 0's) to decimal integer.
    
    Args:
        binary_str (str): A string containing only 0's and 1's (max 8 digits)
    
    Returns:
        int: The decimal representation of the binary string
    
    Raises:
        ValueError: If input is invalid (not binary digits or more than 8 digits)
    """
    # Validate input is a string
    if not isinstance(binary_str, str):
        raise ValueError("Input must be a string")
    
    # Remove any whitespace
    binary_str = binary_str.strip()
    
    # Check if empty
    if not binary_str:
        raise ValueError("Input cannot be empty")
    
    # Check length (max 8 digits)
    if len(binary_str) > 8:
        raise ValueError("Binary string cannot be longer than 8 digits")
    
    # Validate that all characters are 0 or 1
    if not all(c in '01' for c in binary_str):
        raise ValueError("Input must contain only 0's and 1's")
    
    # Convert binary to decimal
    decimal_value = 0
    for i, bit in enumerate(reversed(binary_str)):
        if bit == '1':
            decimal_value += 2 ** i
    
    return decimal_value
