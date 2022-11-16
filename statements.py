
# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
new_list = [st.split(' ')]
#print(new_list)

for word in new_list:
  for letter in word:
    if letter[0] == 's':
      print(letter)

print ("##############################################################")
# Use range() to print all the even numbers from 0 to 10.

for num in range(11):
  if num % 2 == 0:
    print(num)

print ("##############################################################")
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

my_list = [ x for x in range(1, 51) if x % 3 == 0]
print(my_list)

print ("##############################################################")
# Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
my_st = st.split(' ')

for word in my_st:
  if len(word) % 2 == 0:
    print('even!')

print ("##############################################################")

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for num in range(1, 101):
  if num % 3 == 0  and num % 5 == 0:
    print('FizzBuzz')
  elif num % 5 == 0:
    print('Buzz')
  elif num % 3 == 0 :
    print('Fizz')
  else:
    print(num)

print ("##############################################################")
# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'

my_new = [x[0] for x in st.split(' ')]
print(my_new)
