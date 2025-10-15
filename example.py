#!/usr/bin/env python3
"""
Example usage of the bin2dec function
"""

from bin2dec import bin2dec


def main():
    """Demonstrate the bin2dec function with various examples"""
    print("Binary to Decimal Converter")
    print("=" * 50)
    print()
    
    # Example conversions
    examples = [
        '0',
        '1',
        '10',
        '11',
        '100',
        '101',
        '1000',
        '1111',
        '10101010',
        '11111111',
    ]
    
    print("Example conversions:")
    print("-" * 50)
    for binary in examples:
        decimal = bin2dec(binary)
        print(f"Binary: {binary:>8}  =>  Decimal: {decimal:>3}")
    
    print()
    print("-" * 50)
    print()
    
    # Interactive mode
    print("Try your own conversions (or 'q' to quit):")
    while True:
        try:
            user_input = input("Enter binary string (up to 8 digits): ").strip()
            
            if user_input.lower() in ['q', 'quit', 'exit']:
                print("Goodbye!")
                break
            
            if not user_input:
                continue
            
            result = bin2dec(user_input)
            print(f"  => Decimal: {result}")
            print()
            
        except ValueError as e:
            print(f"  Error: {e}")
            print()
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == '__main__':
    main()
