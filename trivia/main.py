class Question: 
  '''
  student = {1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
           2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}}
 '''
  def __init__(self):
      ask = ""
      l1 = []
      self.ask = ask
      self.l1 = l1
  def questions(self):
    print("Question #1")
    l1 = ["1.","2.","3."]
    ans = l1[2]
    for i in l1:
      print(i)
    x = input("Pick an answer:")
    if(x == ans):
      print("Correct")
    else:
      print("wrong")

      ## try a dictionary, look up keys, and try to organize a class with a lot of functions to call from. 


q1 = Question()
q1.questions()
