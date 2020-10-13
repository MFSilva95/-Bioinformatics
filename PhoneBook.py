####################################################################################################################
###                                    Algorithms for Bioinformatics
###                                 ***  class Phone Book              ***    
###
### Test number: 4      Class Number: 3         Date:   17 to 21 February 2020
###
### Group
### Student: ....               Number:...
### Student: ....               Number:...
###
####################################################################################################################
### Complete the code below for the object PhoneBook
### In main give example on how to create, update, insert and use object PhoneBook
### Explain in comments how the data will be organized
##trab2
class PhoneBook:
    ''' Implements a Phone Book '''
    
    def __init__(self):
        ''' initializes phone book with appropriate data structure '''
        # complete
        # DONE
        self.contacts =[]
        
        
    def add_phone(self, name, number):
        # complete
        # DONE
        self.contacts.append((name,number))
    
    # add the remaining methods here
    #DONE
    def search_by_name(self,NameToSearch):
        for name, number in self.contacts:
            if(NameToSearch==name):
               print(f'{name}:{number}')
    
    def search_by_number(self,NumberToSearch):
        for name, number in self.contacts:
            if(NumberToSearch==number):
                print(f'{name}:{number}')
    
    def print_phonebook(self):
        print("PhoneBook:")
        for name,number in self.contacts:
            print(f'{name}:{number}')
                
    def copy_phonebook(self):
        p2 = PhoneBook()
        for name,number in self.contacts:
            p2.add_phone(name,number)  
        return p2

class Email(PhoneBook):
    def add_mail(self, name, email):
        self.add_phone(name,email)   
  
if __name__ == "__main__":
    ''' test code here '''
    # complete
    # DONE
    ###TESTES###
            ##teste PhoneBook
    p1 =PhoneBook()
    p3 = Email()
    p1.add_phone("ANA1","1923")
    p1.add_phone("ANA2","2923")
    p1.add_phone("ANA3","3923")
    p1.add_phone("ANA4","4923")
    p1.add_phone("ANA5","5923")
    p1.add_phone("ANA6","6923")
    
    p1.search_by_name("ANA1")
    p1.search_by_number("3923")

    p1.print_phonebook()
    p4 = p1.copy_phonebook()
    p4.print_phonebook()
            ##teste EMAIL
    print("EMAIL:")
    p3.add_mail("ANA1","asdb@fc.up.pt")
    p3.add_mail("ANA2","dnjasnfdja@fc.up.pt")
    p3.add_mail("ANA3","hsa@fc.up.pt")
    
    p3.search_by_name("ANA1")

    p3.search_by_number("hsa@fc.up.pt")
    p3.print_phonebook()
    p5 = p3.copy_phonebook()
    p5.print_phonebook()
   