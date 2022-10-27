cpf = input("CPF: ")
new_cpf = cpf[:-2]
r = 10
total = 0

for i in range(19):
    if i > 8:
        i -= 9

    total += int(new_cpf[i]) * r

    r -= 1
    if r < 2:
        r = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        new_cpf += str(d)

if new_cpf == cpf:
    print("CPF VÁLIDO!")
else:
    print("CPF INVÁLIDO!")
