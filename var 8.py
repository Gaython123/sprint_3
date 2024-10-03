class Good:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"'{self.name}',"\
               f" in quantity of '{self.quantity}' items,"\
               f" for price of '{self.price}' each"

    def display(self):
        print(f"{self.name}: {self.quantity} items for '{self.price}' euro per each")

    def value_of_product(self):
        print(f"The total sum of '{self.name}' is '{self.quantity * self.price}' euros")

pencil = Good("pencilSun", 7, 40)
pencil.display()
pencil.value_of_product()