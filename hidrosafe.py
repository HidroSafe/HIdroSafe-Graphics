import os
import matplotlib.pyplot as plt

# Calcula o número de linhas (dias) a partir de medias.csv
with open("medias.csv", "r") as arquivo:
    linhas = sum(1 for _ in arquivo)

def clear():
    """Limpa a tela, compatível com Windows e Unix."""
    if os.name == 'nt':
        os.system('cls')
    else:
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
    1. Consultar Banco de Dados
    2. Editar Banco de Dados
    3. Gerar gráficos
    0. Sair

""")

def plotLista(arquivo):
    """
    Exibe 10 valores por linha (dia e valor), conforme
    o arquivo passado como parâmetro.
    """
    clear()
    print(f"--- Exibindo dados de '{arquivo}' ---\n")
    with open(arquivo, "r") as arq:
        for i in range(linhas):
            linha = arq.readline().strip()
            print(f"Dia {i+1:3}: {float(linha):6.2f}", end="   ")
            if (i + 1) % 10 == 0:
                print("\n")
    print("\n")

# ---------------------------------------------------
#  plotarGraficos() atualizado com opção “Dias (1 a N)”
# ---------------------------------------------------
def plotarGraficos():
    clear()
    print(r"""
*---------------------------------------------*
*-------------Gerar Gráficos------------------*
*---------------------------------------------*
1. Escolher estilo do gráfico
2. Escolher formato de arquivo de saída
3. Escolher EIXOS X e Y
4. Gerar e salvar gráfico
0. Voltar ao menu principal

""")
    # Valores padrão
    estilo = 'linha_continua'
    formato_arquivo = 'png'
    eixo_x_tipo = None   # 'arquivo' ou 'dias'
    eixo_y_tipo = None
    arquivo_x = None
    arquivo_y = None

    def menu_estilo():
        nonlocal estilo
        clear()
        print("--- Escolha o estilo do gráfico ---\n")
        print("1. Linha contínua")
        print("2. Linha pontilhada")
        print("3. Somente pontos")
        print("4. Linha + pontos")
        print("0. Voltar")
        escolha = input("-> ")
        match escolha:
            case "1":
                estilo = 'linha_continua'
            case "2":
                estilo = 'linha_pontilhada'
            case "3":
                estilo = 'somente_pontos'
            case "4":
                estilo = 'linha_pontos'
            case "0":
                return
            case _:
                print("Opção inválida! Tente de novo.")
                input("Pressione Enter para continuar...")
                menu_estilo()

    def menu_formato():
        nonlocal formato_arquivo
        clear()
        print("--- Escolha o formato de saída ---\n")
        print("1. PNG")
        print("2. JPEG")
        print("3. PDF")
        print("4. SVG")
        print("0. Voltar")
        escolha = input("-> ")
        match escolha:
            case "1":
                formato_arquivo = 'png'
            case "2":
                formato_arquivo = 'jpeg'
            case "3":
                formato_arquivo = 'pdf'
            case "4":
                formato_arquivo = 'svg'
            case "0":
                return
            case _:
                print("Opção inválida! Tente de novo.")
                input("Pressione Enter para continuar...")
                menu_formato()

    def menu_arquivos_eixos():
        """
        Permite ao usuário escolher para cada eixo:
        - 1,2 ou 3 para arquivos (medias.csv, picos.csv, horarios.csv)
        - 4 para usar o vetor [1, 2, …, linhas]
        """
        nonlocal eixo_x_tipo, eixo_y_tipo, arquivo_x, arquivo_y
        clear()
        print("--- Escolha os dados para EIXO X ---\n")
        print("1. medias.csv")
        print("2. picos.csv")
        print("3. horarios.csv")
        print("4. Dias (1 a N)")
        print("0. Voltar")
        escolha_x = input("-> ")
        if escolha_x == "0":
            return
        elif escolha_x in ("1", "2", "3"):
            eixo_x_tipo = 'arquivo'
            mapa = {"1": "medias.csv", "2": "picos.csv", "3": "horarios.csv"}
            arquivo_x = mapa[escolha_x]
        elif escolha_x == "4":
            eixo_x_tipo = 'dias'
            arquivo_x = None
        else:
            print("Opção inválida para eixo X!")
            input("Pressione Enter para continuar...")
            menu_arquivos_eixos()
            return

        # Agora eixo Y
        clear()
        print("--- Escolha os dados para EIXO Y ---\n")
        print("1. medias.csv")
        print("2. picos.csv")
        print("3. horarios.csv")
        print("4. Dias (1 a N)")
        print("0. Voltar")
        escolha_y = input("-> ")
        if escolha_y == "0":
            return
        elif escolha_y in ("1", "2", "3"):
            eixo_y_tipo = 'arquivo'
            mapa = {"1": "medias.csv", "2": "picos.csv", "3": "horarios.csv"}
            arquivo_y = mapa[escolha_y]
        elif escolha_y == "4":
            eixo_y_tipo = 'dias'
            arquivo_y = None
        else:
            print("Opção inválida para eixo Y!")
            input("Pressione Enter para continuar...")
            menu_arquivos_eixos()
            return

        # Impede usar “Dias” em ambos os eixos simultaneamente,
        # pois ambos virariam range(1, linhas+1) e não faria sentido.
        if eixo_x_tipo == 'dias' and eixo_y_tipo == 'dias':
            print("Não é permitido usar 'Dias' em X e Y ao mesmo tempo!")
            input("Pressione Enter para voltar a escolher...")
            eixo_x_tipo = None
            eixo_y_tipo = None
            arquivo_x = None
            arquivo_y = None
            menu_arquivos_eixos()

    def gerar_e_salvar():
        nonlocal estilo, formato_arquivo, eixo_x_tipo, eixo_y_tipo, arquivo_x, arquivo_y
        clear()

        # Valida se já foi escolhido ambos eixos
        if eixo_x_tipo is None or eixo_y_tipo is None:
            print("Por favor, escolha primeiro EIXOS X e Y (opção 3).")
            input("Pressione Enter para continuar...")
            return

        # 1) Obter dados para X
        if eixo_x_tipo == 'dias':
            dados_x = list(range(1, linhas + 1))
        else:
            try:
                with open(arquivo_x, "r") as arqx:
                    dados_x = [float(l.strip()) for l in arqx]
            except Exception as e:
                print(f"Erro ao ler '{arquivo_x}': {e}")
                input("Pressione Enter para voltar...")
                return

        # 2) Obter dados para Y
        if eixo_y_tipo == 'dias':
            dados_y = list(range(1, linhas + 1))
        else:
            try:
                with open(arquivo_y, "r") as arqy:
                    dados_y = [float(l.strip()) for l in arqy]
            except Exception as e:
                print(f"Erro ao ler '{arquivo_y}': {e}")
                input("Pressione Enter para voltar...")
                return

        # 3) Verifica se têm o mesmo tamanho
        if len(dados_x) != len(dados_y):
            print("X e Y têm tamanhos diferentes! Não é possível plotar.")
            print(f"  |X| = {len(dados_x)} vs |Y| = {len(dados_y)}")
            input("Pressione Enter para continuar...")
            return

        # 4) Desenha o gráfico conforme o estilo
        plt.figure(figsize=(8, 5))
        if estilo == 'linha_continua':
            plt.plot(dados_x, dados_y, linestyle='-', marker='')
        elif estilo == 'linha_pontilhada':
            plt.plot(dados_x, dados_y, linestyle=':', marker='')
        elif estilo == 'somente_pontos':
            plt.plot(dados_x, dados_y, linestyle='', marker='o')
        elif estilo == 'linha_pontos':
            plt.plot(dados_x, dados_y, linestyle='-', marker='o')

        # Rotular eixos
        label_x = "Dias (1 a N)" if eixo_x_tipo == 'dias' else f"Eixo X: {arquivo_x}"
        label_y = "Dias (1 a N)" if eixo_y_tipo == 'dias' else f"Eixo Y: {arquivo_y}"
        plt.xlabel(label_x)
        plt.ylabel(label_y)
        plt.title("HidroSafe – Gráfico de Dados do Rio")
        plt.grid(True)

        # 5) Determina nome de saída
        nome_x = "dias" if eixo_x_tipo == 'dias' else arquivo_x.replace('.csv', '')
        nome_y = "dias" if eixo_y_tipo == 'dias' else arquivo_y.replace('.csv', '')
        nome_saida = f"grafico_{nome_x}_x_{nome_y}.{formato_arquivo}"

        # 6) Salva o arquivo
        try:
            plt.savefig(nome_saida, format=formato_arquivo, bbox_inches='tight')
            print(f"\nGráfico salvo em: '{nome_saida}'")
        except Exception as e:
            print(f"Erro ao salvar o gráfico: {e}")
        finally:
            plt.close()

        input("Pressione Enter para continuar...")

    # ---- Loop principal do submenu de plotagem ----
    while True:
        clear()
        print(r"""
*---------------------------------------------*
*-------------Gerar Gráficos------------------*
*---------------------------------------------*
1. Escolher estilo do gráfico
2. Escolher formato de arquivo de saída
3. Escolher EIXOS X e Y
4. Gerar e salvar gráfico
0. Voltar ao menu principal

""")
        opc = input("-> ")
        match opc:
            case "1":
                menu_estilo()
            case "2":
                menu_formato()
            case "3":
                menu_arquivos_eixos()
            case "4":
                gerar_e_salvar()
            case "0":
                break
            case _:
                print("Opção inválida!")
                input("Pressione Enter para continuar...")

# ---------------------------------------------------
# Funções consultarBanco() e editarBanco() mantêm-se iguais
# ---------------------------------------------------

def consultarBanco():
    clear()
    print(r"""
*---------------------------------------------*
*--------------Consultar Banco----------------*
*---------------------------------------------*
    1. Mostrar: Média do nível do rio
    2. Mostrar: Picos do nível do rio
    3. Mostrar: Horário de pico
    0. Voltar ao menu principal

    """)
    while True:
        print(f"Total de dias Armazenados: {linhas}")
        escolha = input("-> ")
        if not escolha.isdigit():
            print("Digite uma opção numérica válida!")
            continue

        opc = int(escolha)
        match opc:
            case 1:
                plotLista("medias.csv")
            case 2:
                plotLista("picos.csv")
            case 3:
                plotLista("horarios.csv")
            case 0:
                clear()
                intro()
                break
            case _:
                print("Digite uma opção válida!")

def editarBanco():
    clear()
    print(r"""
*---------------------------------------------*
*----------------Editar Banco-----------------*
*---------------------------------------------*
    1. Editar: Média do nível do rio
    2. Editar: Picos do nível do rio
    3. Criar nova lista de dados (sobrescreve o arquivo)
    0. Voltar ao menu principal

    """)
    while True:
        print(f"Total de dias Armazenados: {linhas}")
        escolha = input("-> ")
        if not escolha.isdigit():
            print("Digite uma opção numérica válida!")
            continue

        opc = int(escolha)
        match opc:
            case 1:
                editarLista("medias.csv")
            case 2:
                editarLista("picos.csv")
            case 3:
                clear()
                print("Qual lista deseja criar do zero?")
                print(" 1. medias.csv\n 2. picos.csv\n 3. horarios.csv\n 0. Cancelar")
                sub = input("-> ")
                if sub == "1":
                    criarLista("medias.csv")
                elif sub == "2":
                    criarLista("picos.csv")
                elif sub == "3":
                    criarLista("horarios.csv")
                elif sub == "0":
                    pass
                else:
                    print("Opção inválida!")
                    input("Pressione Enter para continuar...")
                clear()
                clear()
                print(r"""
*---------------------------------------------*
*----------------Editar Banco-----------------*
*---------------------------------------------*
    1. Editar: Média do nível do rio
    2. Editar: Picos do nível do rio
    3. Criar nova lista de dados (sobrescreve o arquivo)
    0. Voltar ao menu principal

    """)
            case 0:
                clear()
                intro()
                break
            case _:
                print("Digite uma opção válida!")

# ---------------------------------------------------
#       PONTO DE ENTRADA DO PROGRAMA
# ---------------------------------------------------

intro()
while True:
    escolha = input("-> ")
    if not escolha.isdigit():
        print("Digite uma opção numérica válida!")
        continue

    opc = int(escolha)
    match opc:
        case 1:
            consultarBanco()
        case 2:
            editarBanco()
        case 3:
            plotarGraficos()
        case 0:
            exit(0)
        case _:
            print("Digite uma opção válida!")
