try:
  for i in ['a','b','c']:
    print(i**2)
except:
  print('Something wrong!')
  
print('#'*75)

x = 5
y = 0

try:
  z = x / y
except ZeroDivisionError:
  print('division can not able by zero')
finally:
  print('All Done')

def ask():
  while True:
    try:
      num = int(input("please give a number you want to square it: "))
      print(num **2) 
    except:
      print('Something went wrong!')
    break
ask()
