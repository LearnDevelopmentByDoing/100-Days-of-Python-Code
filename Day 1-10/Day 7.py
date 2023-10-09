a = 0
b = 1

for i in range(10):
    som = a
    a = b
    b = som + b
    print(som)
