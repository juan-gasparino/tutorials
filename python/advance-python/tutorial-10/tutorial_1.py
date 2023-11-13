import logging


class Product:

  def __init__(self):
    self.__name: str
    self.__category: str
    self.__shipping_weight: float
    self.__unit_price: int
    self.__tax_percent: float

  @property
  def name(self):
    return self.__name 

  @name.setter
  def name(self, value):
    if isinstance(value, str) and value != '' and value is not None:
      self.__name = value
    else:
      logging.error(f'name should be a str and be empty or a None value: {value} is not valid')

  @property
  def category(self):
    return self.__category 

  @category.setter
  def category(self, value):
    if isinstance(value, str) and value != '' and value is not None:
      self.__category = value
    else:
      logging.error(f'category should be a str and be empty or a None value: {value} is not valid')

  @property
  def shipping_weight(self):
    return self.__shipping_weight

  @shipping_weight.setter
  def shipping_weight(self, value):
    if isinstance(value, float) and value > 0.0:
      self.__shipping_weight = value
    else:
      logging.error(f'shipping_weight should be a float greather than 0.0: {value} is not valid')

  @property
  def unit_price(self):
    return self.__unit_price

  @unit_price.setter
  def unit_price(self, value):
    if isinstance(value, int) and value > 0:
      self.__unit_price = value
    else:
      logging.error(f'unit_price should be a int greather than 0: {value} is not valid')

  @property
  def tax_percent(self):
    return self.__tax_percent

  @tax_percent.setter
  def tax_percent(self, value):
    if isinstance(value, float) and value > 0.0:
      self.__tax_percent = value
    else:
      logging.error(f'tax_percent should be a float greather than 0.0: {value} is not valid')

  def __str__(self):
    return f'the product is: {self.__name}\
 with category: {self.__category} and shipping weight: {self.__shipping_weight}\
 price: {self.__unit_price + self.__unit_price*self.__tax_percent}'


class Order:

  def __init__(self):
    self.__products: list[Product] = []

  @property
  def products(self):
    return self.__products 

  def add_product(self, product: Product):
    if isinstance(product, Product):
      self.__products.append(product)
    else:
      logging.error(f'products should be a list[Product]: {product.__name} is not valid')

  def __str__(self):
    return f'the products you bought are the following: {[item.name for item in self.__products]}'

  def show_total_products(self):
    total_price = sum(item.unit_price + (item.unit_price * item.tax_percent) for item in self.__products)
    print(f'Products: {[item.name for item in self.__products]}\n' + 
    f'total price: {total_price}')


if __name__ == '__main__':

  prod1 = Product()
  prod1.name = 'Banana'
  prod1.category = 'Fruit'
  prod1.shipping_weight = 0.1
  prod1.unit_price = 100
  prod1.tax_percent = 0.21

  prod2 = Product()
  prod2.name = 'Apple'
  prod2.category = 'Fruit'
  prod2.shipping_weight = 0.1
  prod2.unit_price = 200
  prod2.tax_percent = 0.21

  prod3 = Product()
  prod3.name = 'Apple'
  prod3.category = 'Fruit'
  prod3.shipping_weight = 0.1
  prod3.unit_price = 200
  prod3.tax_percent = 0.21

  prod4 = Product()
  prod4.name = 'Apple'
  prod4.category = 'Fruit'
  prod4.shipping_weight = 0.1
  prod4.unit_price = 200
  prod4.tax_percent = 0.21

  prod5 = Product()
  prod5.name = 'Apple'
  prod5.category = 'Fruit'
  prod5.shipping_weight = 0.1
  prod5.unit_price = 200
  prod5.tax_percent = 0.21

  order = Order()
  order.add_product(prod1)
  order.add_product(prod2)
  order.add_product(prod3)
  order.add_product(prod4)
  order.add_product(prod5)
  order.show_total_products()