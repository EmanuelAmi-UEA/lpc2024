palavra = input("digite uma palavra palindroma:")

palavra_trim = palavra.replace(" ","")

inversor = palavra_trim[ : :-1]

if inversor==palavra_trim:

    print(f'A palavra {palavra} é palindroma')
