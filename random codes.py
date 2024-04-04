# Write a Python function called calculate_average that takes in a list of numbers as an argument and returns the average (mean) of those numbers.
# The function should round the average to two decimal places. Test your function by calling it with a list of numbers [10, 20, 30, 40, 50] and
#  print the result.


def calculate_average(numbers):
        result = sum(numbers) / len(numbers)
        return round(result, 2)
    
x = [10, 20, 30, 40, 50]
average = calculate_average(x)
print(average)

# Write a Python program to calculate the sum of two numbers entered by the user. Take two numbers as input using the input() function, convert them 
# to integers, calculate their sum, and print the result.

num_1= int(input())
num_2 = int(input())
print(num_1 + num_2)

# OR 
num_1, num_2= map(int, input('enter 2 numbers of your choice: ').split())
print(num_1 + num_2)

# this program asks the user for their first and last name (2-5 inputs)
# And prints a statement about the user

first, last = input('enter two of your names: ').split(',')
print(f'Her name is {first} {last} of the house Dankudi')


# this program asks the user to enter multiple items 

items = [s for s in input().split(',')]
print('The items the user entered are:',' '.join(items))


# # this program asks for multiple inputs and converts them to integers
items = [int (s) for s in input().split(',')]
print (items)

items = list(map(int, input('enter 2 numbers of your choice: ').split()))



# Write a Python program that takes a list of numbers as input and prints the square of each number in the list. Take a list of numbers as input 
# using the input() function and convert them to integers. Use a for loop to iterate through the list and calculate the square of each number. 
# Print the result for each number on a separate line.

list_of_num = [int (s) for s in input('enter a list of numbers: ').split()]

for s in list_of_num:
    squared = s ** 2
    print(squared)

# # OR

def get_square(numbers):
    squared_list = []
    for s in numbers:
        power = s ** 2
        squared_list.append(power)
    return squared_list
    
print(get_square(list_of_num))

def get_square (numbers):
    new_list = [s for s in numbers if s ** 2]
    return new_list

print(get_square(list_of_num))
    

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]




def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)






















