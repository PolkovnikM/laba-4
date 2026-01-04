print(" 3. ИТЕРАТОР: Инвентарь игрока")


class InventoryItem:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

    def __str__(self):
        return f"{self.name} ({self.type}): {self.value} золота"


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            return item
        raise StopIteration()


inventory = Inventory()
inventory.add_item(InventoryItem("Меч дракона", "оружие", 500))
inventory.add_item(InventoryItem("Зелье здоровья", "зелье", 50))
inventory.add_item(InventoryItem("Кольцо маны", "аксессуар", 200))
inventory.add_item(InventoryItem("Кожаный доспех", "броня", 100))

print("Содержимое инвентаря:")
for i, item in enumerate(inventory, 1):
    print(f"{i}. {item}")
