
grocery_list = ["banana", "apple", "orange"]
grocery_list.append("fruit")
print(grocery_list)

for item in grocery_list:
    print(item)

print(grocery_list[0])

for i in [0, 1, 2, 3]:
    print(grocery_list[i])
    
for i in range(4):
    print(grocery_list[i])
    
print(list(range(len(grocery_list))))

for i in range(len(grocery_list)):
    print(grocery_list[i])

for i, item in enumerate(grocery_list):
    print(i, item)
    