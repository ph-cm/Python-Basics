p = 'text_file.txt'

with open(p, 'r') as f:
    print(f.read())
    
with open('text_file.txt', 'w') as f:
    f.write("Hi")