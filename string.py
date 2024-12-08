name = "Pedro"
fav_num = 3

f"Hey {name} how is it going? My favorite number is {fav_num}"

print(f"Hey {name} how is it going ? My favorite number is {fav_num}") # type: ignore

#almost everything in python is an object
print("my name is Pedro".split(" "))

#tuples
t = (1, 0)
print(t)

for i in t:
    print(i)

#tuples are imutable
t[1] = 2
print(t)