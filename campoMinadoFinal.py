import random


def gerar_matriz(linhas, colunas, valor):
    return [[valor] * colunas for _ in range(linhas)]


def gerar_bombas(campo_com_bombas, numero_bombas):
    linhas = len(campo_com_bombas)
    colunas = len(campo_com_bombas[0])
    bombas_confirmadas = 0

    while bombas_confirmadas < numero_bombas:
        linha_sorteada = random.randint(0, linhas - 1)
        coluna_sorteada = random.randint(0, colunas - 1)
        if campo_com_bombas[linha_sorteada][coluna_sorteada] != "*":
            campo_com_bombas[linha_sorteada][coluna_sorteada] = "*"
            bombas_confirmadas += 1

    return campo_com_bombas


def printar_campo(campo):
    linhas = len(campo)
    colunas = len(campo[0])

    for i in range(linhas):
        for j in range(colunas):
            print(campo[i][j], end=" | ")
        print(i + 1)


def printar_campo_bombas(campo_com_bombas):
    linhas = len(campo_com_bombas)
    colunas = len(campo_com_bombas[0])

    for i in range(linhas):
        for j in range(colunas):
            print(campo_com_bombas[i][j], end=" | ")
        print(i + 1)


def verificar_posicao_valida(linhas, colunas, linha, coluna):
    return linha >= 1 and linha <= linhas and coluna >= 1 and coluna <= colunas


def verificar_jogada_valida(campo, linha, coluna):
    return campo[linha - 1][coluna - 1] != "x"


def verificar_bomba_presenca(campo_com_bombas, campo_minado, linha_jogada, coluna_jogada):
    if campo_com_bombas[linha_jogada - 1][coluna_jogada - 1] == "*":
        return False
    elif campo_minado[linha_jogada - 1][coluna_jogada - 1] == "x":
        return False

    return True


def input_jogador(campo_minado, campo_com_bombas, linha, coluna):
    linhas = len(campo_minado)
    colunas = len(campo_minado[0])
    bombas_ao_redor = 0

    for i in range(linha - 2, linha + 1):
        for j in range(coluna - 2, coluna + 1):
            if i >= 0 and i < linhas and j >= 0 and j < colunas:
                if campo_com_bombas[i][j] == "*":
                    bombas_ao_redor += 1

    campo_minado[linha - 1][coluna - 1] = str(bombas_ao_redor)

    return campo_minado


def jogar_campo_minado():
    linhas = int(input("Selecione o número de linhas: "))
    colunas = int(input("Selecione o número de colunas: "))
    numero_bombas = int(input("Selecione o número de bombas: "))

    campo = gerar_matriz(linhas, colunas, " ")
    campo_bombas = gerar_matriz(linhas, colunas, " ")

    flag_terminar = True
    vitoria = False
    jogadas_certas = 0

    printar_campo(campo)

    campo_bombas = gerar_bombas(campo_bombas, numero_bombas)

    while flag_terminar and not vitoria:
        input_linha = int(input("Selecione a linha que deseja jogar: "))
        input_coluna = int(input("Selecione a coluna que deseja jogar: "))

        while not verificar_posicao_valida(linhas, colunas, input_linha, input_coluna):
            print("Posição inválida. Selecione uma posição dentro da matriz.")
            input_linha = int(input("Selecione a linha que deseja jogar: "))
            input_coluna = int(input("Selecione a coluna que deseja jogar: "))

        while not verificar_jogada_valida(campo, input_linha, input_coluna):
            print("Você já jogou nessa posição.")
            input_linha = int(input("Selecione a linha que deseja jogar: "))
            input_coluna = int(input("Selecione a coluna que deseja jogar: "))

        flag_terminar = verificar_bomba_presenca(campo_bombas, campo, input_linha, input_coluna)

        if flag_terminar:
            jogadas_certas += 1
            campo = input_jogador(campo, campo_bombas, input_linha, input_coluna)
            printar_campo(campo)

            if jogadas_certas == linhas * colunas - numero_bombas:
                vitoria = True
                print("Você ganhou!")

        if not flag_terminar and not vitoria:
            printar_campo_bombas(campo_bombas)
            print("BOOOMMM!")

    reiniciar = input("Deseja jogar novamente? (S/N): ")
    if reiniciar.lower() == "s":
        jogar_campo_minado()


jogar_campo_minado()
