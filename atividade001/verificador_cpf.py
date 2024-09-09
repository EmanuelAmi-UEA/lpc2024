
cpf = str(input("Digite um CPF valido no formato xxx.xxx.xxx-xx\n"))

no_dash_cpf = cpf.replace("-", ".")
split_cpf = no_dash_cpf.split(".")
only_num = int(no_dash_cpf.replace(".", ""))
num_size = str(no_dash_cpf.replace(".", ""))
last_digit_verification_first = ((int(num_size[0])*10+int(num_size[1])*9+int(num_size[2])*8+int(num_size[3])*7+int(num_size[4])*6+int(num_size[5])*5+int(num_size[6])*4+int(num_size[7])*3+int(num_size[8])*2)*10)%11
last_digit_verification_second = ((int(num_size[0])*11+int(num_size[1])*10+int(num_size[2])*9+int(num_size[3])*8+int(num_size[4])*7+int(num_size[5])*6+int(num_size[6])*5+int(num_size[7])*4+int(num_size[8])*3+int(num_size[9])*2)*10)%11

if last_digit_verification_first==10:
    last_digit_verification_first=0
if last_digit_verification_second==10:
    last_digit_verification_second=0
print(num_size[10])
print(num_size[9])
if len(cpf) == 14 and len(split_cpf[0]) == 3 and len(split_cpf[1]) == 3 and len(split_cpf[2]) == 3 and len(split_cpf[3]) == 2 and cpf[3] == "." and cpf[7] == "." and cpf[11] == "-" and int(num_size[10])==last_digit_verification_second and int(num_size[9])==last_digit_verification_first:
    print("Este cpf é valido")

else:
    print("Este cpf é invalido")
