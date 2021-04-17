from a1_CS19037_3 import Product
from a1_CS19037_5 import ProductDB
from a1_CS19037_2 import Cart
from a1_CS19037_1 import AccountDB
from a1_CS19037_4 import User

############ Interface ###############

while True:
    print("*********************")
    print("Welcome to online shopping mart")
    print("""Enter 1 to create account
Enter 2 to access account
Enter 3 to exit
**********************
    """)
    user_input = input(": ")
    if user_input == "3":
        print("See you next time. BYE:))")
        break
    elif user_input == "1":
        user = User()
        user.newUser()
        print("Your new account has been saved with the credentials:")
        user.showUser()
        user.saveUser()
        continue

    elif user_input == "2":
        username = input("Enter the correct unique username of you account: ")
        user = User()
        user.loadUser(username)
        if not user.userinfo:
            continue
        else:
            entered_password = input("Enter correct password: ")
            if entered_password != user.userinfo[1]:
                print("Incorrect password")
                continue
            else:
                print("Account access granted, Now you can do shopping:)")

        while True:
            print("<><><><><><><><><><><><><><><><><><><><><><><><>")
            print("Enter 1 to view products")
            print("Enter 2 to add products to cart")
            print("Enter 3 to view cart")
            print("Enter 4 to remove products from cart")
            print("Enter 5 to view shopping history if you have been here before")
            print("Enter 6 to checkout")
            print("Enter 7 to logout")
            print("<><><><><><><><><><><><><><><><><><><><><><><><>")

            user_input2 = input("==> ")

            if user_input2 == "7":
                print("You have now logged out of your account")
                break

            elif user_input2 == "1":
                cart = Cart(user)
                cart.showProducts()

            elif user_input2 == "2":
                cart = Cart(user)
                while True:
                    print("Do you want to add somthing to your cart? (y/n): ")
                    user_response = input(": ")
                    if user_response == "y":
                        product_name = input("Enter exact name of product: ")
                        quantity = int(input("Enter quantity of product: "))
                        cart.addToCart(product_name, quantity)
                        continue

                    elif user_response == "n":
                        break


            elif user_input2 == "3":
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                try:
                    cart.viewCart()
                except:
                    print("Cannot view cart before shopping")


            elif user_input2 == "4":
                while True:
                    user_response1 = input("Do you want to remove something from your cart? (y/n): ")
                    if user_response1 == "y":
                        remove_product = input("Enter exact name of product: ")
                        cart.removeFromCart(remove_product)
                        continue

                    elif user_response1 == "n":
                        break


            elif user_input2 == "5":
                previous_cart = Cart(user)
                print("<<Your shopping history is shown below in sequence from oldest to latest>>")
                previous_cart.previousCart(user)

            elif user_input2 == "6":
                print(f"Your bill is {cart.calculateBill()}Rs ")
                print("Your cart is saved in history")
                print(f"Hope to see you soon {user.username}. BYE:))")
                print(">>>>>>>>>>>>>>><<<<<<<<<<<<<<<")
                cart.saveCartToFile()

    else:
        print("OOPS!! You entered the wrong key.")
        continue



