from a1_CS19037_1 import AccountDB

class User(AccountDB):
    def __init__(self):
        self.userinfo = []
        
    
    def newUser(self):
        self.username = input("Enter a unique username: ")
        self.userinfo.append(self.username)
        self.password = input("Enter password: ")
        self.userinfo.append(self.password)
        self.firstname = input("Enter your first name: ")
        self.userinfo.append(self.firstname)
        self.lastname = input("Enter last name: ")
        self.userinfo.append(self.lastname)
        self.email = input("Enter an email address: ")
        self.userinfo.append(self.email)

    def showUser(self):
        if not self.userinfo:
            print("No user to show")
        else:
            print(f"Username is {self.userinfo[0]}\n\
Password is {self.userinfo[1]}\n\
First name is {self.userinfo[2]}\n\
Last name is {self.userinfo[3]} \n\
Email is {self.userinfo[4]}")

    
        
        
##u = User()
##u.loadUser("b1lal")
##u.showUser()
