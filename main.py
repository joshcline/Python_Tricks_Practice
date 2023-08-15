# Problem 1: Write a lambda function to sort a list of tuples in ascending order according to the number in the second position of each tuple.
grades = [("English", 88), ("Science", 90), ("Math", 97), ("Social Sciences", 82)]
sorted_grades = sorted(grades, key = lambda x: x[1])
print(sorted_grades)

# Problem 2: Write a Lambda Function to cube every element of a list.
## Original list: [3, 6, 9, 2]
## List after Lambda Function: [27, 216, 729, 8]
cubed = lambda x: [i**3 for i in x]
print(cubed([3, 6, 9, 2]))