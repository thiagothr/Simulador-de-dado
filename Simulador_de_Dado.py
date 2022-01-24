import random


print('========== SIMULADOR DE DADO ==========')

def valor_int (msg):
    while True:
        try:
            x = int(input(msg))
        except ValueError as Erro:
            print('\033[31mErro: por favor digite conforme o enunciado!\033[m')
            continue
        else:
            return x
valor = valor_int ('Você gostaria de jogar o dado? 1/sim ou 2/não:')

if (valor == 1):
    x = random.randint(1,6)
    print(x)
elif (valor == 2):
    print('Programa Finalizado. Volte sempre!')
else:
    print('valor invalido.')



   
    
