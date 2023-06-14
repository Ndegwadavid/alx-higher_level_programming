#!/usr/bin/python3
def roman_to_int(roman_string):
    # Check if input is a string or None
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    prev_value = 0
    curr_value = 0
    for char in roman_string[::-1]:
        curr_value = roman_numerals[char]
        if curr_value < prev_value:
            curr_value *= -1
        prev_value = curr_value + prev_value
    
    return prev_value
