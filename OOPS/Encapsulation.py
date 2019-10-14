#
#   Encapsulation
#

class Father():

    __car="Fararri"
    __bank_banace=1000000

    @staticmethod
    def __business():
        return "Basic Banance"

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
s.to_marry()