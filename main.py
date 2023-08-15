# Problem 1: Write a lambda function to sort a list of tuples in ascending order according to the number in the second position of each tuple.
grades = [("English", 88), ("Science", 90), ("Math", 97), ("Social Sciences", 82)]
sorted_grades = sorted(grades, key = lambda x: x[1])
print(sorted_grades)

# Problem 2: Write a Lambda Function to cube every element of a list.
## Original list: [3, 6, 9, 2]
## List after Lambda Function: [27, 216, 729, 8]
cubed = lambda x: [i**3 for i in x]
print(cubed([3, 6, 9, 2]))

# Problem 3: Write a lambda function to determine whether a number is even or odd (the function should return True or False), and then use the function and a list comprehension to create a new list of booleans, where even numbers are True and odd numbers are False.
## Input List: [3, 6, 9, 2]
## List after Lambda Function and list comprehension: [False, True, False, True]
even_odd = lambda x: True if x%2 == 0 else False
print([even_odd(x) for x in [3, 6, 9, 2]])

# Problem 4: Use a list comprehension to create a list of the numbers from 1 to 100 (including 100).
nums = [i for i in range(1, 101)]
print(nums)

# Problem 5: Use a dictionary comprehension to count the length of each word in a sentence.
## Input: "The quick brown fox jumped over the fence." output: {'The': 3, 'quick': 5, 'brown': 5, 'fox': 3, 'jumped': 6, 'over': 4, 'the': 3, 'fence.': 6}
sent = "The quick brown fox jumped over the fence."
print ({word:len(word) for word in sent.split()})