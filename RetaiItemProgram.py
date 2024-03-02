import RetailItemClass as r 

item1 = r.RetailItem('Jacket', 12, 59.95)
item2 = r.RetailItem('Designer Jeans', 40, 34.95)
item3 = r.RetailItem('Shirt',20, 24.95)

print(f"{item1.item_description}, {item1.units_in_inventory}, ${item1.price}")
print(f"{item2.item_description}, {item2.units_in_inventory}, ${item2.price}")
print(f"{item3.item_description}, {item3.units_in_inventory}, ${item3.price}")