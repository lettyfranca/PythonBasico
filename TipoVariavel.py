codigo = 10
salario = 1500.00
nome = 'Joao'
situacao = True

tipo = type (salario)

print(salario)
print(tipo)

print("Codigo: ", codigo, "Nome:",nome, "O salario atual e de ",salario)

#Também podemos concatenar as informações na linguagem Python utilizando o sinal de soma (+).
#Neste caso, temos de converter os valores que não são string para o tipo string.
#Para isso, utilizamos o comando (str) antes da impressão da variável.

print("Codigo: " + str(codigo) + " Nome: " + str(nome) + ". O salario atual e de: " + str(salario))