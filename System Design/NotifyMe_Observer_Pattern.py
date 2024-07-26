# Observer Design Pattern for NotifyMe Function on websites Like Flipkart,Amazon etc..

# Classes Used -
    # User Class : For Creating Users.
    # Product Class : Creating Products for Notifyme functionality
    # NotifyMe Class : Abstract Class for Declaring functionality like Notify(), add_notify_users(), remove_notify_users()


from abc import ABC, abstractmethod

class User:
    # def __new__(cls, *args, **kwargs):
    #     return super(User, cls).__new__(cls)
    
    def __init__(self,Firstname,Lastname,Email,Phone):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.Email = Email
        self.Phone = Phone
        
    def update_Firstname(self,New_Firstname):
        self.Firstname = New_Firstname
        
    def update_Lastname(self,New_Lastname):
        self.Lastname = New_Lastname
        
    def update_delete_Email(self,Email=None,Operation="update"):
        match Operation.lower():
            case "update":
                self.Email = Email
                return
            case "delete":
                self.Email = None
                return
            case default:
                print("Operation is invalid!! Please select appropriate Operation")
                return
            
    def update_delete_Phone(self,Phone=None,Operation="update"):
        match Operation.lower():
            case "update":
                self.Phone = Phone
                return
            case "delete":
                self.Phone = None
                return
            case default:
                print("Operation is invalid!! Please select appropriate Operation")
                return
            
    
class NotifyMe(ABC):
    
    @abstractmethod
    def notify(self):
        pass    
    
    @abstractmethod
    def add_notify_user(self,*args,**kwargs):
        pass
    
    @abstractmethod
    def remove_notify_user(self,*args):
        pass
            
            
class Product(NotifyMe):
    def __init__(self,Name,Type,Stock):
        self.Name = Name
        self.Type = Type
        self.Stock = Stock
        self.Observers = {}
        
    def add_stock(self,Stockcount):
        if self.Stock == 0:
            self.Stock = Stockcount
            self.notify()
        else:
            self.Stock += Stockcount
            
    def subtract_stock(self,Purchasedstock):
        if self.Stock == 0:
            print(f"Product {self.Name} is out of Stock!!")
            return
        elif self.Stock - Purchasedstock < 0:
            print(f"cannot But this Product {self.Name}. Stock remaining is {self.Stock}")
            return
        else:
            self.Stock -= Purchasedstock  
            print(f"Remaining Stock for Product {self.Name} is {self.Stock}")       
         
    def add_notify_user(self,user,notify_preference):
        if notify_preference.lower() != "email" and notify_preference.lower() != "phone":
            print(f"Invalid Notify Preferences for User {user.Firstname} {user.Lastname}. Please add again.")
            return
        self.Observers[user] = notify_preference
        
    def remove_notify_user(self,user):
        del self.Observers[user]
        print(f"{user.Firstname} {user.Lastname} removed successfully for Product {self.Name}")
    
            
    def notify(self):
        for user,pref in self.Observers.items():
            if pref.lower() == "email":
                print(f"Email notification sent Successfully for Product {self.Name} to {user.Firstname} {user.Lastname} on Email: {user.Email}. Total Stock added: {self.Stock}")
            else:
                print(f"Phone notification sent Successfully for Product {self.Name} to {user.Firstname} {user.Lastname} on Phone: {user.Phone}. Total Stock added: {self.Stock}")
        
    
if __name__ == "__main__":      
    John = User(Firstname="John",Lastname="Carter",Email="John.carter@xyz.com",Phone="+911000000000")
    Tony = User(Firstname="Tony",Lastname="Stark",Email="Tony.stark@xyz.com",Phone="+911000000011")
    Chris = User(Firstname="Chris",Lastname="Evans",Email="Chris.evans@xyz.com",Phone="+911000000022")
    Rocket = User(Firstname="Rocket",Lastname="Chat",Email="Rocket.chat@xyz.com",Phone="+911000000033")

    Realme = Product(Name="Realme Narzo", Type="Mobile", Stock=20)
    Msi = Product(Name="Msi Gaming Laptop", Type="Laptop", Stock=10)

    Realme.add_notify_user(user=John,notify_preference="Email")
    Realme.add_notify_user(user=Chris,notify_preference="Email")
    Msi.add_notify_user(user=Tony,notify_preference="Email")
    Msi.add_notify_user(user=Rocket,notify_preference="Phone")
    

    Realme.subtract_stock(20)
    Realme.subtract_stock(5)
    Realme.add_stock(25)

    print()
    Msi.remove_notify_user(user=Rocket)
    Msi.subtract_stock(5)
    Msi.subtract_stock(7)
    Msi.subtract_stock(5)
    Msi.add_stock(15)




            
          
        
    