def somaQuadradosA(n):
    x = 0
    for n in range(1,n):
        x = x+(n*n);
    return x

x1 = somaQuadradosA(4)
print(x1)

def somaQuadradosB(n):
    x = n (n+1) * (2*n+1)
    x = x/6
    return x

x2 = somaQuadradosA(4)
print(x2)