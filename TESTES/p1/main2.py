products = 'Apricot, Pineapple, Orange, Watermelon, Banana, Mutton, Pancake, Wafer, Vermicelli, Ham, Grape, Cherry, Water, Beef, Pea, Pomegranate, Grapefruit,   Mushroom'
products = products.replace(' ', '').split(',')
products
i = 0
while i < len(products):
    if products[i] == 'Pea':
        print(f"Горох на базе под индексом {products[i]}")
    else:
        print(f"Ребята, это не горох! Это {products[i]}")
    i += 1
