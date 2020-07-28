'''
  Name: Joshua Santillan
  Date: May 26th 2020
  Filename: main.py
  Description: Create a person class. Create a customer class that is a subclass of the Person class and write a program showing how it works~ Customer class should have its own attributes as well.
  Email: santj96@gmail.com
'''

class Person:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number
    def person_name(self):
        return self.name

    def person_attributes(self):
        return self.name, self.address, self.phone_number

class Customer(Person):
    def __init__(self, name, address, phone_number,customer_number,mail_bool):
        Person.__init__(self,name, address, phone_number)
        self.customer_number = customer_number
        self.mail_bool = mail_bool
   
    def customer_attributes(self):
        return self.name, self.address, self.phone_number, self.customer_number,self.mail_bool

x = Person("Spongebob", "Bikini Bottom","123-456-7890")
y = Customer("Squidward", "Bikini Bottom", "987-654-3210","01",True)


def main():
    print(x.name) #output spongebob
    print(x.person_attributes())

    print("\n")

    print(y.person_name()) # should output squidward using method from person class
    print(y.customer_attributes())

    #print(x.customer_attributes()) -> this will not work, x object is not a sublcass of customer but customer is a subclass of person.




if __name__ == "__main__":
    main()