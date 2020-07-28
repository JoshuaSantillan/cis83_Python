## Name: Joshua Santillan
## Date: 3/1/20
## Email: santillanj125821@student.vvc.edu
## Class: cis83 spr-2020
## Description: Capitalizing every word after proper puncation. using split and captialize function


def string_cap(s):
  s1 = s.split()
  s1 = [i.capitalize() for i in s1]
  s2 = ' '.join(s1)
  print(s2)


hardcode = "Hello. how are you today? good weather we are having! "
string_cap(hardcode)



ask = input("Type a string!\n")
string_cap(ask)