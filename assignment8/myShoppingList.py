

class MyShoppingList:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        print(f"Added {quantity} of {item} to the shopping list.")

    def __iter__(self):
        return iter(self.items.items())

    def __next__(self):
        if self.index < len(self.items):
            item = list(self.items.items())[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration
        
if __name__ == "__main__":
    shopping_list = MyShoppingList()
    shopping_list.add_item("apple", 5)
    shopping_list.add_item("banana", 3)
    shopping_list.add_item("orange", 2)

    for product in shopping_list:
        print(f"{product[0]}: {product[1]} units")
    