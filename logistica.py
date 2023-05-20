# Exercício elaborado na aula de Lógica de Programação e Algoritmos
print('\033[7m-=-=-=-=-=-=-=-=-=- Boas-vindas à Empresa de Logística de Carolina Cozer Bacca -=-=-=-=-=-=-=-=-=-\033[m')
print('--------------------------------------------------------------------------------------------------')
print('\033[7m-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=- Dimensões do Objeto -=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=\033[m')
print('--------------------------------------------------------------------------------------------------')
def dimensoesObjeto(): # Aqui vão as informações que definem o preço com base no volume final do objeto
   while True:
       try:
           altura = float(input('\033[1;44;33m>\033[m Digite a altura do objeto em cm: '))
           comprimento = float(input('\033[1;44;33m>\033[m Digite o comprimento do objeto em cm: '))
           largura = float(input('\033[1;44;33m>\033[m Digite a largura do objeto em cm: '))
           volume = altura * comprimento * largura
           if volume < 1000:
               return 10
           elif volume < 10000:
               return 20
           elif volume < 30000:
               return 30
           elif volume < 100000:
               return 50
           else:
               print('Valor indisponível. Não trabalhamos com objetos nestas dimensões.')
       except ValueError:
           print('Este caractere é inválido. Tente novamente.') # Caso o usuário digite qualquer coisa que não seja um número


def pesoObjeto(): # Aqui é calculado o valor referente ao peso
   while True:
       try:
           peso = float(input('\033[1;44;33m>\033[m Digite o peso do objeto em kg: '))
           if peso <= 0.1:
               return 1
           elif peso < 1:
               return 1.5
           elif peso < 10:
               return 2
           elif peso < 30:
               return 3
           else:
               print('Não trabalhamos com o peso escolhido. Tente novamente.')
       except ValueError:
           print('Este caractere é inválido. Tente novamente.') # Caso o usuário digite qualquer coisa que não um número


def rotaObjeto(): # Aqui é calculado o valor referente à distância
   rotas = {
       '1': 1,
       '2': 1.2,
       '3': 1.5,
   }
   while True:
       rota = input('\033[1;44;33m>\033[m Escolha uma das rotas abaixo: \n 1 - SP-RJ \n 2 - RS-SP \n 3 - RS-BSB \n \033[1;44;33m>\033[m Digite o número da rota escolhida: ').upper()
       if rota in rotas:
           return rotas[rota]
       else:
           print('Não trabalhamos com as rotas escolhidas. Tente novamente.') # Caso o usuário digite qualquer coisa que não seja 1/2/3

# Aqui o programa final é exibido
dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimensoes * peso * rota
print('O preço final da sua encomenda ficou: R$ {:.2f}. Agradecemos pela preferência!' .format(total))