### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
# try:
#     quant = int(input('Digite a quantidade: '))
#     preco = int(input('Digite a preco: '))
#     if quant > 0 and preco > 0:
#         print('Dados validos!')
#     else:
#         print('Dados invalidos!')
# except ValueError:
#     print('Dados invalidos!')

    

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# BAIXA = 4
# MEDIA = 7
# ALTA = 10

# try:
#     medicao = int(input('Insira a medicao: '))
    
#     if medicao >= ALTA:
#         print('Medicao alta!')
#     elif medicao >= MEDIA:
#         print('Medicao media!')
#     else:
#         print('Mediao baixa!')
# except ValueError:
#     print('Digite um dado valido')



### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log['level'] == 'ERROR':
#     print(log['message'])
# else:
#     print('Pode prosseguir')



### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
# usuario = {}

# nome = input('Digite seu nome: ')

# if nome.isnumeric() or nome.isspace():
#     print('Digite nomes válidos!')
#     exit()
# else:
#     usuario['nome'] = nome

# try:
#     idade = int(input('Digite sua idade: '))
    
#     if idade < 18 or idade > 65:
#         print('Idade inválida!')
#         exit()
#     else:
#         usuario['idade'] = idade
# except ValueError:
#     print('Valores inválidos para idade!')
#     exit()

# email = input('Digite seu email: ')

# if email.isnumeric() or email.isspace():
#     print('Digite emails válidos!')
#     exit()
# elif '@' not in email:
#     print('Email inválido!')
#     exit()
# else:
#     split_email = email.split('@')
#     if split_email[1] not in ['gmail.com', 'outlook.com', 'yahoo.com']:
#         print('Dominio invalido!')
#         exit()
#     else:
#         usuario['email'] = email

# print('Dados do usuário validados!')




### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
# transacao = {'valor': 12000, 'hora': 10}

# if transacao['valor'] > 10000 and (transacao['hora'] >= 18 or transacao['hora'] < 9):
#     print('Transação suspeita!')
# else:
#     print('Transação normal.')



### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
# texto = input('Digite uma frase: ').lower().replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').lower()

# list_words = texto.split(' ')

# count_words = {}

# for word in list_words:
#     if word in count_words:
#         count_words[word] += 1
#     else:
#         count_words[word] = 1

# print(count_words)


### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
# lista = [1,4,5,10,87]
# lista = [ x / max(lista) for x in lista]
# print(lista)



### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico 
# usuarios = [
#     {'Nome': 'Ferruccio', 'Idade': 27},
#     {'Nome': 'Luana', 'Idade': 28},
#     {'Nome': 'Destruidor', 'Idade': 27}
# ]

# filtrado = list(filter(lambda usuario: usuario['Idade']==27,usuarios))
# print(filtrado)



### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
# lista = [2,3,4,5,6,7,8]

# pares = [x for x in lista if x%2==0]
# print(pares)



### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
# vendas = [
#     {'Categoria': 'Celular', 'Valor': 1000},
#     {'Categoria': 'Computador', 'Valor': 5000},
#     {'Categoria': 'Celular', 'Valor': 1000}
# ]

# venda_por_categoria = {}

# for venda in vendas:
#     categoria = venda['Categoria']
#     valor = venda['Valor']
#     if categoria in venda_por_categoria:
#         venda_por_categoria[categoria] += valor
#     else:
#         venda_por_categoria[categoria] = valor

# print(venda_por_categoria)



### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
# comando = input('Digite o comando: ')

# while comando != 'sair':
#     print('Oh sol ve se nao me esquece, e me ilumina')
#     comando = input('Digite o comando: ')

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
# num = int(input('Digite u numero dentro do intervalo de 1 a 10: '))

# while num > 10 or num < 1:
#     num = int(input('Digite um numero valido: '))



### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
# pagina_atual = 1
# pagina_totais = 5

# while pagina_atual <= pagina_totais:
#     print(f'Processando pagina {pagina_atual}. Total de paginas {pagina_totais}.')
#     pagina_atual += 1



### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
# tentativa = 1

# max_tentativas = 5

# while tentativa <= max_tentativas:
#     print(f'Tentativa de reconexao numero: {tentativa}. Numero maximo de tentativas: {max_tentativas}.')

#     if True:
#         print('Conexao bem sucedida!')
#         break

#     else:
#         print('Tentativa de conexão falhou!')
#         tentativa += 1



### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
# lista = [1,2,3,4,5,6,7]
# i = 0

# while lista[i] != 6:
#     print('Item não encontrado!')
#     i+=1

# print('Item encontrado!')