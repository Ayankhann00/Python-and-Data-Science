#functions in python

def square(num):
    return num ** 2
    
square(2)
# Function to calculate the sum of two numbers
def add(a, b):
    return a + b
# Function to calculate the sum of a list of numbers
def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
# Function to check if a number is even
def is_even(num):
    return num % 2 == 0
# Function to find the maximum number in a list
def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num
#map function to apply a function to each item in a list

def square(num):
    return num**2

lists=[1,2,3,4,5]
print(list(map(square,lists)))

#instead of calling function square use lambda function 
lists=[1,2,3,4,5]
print(list(map(lambda num:num**2,lists)))

#filter function to filter items in a list based on a condition
lists=[1,2,3,4,5]
print(list(filter(lambda num:num%3==0,lists)))

s='My name is Ayan'
# Convert to lowercase
print(s.lower())
# Convert to uppercase
print(s.upper())
#split string into a list 
print(s.split())


#functions in dictionary

d={'key1': 'value1', 'key2': 'value2'}
print(d.keys())

print(d.values())

print(d.items())

#functions in lists

l = [1, 2, 3, 4, 5]

# Append an item to the list
l.append(6)
# Insert an item at a specific position
l.insert(0, 0)
# Remove an item from the list
l.remove(3)
# Pop an item from the list
l.pop()  # Removes the last item
# Sort the list
l.sort()
# Reverse the list
l.reverse()
