# Create a function that gets a number as parameter, and then prints the multiplication table for that number from 1 to 10. E.g., when the parameter is 12, 
# the first line printed is “1 * 12 = 12” and the last line printed is “10 * 12 = 120.”

'''def mutiplication_table(number):
    print('Multiplication Table for', number )
    for i in range(1, 11):
        product = i * number
        print(f'{number} * {i} = {product}')

mutiplication_table(10)'''




'''def addition_table(number):
    print(f"Addition Table for {number}:")
    print("Number  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10")
    print("-" * 66)
    
    for i in range(1, 11):
        result = number + i
        print(f"   {number}    | {result:2}  | {result+1:2}  | {result+2:2}  | {result+3:2}  | {result+4:2}  | {result+5:2}  | {result+6:2}  | {result+7:2}  | {result+8:2}  | {result+9:2}")

print(addition_table(8))
'''

# Write a function that gets as parameters two strings. The function returns the number of characters that the strings have in common. Each character counts 
# only once, e.g., the strings "bee" and "peer" only have one character in common (the letter “e”). You can consider capitals different from lower case letters.
#  Note: the function should return the number of characters that the strings have in common, and not print it. To test the function,
# you can print the result in your main program.

'''def same_characters(word1, word2):
    set_1 = set(word1)
    set_2 = set(word2)

    i = 0
    for l in set_1:
        if l in set_2:
            i+=1
    return i

one = 'happy'
two = 'happiness'
common= same_characters(one, two)
print(common)'''


# OR

'''
def common_character_count(str1, str2):
    # Convert strings to sets to get unique characters
    set1 = set(str1)
    set2 = set(str2)
    
    # Find the common characters by taking the intersection of the sets
    common_chars = set1 & set2
    
    # Return the count of common characters
    return len(common_chars)

# Example usage
string1 = "happy"
string2 = "happiness"
result = common_character_count(string1, string2)
print(f"The number of common characters is: {result}")

'''



# THIS CODE PRINTS THE NUMBER OF CHARATERS APPEARING IN A STRING INTO A DICTIONARY 

'''def count_characters(input_string):
    char_count = {}  # Initialize an empty dictionary to store character counts
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

input_string = "hello"
character_counts = count_characters(input_string)
print(character_counts)'''

# THIS PROGRAM COUNTS EVEN NUMBERS IN A LIST

'''def count_even(list_numbers):
    i = 0
    for num in list_numbers:
        if num % 2 == 0:
            i += 1
    return i

numbers = [2,4,7,1,44,66,87,99,10,12,43,54,68]
even_counts = count_even(numbers)
print(even_counts)
'''

# THIS PROGRAM PRINTS EVEN NUMBERS IN A LIST
'''
def get_even(list_numbers):
    even = []
    for num in list_numbers:
        if num % 2 == 0:
            even.append(num)
    return even

numbers = [2,4,7,1,44,66,87,99,10,12,43,54,68]
even_prints = get_even(numbers)
print(even_prints)
'''

def isEven(num):
    even = num %2 == 0
    return even
    
for n in range(20):
    if isEven(n):
        print(n, 'is an even number')











