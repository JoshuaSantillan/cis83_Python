'''
  Name: Joshua Santillan
  Date: March 18th 2020
  Filename: main.pu
  Description: Bug class that moves/turns
  Email: santj96@gmail.com
'''
class bug:

  def __init__(self,initialPosition):
    self.initialPosition = initialPosition
    direction = 1
    self.direction = direction
  
  def move(self):
    self.initialPosition += self.direction
   
  def turn(self):
    self.direction *=-1
  def getPosition(self):
    print(self.initialPosition)

bugsy = bug(10) # start 10
bugsy.move() # 11
bugsy.move() # 12 
bugsy.turn() # direction is now -1
bugsy.move() # 12 + (-1)

bugsy.getPosition() # output is now 11
