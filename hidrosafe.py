#Programa hidrosafe

import matplotlib.pyplot as plt
import numpy
import os 
# Função para identificar o sistema e adequar o comando clear do terminal para cada sistema
def clear():
    sistema = os.name
    if sistema == 'nt':  # Sistema Windows
        os.system('cls')
    else:  # Para sistemas Linux ou macOS
        os.system('clear')

quebraDePagina = "*----------------------------------------------*"
def intro():
   clear()
   print(quebraDePagina)
   print(r"""
 _   _ _     _          ____         __      
| | | (_) __| |_ __ ___/ ___|  __ _ / _| ___ 
| |_| | |/ _` | '__/ _ \___ \ / _` | |_ / _ \
|  _  | | (_| | | | (_) |__) | (_| |  _|  __/
|_| |_|_|\__,_|_|  \___/____/_\__,_|_|  \___|
 / ___|_ __ __ _ _ __ | |__ (_) ___ ___      
| |  _| '__/ _` | '_ \| '_ \| |/ __/ __|     
| |_| | | | (_| | |_) | | | | | (__\__ \     
 \____|_|  \__,_| .__/|_| |_|_|\___|___/     
                |_|                          
""")
   print(quebraDePagina)
   print(r"""
-> Olá usuário, esse programa tem o objetivo de editar, tratar e plotar
os parâmetros lidos pelo produto HidroSafe, são eles:
-> Nível médio do rio no dia
-> Pico de altura do rio no dia (em relação ao assoalho)
-> Horário do pico

""")       
   print(quebraDePagina)
   print(r"""
*---------------------------------------------*
*--------------------MENU---------------------*
*---------------------------------------------*
1.Consultar Banco de Dados
2.Editar Banco de Dados
3.Gerar gráficos
0.Sair

""")  



def consultarBanco():
    clear()
    print(r"""
*---------------------------------------------*
*--------------Consultar Banco----------------*
*---------------------------------------------*
    1.Mostrar: Média do nível do rio
    2.Mostrar: Picos do nível do rio
    3.Mostrar: Horário de pico
    0.Sair

    """) 
    while True:

        with open("medias.csv", "r") as arquivo:
            linhas = sum(1 for _ in arquivo)

        print(f"Total de dias Armazenados: {linhas}")
        
        match int(input("-> ")):
            case 1:
                with open("medias.csv", "r") as arquivo:
                    print("--- Níveis Médios do Rio ---\n")
                    for i in range(linhas):
                        valor = arquivo.readline().strip()
                        print(f"Dia {i+1:3}: {float(valor):5.2f}", end="   ")
                        if (i + 1) % 10 == 0:
                            print("\n")  # Pula linha a cada 10 leituras
                print("\n")

            case 0:
                intro()
                break
            case _:
                print("Digite uma opção válida!")




intro()


while True:
    opcao = int(input("-> "))
    match opcao:
        case 1:
            consultarBanco()
        case 0:
            exit(0)
        case _:
            print("Digite uma opção válida!")



