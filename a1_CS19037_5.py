

class ProductDB:
    products = []
    def loadProducts(self):
        with open("a1_CS19037_ProductDB.txt", "r") as f:
            for line in f:
                line = eval(line)
                ProductDB.products.append(line)

    def showProducts(self):
        for i in range(len(ProductDB.products)):
            print("Name: {} \nPrice: {} ".format(ProductDB.products[i][0],\
                                              ProductDB.products[i][1]))

                
            
# p = ProductDB()
# p.loadProducts()
# p.showProducts()
# print(ProductDB.products)
