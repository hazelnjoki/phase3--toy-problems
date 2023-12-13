def solve(word):
    vowels = "aeiou"
    consonant_values = {letter: ord(letter) - ord('a') + 1 for letter in 'abcdefghijklmnopqrstuvwxyz' if letter not in vowels}

    def get_consonant_value(substring):
        return sum(consonant_values[letter] for letter in substring)

    max_consonant_value = 0
    current_consonant_substring = ""

    for char in word:
        if char not in vowels:
            current_consonant_substring += char
        else:
            max_consonant_value = max(max_consonant_value, get_consonant_value(current_consonant_substring))
            current_consonant_substring = ""

    # Check the last substring if the word ends with a consonant
    max_consonant_value = max(max_consonant_value, get_consonant_value(current_consonant_substring))

    return max_consonant_value

# Examples:
result1 = solve("zodiacs")
result2 = solve("strength")

print(result1)  # Output: 26
print(result2)  # Output: 57
