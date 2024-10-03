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
        print(f"The total value of '{self.name}' is '{self.quantity * self.price}' euros")

pencil = Good("pencilSun", 7, 40)
pencil.display()
pencil.value_of_product()

class Good_(Good): #class Child(Parent) - вказуэмо у дужках батьківський клас)
    def __init__(self, name: str, price: float, quantity: int, supplier_name: str): #тут у атрибутах ми прописуэмо вcі атрибути (попередні та новий)

        #When you add the __init__() function WITHOUT SUPER() OR PARENT., the child class will no longer inherit the parent's __init__() function.

        super().__init__(name, price, quantity) #тут ми вказуэмо всі атрибути які беремо з батьківського класу.
        #не вказуємо новий атрибут який буде у нового класу
        self.supplier_name = supplier_name

    def display_good_and_supply(self):
        print(f"Company '{self.supplier_name}' creates {self.name}: {self.quantity} items for '{self.price}' euro per each")






pencil_2 = Good_("Graphit black", 40, 140, "FOP 'Nazarius'")
pencil_2.display()
pencil_2.display_good_and_supply()



