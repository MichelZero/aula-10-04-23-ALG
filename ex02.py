#
# autores:
# Cristiano e Michel

# data: 10/04/2023

# Implemente um programa em linguagem Python que recebe 
# como entradas a base e a altura de um triângulo e 
# apresente ao usuário a área deste triângulo. A área 
# de um triângulo é calculada a partir da seguinte 
# expressão: AT = (b ∗ h)/2, em que b é a base do
# triângulo e h a sua altura.

# entrada de dados
base = int(input("informe a base: "))
altura = float(input("informe a altura: "))

# processamento
AT = (base * altura)/2

# saída
print(f"a área é: {AT}")
