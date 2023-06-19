import random


def gerar_matriz(tamanho, valor):
    return [[valor] * tamanho for _ in range(tamanho)]


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
    tamanho = len(campo)

    for i in range(tamanho):
        for j in range(tamanho):
            print(campo[i][j], end=" | ")
        print(i + 1)


def printar_campo_bombas(campo_com_bombas):
    tamanho = len(campo_com_bombas)

    for i in range(tamanho):
        for j in range(tamanho):
            print(campo_com_bombas[i][j], end=" | ")
        print(i + 1)


def verificar_posicao_valida(tamanho, linha, coluna):
    return linha >= 0 and linha < tamanho and coluna >= 0 and coluna < tamanho


def verificar_jogada_valida(campo, linha, coluna, jogada):
    if jogada == "abrir":
        return campo[linha][coluna] != "x" and campo[linha][coluna] == " "
    else:
        if jogada == "marcar":
            return campo[linha][coluna] != "x"
        else:
            if jogada == "desmarcar":
                return campo[linha][coluna] == "x"

    return False


def verificar_bomba_presenca(campo_com_bombas, linha_jogada, coluna_jogada, jogada):
    if jogada != "marcar":
        if campo_com_bombas[linha_jogada][coluna_jogada] == "*":
            return False

    return True


def contar_minas_ao_redor(campo_com_bombas, linha, coluna):
    count = 0
    direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for direcao in direcoes:
        nova_linha = linha + direcao[0]
        nova_coluna = coluna + direcao[1]

        if verificar_posicao_valida(len(campo_com_bombas), nova_linha, nova_coluna) and campo_com_bombas[nova_linha][nova_coluna] == "*":
            count += 1

    return count


def input_jogador(campo_minado, campo_com_bombas, linha, coluna, jogada):

    if jogada == "abrir":
        minas_ao_redor = contar_minas_ao_redor(campo_com_bombas, linha, coluna)
        campo_minado[linha][coluna] = str(minas_ao_redor)
    else:
        if jogada == "marcar":
            campo_minado[linha][coluna] = "x"
        else:
            if jogada == "desmarcar":
                campo_minado[linha][coluna] = " "
    return campo_minado


def jogar_campo_minado():
    tamanho_tabuleiro = int(input("Selecione o tamanho do tabuleiro: "))
    numero_bombas = int(input("Selecione o número de bombas (entre 1 e {}): ".format((tamanho_tabuleiro * tamanho_tabuleiro) // 2)))

    campo = gerar_matriz(tamanho_tabuleiro, " ")
    campo_bombas = gerar_matriz(tamanho_tabuleiro, " ")

    flag_terminar = True
    vitoria = False
    jogadas_certas = 0

    printar_campo(campo)

    campo_bombas = gerar_bombas(campo_bombas, numero_bombas)

    while flag_terminar and not vitoria:
        input_linha = int(input("Selecione a linha que deseja jogar (de 1 a {}): ".format(tamanho_tabuleiro))) - 1
        input_coluna = int(input("Selecione a coluna que deseja jogar (de 1 a {}): ".format(tamanho_tabuleiro))) - 1
        jogada = input("Digite 'abrir' para abrir a célula, 'marcar' para marcar uma mina, ou 'desmarcar' para desmarcar uma mina: ")

        while not verificar_posicao_valida(tamanho_tabuleiro, input_linha, input_coluna):
            print("Posição inválida. Selecione uma posição dentro do tabuleiro.")
            input_linha = int(input("Selecione a linha que deseja jogar (de 1 a {}): ".format(tamanho_tabuleiro))) - 1
            input_coluna = int(input("Selecione a coluna que deseja jogar (de 1 a {}): ".format(tamanho_tabuleiro))) - 1

        while not verificar_jogada_valida(campo, input_linha, input_coluna, jogada):
            print("Jogada inválida. Selecione uma posição válida para jogar.")
            input_linha = int(input("Selecione a linha que deseja jogar (de 1 a {}): ".format(tamanho_tabuleiro))) - 1
            input_coluna = int(input("Selecione a coluna que deseja jogar (de 1 a {}): ".format(tamanho_tabuleiro))) - 1

        flag_terminar = verificar_bomba_presenca(campo_bombas, input_linha, input_coluna, jogada)

        if flag_terminar:
            if jogada != "marcar":
                jogadas_certas += 1

            campo = input_jogador(campo, campo_bombas, input_linha, input_coluna, jogada)
            printar_campo(campo)

            if jogadas_certas == tamanho_tabuleiro * tamanho_tabuleiro - numero_bombas:
                vitoria = True
                print("Você ganhou!")

        if not flag_terminar and not vitoria:
            printar_campo_bombas(campo_bombas)
            print("BOOOMMM!")

    reiniciar = input("Deseja jogar novamente? (S/N): ")
    if reiniciar.lower() == "s":
        jogar_campo_minado()


jogar_campo_minado()
