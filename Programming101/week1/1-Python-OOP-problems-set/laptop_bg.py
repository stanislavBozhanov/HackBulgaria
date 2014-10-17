class Product(object):            
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price
 
    def __str__(self):
        return self.name

    def profit(self):
        return self.final_price - self.stock_price


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, diskspace, ram):
        super().__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.ram = ram


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, screen_size, mega_px):
        super().__init__(name, stock_price, final_price)
        self.screen_size = screen_size
        self.mega_px = mega_px


class Store(object):
    def __init__(self, name):
        self.name = name
        self.products = {}
        self.income = 0

    def load_new_products(self, product, count):
        if product in self.products:
            self.products[product] += count
        else:
            self.products[product] = count

    def list_products(self, product_class):
        for product in self.products:
            if isinstance(product, product_class):
                print("{} - {}".format(product, self.products[product]))

    def sell_product(self, product):
        if product in self.products and self.products[product] > 0:
            self.products[product] -= 1
            self.income += product.profit()
            return True
        else:
            return False

    def total_income(self):
        return self.income

store = Store('Laptop.bg')
smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
smarthphone2 = Smartphone('Hack Phone Lqlql', 500, 820, 7, 10)
store.load_new_products(smarthphone, 2)
store.sell_product(smarthphone)  # True
store.sell_product(smarthphone2)  # True
print(store.total_income())  # 640
