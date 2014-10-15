class Product(object):
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price

new_product = Product('HP HackBook', 1000, 1243)
print(new_product.profit())
