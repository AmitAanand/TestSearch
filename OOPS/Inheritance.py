#
#   Inheritance   /  Overriding
#

class Father():

    car="Fararri"
    bank_banace=1000000

    @staticmethod
    def business():
        return "Basic Balance"

    #Overrinding
    def to_marry(self):
        print("Priyanka")

#Inheritance
class Son(Father):

    # Overrinding
    def to_marry(self):
        print("Kriti")



f=Father()
print(f.bank_banace)
print(f.business())
f.to_marry()

s=Son()
print(f.bank_banace)
print(f.business())
s.to_marry()