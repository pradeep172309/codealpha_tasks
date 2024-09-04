num_terms = 10
a, b = 0, 1
for _ in range(num_terms):
    print(a)
    temp = a + b
    a = b
    b = temp
     