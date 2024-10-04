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
        #print(f"The total value of '{self.name}' is '{self.quantity * self.price}' euros")
        return self.price * self.quantity

#pencil = Good("pencilSun", 7, 40)
#pencil.display()
#pencil.value_of_product()

class Good_(Good): #class Child(Parent) - вказуэмо у дужках батьківський клас)
    def __init__(self, name: str, price: float, quantity: int, supplier_name: str) : #тут у атрибутах ми прописуэмо вcі атрибути (попередні та новий)

        #When you add the __init__() function WITHOUT SUPER() OR PARENT., the child class will no longer inherit the parent's __init__() function.

        super().__init__(name, price, quantity) #тут ми вказуэмо всі атрибути які беремо з батьківського класу.
        #не вказуємо новий атрибут який буде у нового класу
        self.supplier_name = supplier_name

    def display_good_and_supply(self):
        print(f"Company '{self.supplier_name}' creates {self.name}: {self.quantity} items for '{self.price}' euro per each")

    def increase_price(self, percentage_of_increasing: float):
        self.price += self.price * percentage_of_increasing/100
        return f"{self.price}"

class Storage:
    def __init__(self):
        self.storage = []

    def __str__(self):
        return f"{self.storage}"

    def add_good(self, good: Good_):
        if good.name in self.storage:
            return

        self.storage.append(good)

    def show_storage(self):
        for good in self.storage:
            print(f"\n {good} \n")

    def total_price(self):
        supplier_total = {}
        for good in self.storage:
            if good.supplier_name in self.storage:
                supplier_total[good.supplier_name] += good.value_of_product()
            else:
                supplier_total[good.supplier_name] = good.value_of_product()

        return supplier_total

pencil_2= Good_("Graphit black", 40, 140, "FOP 'Nazarius'")
pencil_2.value_of_product()

pencil_2.increase_price(15)
pencil_2.value_of_product()

pen = Good_("Pider_Pen", 20, 38, "Epicenter")
pencil_box = Good_("boxer_sex", 17.5, 30, "Calvin Klose")
scissors = Good_("Cutty-Cutty", 2.3, 25, "Bez_Pipisky")
pen_2 = Good_("Pider_Pen", 201, 380, "Epicenter")
pencil_box_2 = Good_("boxer_sex", 120, 306, "Calvin Klose")
scissors_2 = Good_("Cutty-Cutty", 4, 50, "Bez_Pipisky")

new_storage = Storage()
new_storage.add_good(pencil_2)
new_storage.add_good(pen)
new_storage.add_good(scissors)
new_storage.show_storage()

new_storage.total_price()
print(new_storage.total_price())