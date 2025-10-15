# bin2dec

A Python function that converts binary strings (up to 8 binary digits) to decimal integers.

## Usage

```python
from bin2dec import bin2dec

# Convert binary to decimal
result = bin2dec('101')      # Returns: 5
result = bin2dec('11111111') # Returns: 255
result = bin2dec('10')       # Returns: 2
```

## Function Signature

```python
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
```

## Input Requirements

- Input must be a string
- String can only contain characters '0' and '1'
- Maximum length is 8 digits
- Leading/trailing whitespace is automatically stripped

## Examples

```python
bin2dec('0')         # 0
bin2dec('1')         # 1
bin2dec('10')        # 2
bin2dec('101')       # 5
bin2dec('11111111')  # 255 (maximum value for 8 bits)
bin2dec('10101010')  # 170

# Whitespace is handled
bin2dec(' 101 ')     # 5
```

## Error Handling

The function raises `ValueError` for invalid inputs:

```python
bin2dec('111111111')  # ValueError: Binary string cannot be longer than 8 digits
bin2dec('abc')        # ValueError: Input must contain only 0's and 1's
bin2dec('102')        # ValueError: Input must contain only 0's and 1's
bin2dec('')           # ValueError: Input cannot be empty
```

## Running Tests

Run the test suite using Python's unittest:

```bash
python -m unittest test_bin2dec.py -v
```