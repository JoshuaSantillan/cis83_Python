## Name: Joshua Santillan
## Date: 3/12/20
## Email: santillanj125821@student.vvc.edu
## Class: cis83 spr-2020
## Description: Fraction class using overloading functions and exeption handing to make sure denom != 0

class Fraction:
   def __init__(self,numerator,denominator):

      self.numerator = numerator

      self.denominator = denominator
      try:
        self.denominator = denominator
        if self.denominator == 0:
          raise ValueError('Denominator cannot be 0, Invalid rational number')
        del self
      except ValueError as excpt:
        print(excpt)



   def __add__(self,rhs):
      ## added a function where if the numerator/denominator are the same number print 1, else print the original value. 
      if(self.numerator*rhs.denominator + rhs.numerator*self.denominator == rhs.denominator*self.denominator):
          return 1
      elif(Fraction(self.numerator*rhs.denominator + rhs.numerator*self.denominator,
                      rhs.denominator*self.denominator ) !=1 ) :

          return Fraction(self.numerator*rhs.denominator + rhs.numerator*self.denominator,
                      rhs.denominator*self.denominator )
   

   def __sub__(self,rhs):
      if(self.numerator*rhs.denominator - rhs.numerator*self.denominator == rhs.denominator*self.denominator):
          return 1
      elif(Fraction(self.numerator*rhs.denominator - rhs.numerator*self.denominator,

                      rhs.denominator*self.denominator ) !=1 ) :

          return Fraction(self.numerator*rhs.denominator - rhs.numerator*self.denominator,
                      rhs.denominator*self.denominator )
    
   def __mul__(self,rhs):
      if(self.numerator*rhs.numerator == rhs.denominator*self.denominator):
          return 1
      else:
          return Fraction(self.numerator*rhs.numerator,
                      rhs.denominator*self.denominator )

   def __str__(self):

      return "{}/{}".format(self.numerator,self.denominator)



def main():
  a = Fraction(2,2)
  b = Fraction(2,2)
  c = a + b 
  d = a - b
  e = a * b
  print(c)
  print(d)
  print(e)

if __name__ == "__main__":

   main()