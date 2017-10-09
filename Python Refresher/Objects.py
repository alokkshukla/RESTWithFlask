# class LotteryPlayer:
#     def __init__(self,name):
#         self.name = name
#         self.numbers = (3,4)
#
#     def total(self):
#         self.total=sum(self.numbers)
#         return self.total
#
#
#
# print(LotteryPlayer("Rolf").total())

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def avg(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def go_to_school(cls):
        print("I go to school - class.")
        print("I'm {}".format(cls))

    @staticmethod
    def go_to_school():
        print("I go to school - static.")


anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(67)
print(anna.__dict__)
anna.go_to_school()
Student.go_to_school()


class Store2:
    def __init__(self, name):
        self.name = name
        self.items = []

    # You'll need 'name' as an argument to this method.
    # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.

    def add_item(self, name, price):
        self.items.append({'name': name, 'price': price})

    # Create a dictionary with keys name and price, and append that to self.items.

    def stock_price(self):
        # total  = 0
        # for item in self.items:
        #     total+=item['price']
        return sum([item['price'] for item in self.items])

        # Add together all item prices in self.items and return the total.


# store = Store("Tesla")
# store.add_item("A",980)
# store.add_item("B",970)
# print(store.__dict__)
# print(store.stock_price())


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return store.name + ", total stock price: " + str(store.stock_price())
