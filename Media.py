notaA = float(input("Digite a nota A: "));
notaB = float(input("Digite a nota B: "));

#calcular média
mediaFinal = (notaA+notaB) / 2;

#verificação 
if mediaFinal >= 7.0:
    print("A média: %.2f - Aprovado" % mediaFinal);
    #print("Codigo: %f " % mediaFinal)
else:
    #print("A média: $.1f - Reprovado" % mediaFinal);
    print("A média: %.2f - Reprovado" % mediaFinal);