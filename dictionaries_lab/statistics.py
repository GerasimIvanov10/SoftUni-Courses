products = {}

command_input = input()
while command_input != "statistics":
    tokens = command_input.split(": ")
    product = tokens[0]
    quantity = int(tokens[1])
    command_input = input()
    if product not in products:
        products[product] = 0
    products[product] += quantity

print("Products in stock:")
for (product, quantity) in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")