CONSTANTE_BONUS = 1000


nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido == False or salario_valido == False or bonus_valido == False:

    nome = input('Digite seu nome: ')

    if nome.isdigit():
        print('Digitou um numero no nome. Digite um nome valido!')
        nome_valido = False
    elif len(nome) == 0:
        print('Digite um nome válido!')
        nome_valido = False
    elif nome.isspace():
        print('Digitou somente espaço. Digite um nome valido!')
        nome_valido = False
    else:
        nome_valido = True
        try:
            salario = round(float(input('Digite seu salario: ')),2)
            bonus = round(float(input('Digite o bonus: ')),2)
            if salario > 0 and bonus >= 0:
                print('Salario e bonus validos!')
                salario_valido = True
                bonus_valido = True
            else:
                print('Salario e bonus nao validos!')
                salario_valido = False
                bonus_valido = False
        except ValueError:
            salario_valido = False
            bonus_valido = False
        
resultado_b = CONSTANTE_BONUS + round(salario * (bonus),2)

print(f'Ola {nome}, tudo bem? \n Seu salário é R${salario} e com o percentual de {bonus}% o se bonus é R${resultado_b}')