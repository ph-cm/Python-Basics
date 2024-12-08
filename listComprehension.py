l = [x for x in range(5)]

print(l)

l2 = [x**2 for x in range(5)]
print(l2)

matrix = [[[j for j in range(5)] for i in range(5)]]
print(matrix)

n = 3  
m = 4  

# Criar a matriz usando aninhamento de for
matriz = [[i * j for j in range(m)] for i in range(n)]

# Exibir a matriz
for linha in matriz:
    print(linha)

for a, b in zip(range(3), range(4, 7)):
    print(a, b)