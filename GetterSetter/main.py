from phone import Phone
from item import Item

item1 = Item("MyItem", 750)

# Setting an Attribute using a setter method
item1.name = "OtherItem"

# Getting an Attribute
print(item1.all_items)


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
phone1 = Phone("jscPhonev10", 500, 5, 1)

print(Item.all_items)