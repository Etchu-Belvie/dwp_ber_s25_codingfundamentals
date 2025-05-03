# Shopping List 
print("\n# Shopping List")

shopping_items = []
shopping = True

while shopping:
    shopping_item = input("Enter an Item ('done' to finish): ")
    if shopping_item.lower() == "done":
         break
    shopping_items.append(shopping_item)
singled_items  = set(shopping_items)
sorted_shopping_items = list(singled_items)
sorted_shopping_items.sort()
num = 0
print("Shopping List:")
for item in sorted_shopping_items:
    num +=1
    print(f"{num}.{item}")
print(f"Total Number of Items: {len(sorted_shopping_items)}")
