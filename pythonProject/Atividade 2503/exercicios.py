'''
#Exercício 1 - Valor Maior

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if num1 > num2:
    print(f"O maior valor é {num1}")
else:
    print(f"O maior valor é {num2}")


#Exercicio 2 - Votar

anoNascimento = int(input("Digite o seu ano de nascimento: "))
idade = 2025 - anoNascimento

if idade < 16:
    print("Proibido votar")
elif idade < 18 or idade >= 70:
    print("Votar é opcional")
else:
    print("Votar é obrigatório")

if idade < 16:
    print("Proibido votar")
elif idade < 18:
    print("Votar é opcional, jovem")
elif idade < 70:
    print("Votar é obrigatório")
else:
    print("Votar é opcional, senhor")


#Exercicio 3 - Senha Válida

senhaCadastrada = "1234"
senhaFornecida = input("Digite uma senha: ")

if senhaFornecida == senhaCadastrada:
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")


#Exercicio 4 - Comprar maçãs

quantMaca = int(input("Digite a quantidade de maçã comprada: "))

#if quantMaca < 12:
#    valor = 0.3
#else:
#    valor = 0.25
#total = quantMaca * valor

valor = 0.25
if quantMaca < 12:
    valor = 0.3
total = quantMaca * valor

print(f"O valor total da sua compra é R${total}")


#Exercício 5 - Ordem crescente

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num3 < num2:
    numAuxiliar = num2
    num2 = num3
    num3 = numAuxiliar

if num2 < num1:
    numAuxiliar = num1
    num1 = num2
    num2 = numAuxiliar

if num3 < num2:
    numAuxiliar = num2
    num2 = num3
    num3 = numAuxiliar

print(f"A ordem crescente dos números é: {num1}, {num2}, {num3}")


#Exercício 6 - Calcular peso

altura = float(input("Digite a sua altura em metros: "))
sexo = input("Digite o seu gênero: ")

if sexo == "masculino":
    pesoIdeal = (72.7 * altura) - 58
else:
    pesoIdeal = (62.1 * altura) - 44.7

print(f"O seu peso ideal é {pesoIdeal:.1f}")


#Exercício 7 e 8 - Perímetro de polígonos

numLados = int(input("Digite a quantidade de lados: "))
medidaLado = int(input("Digite a medida do lado em cm: "))

if numLados < 3:
    print("Não é um polígono")
elif numLados == 3:
    print("Triângulo")
elif numLados == 4:
    print("Quadrado")
elif numLados == 5:
    print("Pentágono")
else:
    print("Polígono não identificado")

if numLados < 3:
    print("Não é possível calcular o valor do perímetro")
else:
    print(f"O valor do perímetro é {medidaLado * numLados}cm")


numLados = int(input("Digite a quantidade de lados: "))
if numLados < 3:
    print("Não é um polígono")
elif numLados > 5:
    print("Polígono não identificado")
else:
    medidaLado = int(input("Digite a medida do lado em cm: "))
    perimetro = numLados * medidaLado
    if numLados == 3:
        forma = "triângulo"
    elif numLados == 4:
        forma = "quadrado"
    elif numLados == 5:
        forma = "pentágono"
    print(f"É um {forma} de perímetro {perimetro})



#Exercício 9 - Maior entre os 3

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))

maiorValor = num1

if num2 > maiorValor:
    maiorValor = num2
if num3 > maiorValor:
    maiorValor = num3

print(maiorValor)


#Exercício 10 - Classificação de triângulos

lado1 = int(input("Digite a medida do primeiro lado: "))
lado2 = int(input("Digite a medida do segundo lado: "))
lado3 = int(input("Digite a medida do terceiro lado: "))

if lado1 == lado2 and lado1 == lado3:
    print("Triângulo equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo isósceles")
else:
    print("Triângulo escaleno")


#Exercício 11 - Identificar ângulo

angulo1 = int(input("Digite o valor do primeiro ângulo: "))
angulo2 = int(input("Digite o valor do segundo ângulo: "))
angulo3 = int(input("Digite o valor do terceiro ângulo: "))

if angulo1 + angulo2 + angulo3 == 180:
    if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        print("Triângulo Acutângulo")
    elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print("Triângulo Retângulo")
    else:
        print("Triângulo Obtusângulo")
else:
    print("Não é um triângulo")
'''