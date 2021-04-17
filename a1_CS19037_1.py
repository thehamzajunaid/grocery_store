class AccountDB:

    def saveUser(self):
        f = open("a1_CS19037_AccountDB.txt", "a")
        f.write(str(self.userinfo)+'\n')
        f.close()

    def loadUser(self, username):
        self.username = username
        f = open("a1_CS19037_AccountDB.txt", "r")
        for line in f:
            if self.username == (eval(line))[0]:
                self.userinfo = eval(line)
                
            else:
                continue
        if not self.userinfo:
            print("No user found")
        f.close()

    
    
            
                       
        
