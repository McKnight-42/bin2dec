## Binary to Decimal

**Bin2Dec** is a simple Python function taht converts a binary  8-digit number (base 2) to a decimal number (base 10).

This is done without using built in fucntions like `int(binary, 2)`


## Features
- Accepts binary input up to 8 digits (0s and 1s only)
- Validates input for invalid characters
- Displays the correct decimal (base-10) output
- Handles errors gracefully with descriptive messages
- Fully implemented using **manual binary arithmetic** and a single math function (`pow`)


## Example 
```bash
$ python bin2dec.py
Please enter a number of 1's and 0's up to 8 characters long: 101101
45
```