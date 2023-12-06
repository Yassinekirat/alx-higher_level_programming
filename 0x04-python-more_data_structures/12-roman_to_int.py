#!/usr/bin/python3
def roman_to_int(roman_string):
	roman_letters = {"I": 1, "V": 5, "X": 10, "L": 50,
					 "C": 100, "D": 500, "M": 1000}
	result = 0
	for i in range(len(roman_string) - 1):
		current_value = roman_letters[roman_string[i]]
		next_value = roman_letters[roman_string[i + 1]]
		if current_value < next_value:
			result -= current_value
		else:
			result += current_value
	result += roman_letters[roman_string[-1]]
	return result
