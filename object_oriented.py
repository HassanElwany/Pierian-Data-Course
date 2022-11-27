class Line():
  def __init__(self,coor1,coor2):
    self.coor1 = coor1
    self.coor2 = coor2

  def distance(self):
    x1,y1 = self.coor1
    x2,y2 = self.coor2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
  
  def slope(self):
    x1,y1 = self.coor1
    x2,y2 = self.coor2
    return (y2-y1) / (x2-x1)

coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())
print('#'*75)
class Cylinder:
  def __init__(self, height=1,radius=1):
    self.height = height
    self.radius = radius

  def volume(self):
    return self.height *3.14 * (self.radius)**2
  
  def surface_area(self):
    top = 3.14 * (self.radius**2)
    return (2*top) + (2*3.14*self.radius*self.height)
c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())
print('#'*75)
print('#'*75)
print('#'*75)
print('#'*75)

class Account():
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance
  
  def __str__(self):
    return f"Account owner: {self.owner} \nAccount balance: {self.balance}"
  
  def deposit(self, amount):
    self.balance += amount
    return f"Deposit Accepted amount of deposit is {amount} Total Balance is {self.balance}"
  
  def withdraw(self, amount):
    if amount < self.balance:
      self.balance -= amount
      return f"Withdrawal Accepted your current balance is {self.balance}"
    else:
      return "Your balance less than amount"

acct1 = Account('Jose',100)
print(acct1)
print(acct1.deposit(50))
print(acct1.withdraw(75))
print(acct1.withdraw(100))