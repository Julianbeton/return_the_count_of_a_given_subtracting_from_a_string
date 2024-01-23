# Exercise 7: Return the count of a given substring from a string

# Write a program to find how many times substring “Emma” appears in the given string.

# Given:
# str_x = "Emma is good developer. Emma is a writer"

# Expected Output:
# Emma appeared 2 times

string = "Julian is a first year computer engineering student. Julian is very handsome person."
print('\033[1;32;40mThe sentence is "Julian is a first year computer engineering student. Julian is very handsome person."')

word_counter = string.count("Julian")
print('The word "Julian" appeared', word_counter, 'times')