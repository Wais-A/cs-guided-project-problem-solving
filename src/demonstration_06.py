"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    # Your code here
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in input_str.lower():
        for letter in vowels:
            if i == letter:
                count +=1
    return count

print(get_count("Hello my name is Wais Almakaleh"))