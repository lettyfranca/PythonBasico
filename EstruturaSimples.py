A = input("Informe um valor para A")    
B = input("Informe um valor para B")

if (A>B):
    aux = A;
    A = B;
    B = aux;
print("O valor de A é: ", A);
print("O valor de B é: ", B);