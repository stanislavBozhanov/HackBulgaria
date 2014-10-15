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

    def load_new_products(self, product, count):
        if product in self.products:
            self.products[product] += count
        else:
            self.products[product] = count

    def list_products(self, product_class):
        for product in self.products:
            if isinstance(product, product_class):
                print("{} - {}".format(product, self.products[product]))


new_product = Product('HP HackBook', 1000, 1243)
new_laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
new_smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
new_store = Store('Laptop.bg')
new_store.load_new_products(new_smarthphone, 20)
new_store.list_products(Smartphone)
