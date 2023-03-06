def soma():
    n1 = int(input("\nDigite o primeiro número = "))
    n2 = int(input("Digite o segundo número = "))
    print("\n", n1," + ",n2, " = ", n1 + n2)
    print("\n")
    
def sub():
    n1 = int(input("\nDigite o primeiro número = "))
    n2 = int(input("Digite o segundo número = "))
    print("\n", n1," - ",n2, " = ", n1 - n2)
    print("\n")

def mult():
    n1 = int(input("\nDigite o primeiro número = "))
    n2 = int(input("Digite o segundo número = "))
    print("\n", n1," * ",n2, " = ", n1 * n2)
    print("\n")

def div():
    n1 = int(input("\nDigite o numerador = "))
    n2 = int(input("Digite o denominador = "))
    if n2 == 0:
        print("\nDenominador não pode ser zero.")
        print("\n")
    else:
        print("\n", n1," / ",n2, " = ", n1 / n2)
        print("\n")

print("\n****** Calculadora em Python ******")
print("\nEscolha a operação:")
print("\n1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = input("\nEscolha: ")

if escolha == '1':
    soma()        

elif escolha == '2':
    sub()
    
elif escolha == '3':
    mult()        
    
elif escolha == '4':
    div()

else:
    print("\nOpção inválida.\n\n")