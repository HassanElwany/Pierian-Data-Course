# Write a function that computes the volume of a sphere given its radius.
from math import pi
def vol(rad):
  return (4/3) * pi * (rad ** 3) 
print(vol(2))
print("########################################################")
# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num, low,high):
  return num in range(low, high+1)
print(ran_check(7,2,7))
print("########################################################")
# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
  lower_letter = 0
  upper_letter = 0
  for letter in s:
    if letter.isupper():
      upper_letter += 1
    elif letter.islower():
      lower_letter += 1
  print(f'No. of Upper case characters: {upper_letter}')
  print(f'No. of Lower case Characters: {lower_letter}')
up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
print("########################################################")
# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
  #convert the list to set
  list_set = set(lst)
  # re-convert the set to list
  unique_list = list(list_set)
  print(unique_list)
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
print("########################################################")
# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
  total = 1
  for number in numbers:
    total *= number 
  return total
print(
multiply([1,2,3,-4]))
print("########################################################")
# Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(s):
  word = s.replace(' ', '')
  return word[::1] == word[::-1]
print(palindrome('nurses run'))
print("########################################################")
# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

def ispangram(str1):
  alphabet = list('abcdefghijklmnopqrstuvwxyz')
  word = str1.lower().replace(' ', '')
  new_word = list(word)
  # print(new_word)
  for letter in alphabet:
    return letter in new_word
#ispangram("The quick brown fox jumps over the lazy dog")
print(ispangram("The quick brown fox jumps over the lazy dog"))

