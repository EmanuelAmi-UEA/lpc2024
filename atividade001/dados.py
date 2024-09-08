import random

repetidos = []
num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0
num_6 = 0

for i in range(1, 101):
    dado = random.randint(1, 6)

    if(dado==1):
        num_1+=1
    elif(dado==2):
        num_2+=1
    elif(dado==3):
        num_3+=1
    elif(dado==4):
        num_4+=1
    elif(dado==5):
        num_5+=1
    elif(dado==6):
        num_6+=1

repetidos.append(num_1)
repetidos.append(num_2)
repetidos.append(num_3)
repetidos.append(num_4)
repetidos.append(num_5)
repetidos.append(num_6)

print(repetidos)

for show in range(7):
    print(f'N{show+1} = {repetidos[show]}')