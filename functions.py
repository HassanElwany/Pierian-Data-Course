def lesser_of_two_evens(a, b):
  if a % 2 == 0 and b % 2 == 0:
    return min(a,b)
  else:
    return max(a,b)
print(lesser_of_two_evens(2,5))
print ("##############################################################")

def animal_crackers(text):
  word, the_word = text.split(' ')
  return word[0] == the_word[0] 
result0 = animal_crackers('Crazy Cangaroo')
print(result0)
print ("##############################################################")

def makes_twenty(num1, num2):
  return num1 == 20 or num2 == 20  or (num1 + num2) == 20
result = makes_twenty(2, 18)
print(f'hi {result}')
print ("##############################################################")

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
  return name[0:3].capitalize() + name[3:].capitalize()
result1 = old_macdonald('macdonald')
print(result1)
print ("##############################################################")

# MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(text):
  return text.split(' ')[::-1]
  
result2 = master_yoda('I am home')
print(result2)

print ("##############################################################")

# Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
  if int(n) in range(90, 110) or  int(n) in range(190, 210):
    return abs(n)
  else:
    print('check the num')
result3 = almost_there(150)
print(result3)

print ("##############################################################")

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
  if any( nums[i] == nums[i + 1] == 3  for i in range(len(nums) - 1)):
    return True
  return False
result4 = has_33([3,2,3])
print(result4)

print ("##############################################################")

# Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
 return ''.join([i * 3 for i in text])  
print(paper_doll('Hello'))

print ("##############################################################")

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
  if any (nums[i] == nums[i + 1] == 0 and nums[i + 2] == 7 for i in range(len(nums) - 1) ):
    return True
  return False
print(spy_game([1,0,2,4,0,5,7]))

print ("##############################################################")

def myfunc(word):
    result = ""
    index = 0
    for letter in word:
        if index % 2 == 0:
            result += letter.lower()
        else:
            result += letter.upper()
        index += 1
    return result
print(myfunc('Anthropomorphism'))

