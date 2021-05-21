class book:
    _score = 0

    def __init__(self):
        self._score = 100

    def get_price(self):
        return self._score

    def set_price(self,price):
        if not isinstance(price, int):
            raise ValueError('price must be an integer!')
        if price < 0 :
            raise ValueError('price must > 0 !')
        self._score = price

b = book()
b.set_price(100)
print("book`s price is :",b.get_price())



class book:
    _score = 0

    def __init__(self):
        self._score = 100

    @property
    def price(self):
        return self._score

    @price.setter
    def price(self,price):
        if not isinstance(price, int):
            raise ValueError('price must be an integer!')
        if price < 0 :
            raise ValueError('price must > 0 !')
        self._score = price

b = book()
b.price = 100
print("book`s price is :",b.price)