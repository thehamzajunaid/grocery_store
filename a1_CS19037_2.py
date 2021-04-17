from a1_CS19037_5 import ProductDB
from a1_CS19037_1 import AccountDB
from a1_CS19037_4 import User
from a1_CS19037_3 import Product
import os

class Cart(ProductDB):   #should pass User object as argument

    def __init__(self, User):

        self.cart = [[User.username],[]]

    def showProducts(self):    # load products from ProductDB file
        ProductDB.loadProducts(self)
        ProductDB.showProducts(self)

    def addToCart(self, user_input, quantity):
        for i in range(len(super().products)):
            if user_input in super().products[i][0]:
                self.cart[1].append([user_input, super().products[i][1], quantity])

            else:
                continue
            

    def removeFromCart(self, user_input):  #pass the exact item name in string
        temp_list = 0
        for item in self.cart[1]:
            if user_input == item[0]:
                temp_list+=1
                self.cart[1].remove(item)
                print("Item removed")
                break
        if temp_list == 0:
            print("Item is not in cart")
        
            

    def saveCartToFile(self):
        with open("a1_CS19037_Cart2.txt", "a") as f:
            f.write(str(self.cart)+'\n')


    def previousCart(self, User):   # Pass the user object to check his previous cart
        with open("a1_CS19037_Cart2.txt", "r") as f:
            temp_user = 0
            previous_cart = []
            if os.stat("a1_CS19037_Cart2.txt").st_size == 0:
                print('File is empty')
            else:
                for line in f:
                    line = eval(line)
                    if User.username == line[0][0]:
                        temp_user+=1
                        previous_cart.append(line)
                        print(previous_cart[-1])


            if temp_user == 0:
                print("No previous Cart of this user")

    def viewCart(self):
        print("<<Products in Cart>>")
        for i in range(len(self.cart[1])):
            print(f"Product: {self.cart[1][i][0]} \nPrice: {self.cart[1][i][1]}Rs\n"
                  f"Quantity: {self.cart[1][i][2]}")



    def calculateBill(self):
        indivisual_prices = []
        for item in self.cart[1]:
            indivisual_prices.append(item[1])
            
        quantities = []
        for item in self.cart[1]:
            quantities.append(item[2])

        bill = []
        for num1, num2 in zip(indivisual_prices, quantities):
            bill.append(num1 * num2)
        
        return sum(bill)
                
        

        
##user = User()
##user.loadUser("urooj")
##cart = Cart(user)
##cart.showProducts()
##user_input = input("Enter exact name of product: ")
##q1 = int(input("Enter quantity: "))
##cart.addToCart(user_input, q1)
##user_input2 = input("Enter exact name of product: ")
##q2 = int(input("Enter quantity: "))
##cart.addToCart(user_input2, q2)
##print(cart.cart)
##user_input3 = input("Enter exact name of product: ")
##cart.removeFromCart(user_input3)
####print(cart.cart)
##cart.saveCartToFile()
##cart.previousCart(user)
##print(cart.calculateBill())
####print(cart.cart[1])
