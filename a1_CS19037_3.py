class Product:
    products = []
    def __init__(self):
        self.productinfo = []

    def addProduct(self):
        self.name = input("Enter name of the product: ")
        self.price = input("Enter price of the product: ")
##        self.quantity = input("Enter quantity of the product: ")
        self.productinfo = [self.name, self.price]
        Product.products.append(self.productinfo)
        

    def addProducts(self, howmany):  #Preferable to use
                                    #as we can specify how many item do we want to add
        for i in range(int(howmany)): 
            self.addProduct()
        

    def saveProduct(self):
        with open("a1_CS19037_ProductDB.txt", "a") as f:
            f.write(str(self.productinfo)+'\n')

    def saveProducts(self):
        with open("a1_CS19037_ProductDB.txt", "a") as f:
            for i in range(len(Product.products)):
                f.write(str(Product.products[i])+ '\n')

##    def __str__(self):
##        return "Product name: {} \nPrice: {} \nQuantity: {}".format(self.productinfo[0],\
##                                                                    self.productinfo[1],\
##                                                                    self.productinfo[2])
##        
        
# p = Product()
# p.addProducts(10)
# p.saveProducts()

