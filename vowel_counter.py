def count_vowels(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    count = 0
    for char in string:
        if char.lower() in vowels:
            count+=1
    return count



# List comprehension way
# def count_vowels(string):
#     vowels = ('a', 'e', 'i', 'o', 'u')
#     return sum(1 for char in string if char.lower() in vowels)

print(count_vowels("Hello, world!"))