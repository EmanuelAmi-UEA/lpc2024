from num2words import num2words

numero = int(input("Digite um numero (máx.:99): "))

num_extenso = num2words(numero, lang='pt-br')

print(num_extenso)
