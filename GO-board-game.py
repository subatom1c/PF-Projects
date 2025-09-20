# TAD intersecao

# Construtor

def cria_intersecao(coluna, linha):
    """
    Criação de uma interseção

    Pârametros:
        coluna (string): Coluna do goban
        linha (inteiro): Linha do goban
        
    Retorna:
        tuple: Interseção
    """
    # Verificação dos valores de entrada
    if type(coluna) != str or len(coluna) != 1 or type(linha) != int:
        raise ValueError('cria_intersecao: argumentos invalidos')
    if not (65 <= ord(coluna) <= 83 and 1 <= linha <= 19):
        raise ValueError('cria_intersecao: argumentos invalidos')
    return coluna, linha


# Seletor

def obtem_col(intersecao):
    """
    Obter a coluna de um goban

    Pârametros:
        intersecao (tuplo): Interseção
        
    Retorna:
        str: Coluna do goban
    """
    return intersecao[0]


def obtem_lin(intersecao):
    """
    Obter a linha de um goban

    Pârametros:
        intersecao (tuplo): Interseção

    Retorna:
        int: Linha do goban
    """
    return intersecao[1]


# Reconhecedor

def eh_intersecao(intersecao):
    """
    Verificar a validade de uma interseção

    Pârametros:
        intersecao (tuplo): Interseção

    Retorna:
        boolean: Validade de uma interseção
    """
    
    try:
        # Verificação dos valores de entrada
        if len(intersecao) != 2 or type(intersecao) != tuple:
            return False
        if type(obtem_col(intersecao)) != str or type(obtem_lin(intersecao)) != int:
            return False
        if len(obtem_col(intersecao)) != 1:
            return False
        # Validade da interseção
        if not (65 <= ord(obtem_col(intersecao)) <= 83 and 1 <= obtem_lin(intersecao) <= 19):
            return False
        cria_intersecao(obtem_col(intersecao), obtem_lin(intersecao))
        return True
    except IndexError:
        return False
    except ValueError:
        return False
    except TypeError:
        return False


# Teste

def intersecoes_iguais(i1, i2):
    """
    Verificar se duas interseções são iguais

    Pârametros:
        i1 (tuplo): Interseção
        i2 (tuplo): Interseção

    Retorna:
        boolean: Validade da igualdade de duas interseções
    """
    # Verficação se ambas as interseções são interseções
    if not eh_intersecao(i1) or not eh_intersecao(i2):
        return False
    return i1 == i2


# Transformador

def intersecao_para_str(intersecao):
    """
    Transformação de uma interseção para um string

    Pârametros:
        intersecao (tuplo): Interseção

    Retorna:
        str: Interseção em string
    """
    return obtem_col(intersecao) + str(obtem_lin(intersecao))


def str_para_intersecao(string):
    """
    Transformação de um string para uma interseção

    Pârametros:
        string (string): String de uma interseção

    Retorna:
        tuple: Interseção
    """
    # Verificação dos valores de entrada
    if type(string) != str:
        raise ValueError("argumento invalido")
    if len(string) not in (2,3):
        raise ValueError("argumento invalido")
    if not string[1:].isdecimal():
        raise ValueError("argumento invalido")
    
    return cria_intersecao(string[0], int(string[1:]))


# FAN

def obtem_intersecoes_adjacentes(intersecao, topo_direito):
    """
    Obter as interseções adjacentes à interseção dada

    Pârametros:
        intersecao(tuplo): Interseção
        topo_direito(tuplo): Interseção superior direita do tabuleiro de Go

    Retorna:
        tuple: Interseções adjacentes à interseção dada
    """
    col = obtem_col(intersecao)
    linha = obtem_lin(intersecao)
    col_topo = obtem_col(topo_direito)
    linha_topo = obtem_lin(topo_direito)
    adjacentes = ()

    # Baixo
    if linha > 1:
        adjacentes += cria_intersecao(col, linha - 1),

    # Esquerda
    if ord(col) > 65:
        adjacentes += cria_intersecao(chr(ord(col) - 1), linha),

    # Direita
    if ord(col) < ord(col_topo):
        adjacentes += cria_intersecao(chr(ord(col) + 1), linha),
    
    # Cima
    if linha < linha_topo:
        adjacentes += cria_intersecao(col, linha + 1),

    return adjacentes


def ordena_intersecoes(tuplo):
    """
    Ordenação de um tuplo de interseções de acordo com a ordem de leitura
    de um tabuleiro de Go

    Pârametros:
        tuplo(tuplo): Tuplo com várias interseções
        
    Retorna:
        tuple: Tuplo de interseções ordenadas
    """
    return tuple(sorted(tuplo, key=lambda x: (obtem_lin(x), obtem_col(x))))


# TAD Pedra

# Construtor

def cria_pedra_branca():
    """
    Criação da pedra pertecente ao jogador branco

    Pârametros:
        None

    Retorna:
        str: Pedra pertencente ao jogador branco
    """
    return 'O'


def cria_pedra_preta():
    """
    Criação da pedra pertecente ao jogador preto

    Pârametros:
        None

    Retorna:
        str: Pedra pertencente ao jogador preto
    """
    return 'X'


def cria_pedra_neutra():
    """
    Criação de uma pedra neutra

    Pârametros:
        None

    Retorna:
        str: Pedra não pertencente a nenhum dos jogadores
    """
    return '.'


# Reconhecedor

def eh_pedra(arg):
    """
    Verficação se um argumento é uma pedra

    Pârametros:
        arg(any): Argumento a ser testado

    Retorna:
        boolean: Validade do argumento ser uma pedra
    """
    return arg in (cria_pedra_branca(), cria_pedra_neutra(), cria_pedra_preta())


def eh_pedra_branca(pedra):
    """
    Verficação se um argumento é uma pedra branca

    Pârametros:
        pedra(any): Pedra a ser testada

    Retorna:
        boolean: Validade do argumento ser uma pedra branca
    """
    return pedra == cria_pedra_branca() and eh_pedra(pedra)


def eh_pedra_preta(pedra):
    """
    Verficação se um argumento é uma pedra preta

    Pârametros:
        pedra(any): Pedra a ser testada

    Retorna:
        boolean: Validade do argumento ser uma pedra preta
    """
    return pedra == cria_pedra_preta() and eh_pedra(pedra)


# Teste

def pedras_iguais(p1, p2):
    """
    Verficação se as pedras são iguais

    Pârametros:
        p1(any): Pedra a ser testada
        p2(any): Pedra a ser testada

    Retorna:
        boolean: Validade das pedras serem iguais
    """
    if not eh_pedra(p1) or not eh_pedra(p2):
        return False
    return p1 == p2


# Transformador

def pedra_para_str(pedra):
    """
    Transformar uma pedra em um string

    Pârametros:
        pedra(any): Pedra a ser transformada

    Retorna:
        str: Pedra em string
    """
    return str(pedra)


# FAN

def eh_pedra_jogador(pedra):
    """
    Verificação se uma pedra é de um jogador

    Pârametros:
        pedra(any): Pedra a ser testada

    Retorna:
        boolean: Validade da pedra ser de um jogador
    """
    return eh_pedra_branca(pedra) or eh_pedra_preta(pedra)


# TAD goban

# Construtor

def cria_goban_vazio(n):
    """
    Criação de um goban vazio

    Pârametros:
        n(int): Comprimento e largura do tabuleiro de Go

    Retorna:
        goban(list): goban vazio 
    """
    # Verificação dos valores de entrada
    if type(n) != int or n not in (9, 13, 19):
        raise ValueError('cria_goban_vazio: argumento invalido')
    return [[cria_pedra_neutra() for i in range(n)] for j in range(n)]


def cria_goban(n, brancas, pretas):
    """
    Criação de um goban com pedras

    Pârametros:
        n(int): Comprimento e largura do tabuleiro de Go
        brancas(tuplo): Tuplo com interseções das pedras brancas
        pretas(tuplo): Tuplo com interseções das pedras pretas

    Retorna:
        goban(list): goban com pedras 
    """
    # Verificação dos valores de entrada
    if type(n) != int or n not in (9, 13, 19):
        raise ValueError('cria_goban: argumentos invalidos')
    if type(brancas) != tuple or type(pretas) != tuple:
        raise ValueError('cria_goban: argumentos invalidos')

    # Criação de um goban vazio e colocação das pedras nele
    goban = cria_goban_vazio(n)

    for tipo in brancas, pretas:
        for intersecao in tipo:
            # Verificação dos valores de entrada
            if intersecao in brancas and intersecao in pretas:
                raise ValueError('cria_goban: argumentos invalidos')
            if not eh_intersecao(intersecao):
                raise ValueError('cria_goban: argumentos invalidos')
            if obtem_lin(intersecao) > n or ord(obtem_col(intersecao)) - 64 > n:
                raise ValueError('cria_goban: argumentos invalidos')
                
            coluna = ord(obtem_col(intersecao)) - 65
            linha = obtem_lin(intersecao) - 1

            if eh_pedra_jogador(goban[coluna][linha]):
                raise ValueError('cria_goban: argumentos invalidos')
            # Colocação das pedras consoante da sua origem
            if intersecao in brancas:
                goban[coluna][linha] = pedra_para_str(cria_pedra_branca())
            else:
                goban[coluna][linha] = pedra_para_str(cria_pedra_preta())

    return goban


def cria_copia_goban(goban):
    """
    Criação de uma cópia de um goban

    Pârametros:
        goban(lista): Goban a ser copiado

    Retorna:
        Copia do goban 
    """
    return [[col for col in linha] for linha in goban]

# Seletor

def obtem_ultima_intersecao(goban):
    """
    Obtém a interseção correspondente ao canto direito
    do tabuleiro de go

    Pârametros:
        goban(lista): Goban selecionado

    Retorna:
        Interseção do canto direito do tabuleiro 
    """
    return cria_intersecao(chr(len(goban) + 64), len(goban))


def obtem_pedra(goban, intersecao):
    """
    Obtém a pedra numa interseção do goban

    Pârametros:
        goban(lista): Goban selecionado
        intersecao(tuple): Intersecao selecionada

    Retorna:
        A pedra na interseção selecionada 
    """
    coluna = ord(obtem_col(intersecao)) - 65
    linha = obtem_lin(intersecao) - 1
    return goban[coluna][linha]


def obtem_cadeia(goban, intersecao):
    """
    Obtém o tuplo de interseções das pedras da cadeia
    que passam na intersecao selecionada

    Pârametros:
        goban(lista): Goban selecionado
        intersecao(tuple): Intersecao selecionada

    Retorna:
        Tuplo ordenado das pedras da cadeia que passam 
        pela interseção selecionada
    """

    pedra = obtem_pedra(goban, intersecao)
    adjacentes = (intersecao,)

    adicionado = True
    while adicionado:
        adicionado = False
        for inter in adjacentes:
            for elemento in obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(goban)):
                if pedras_iguais(obtem_pedra(goban, elemento), pedra) and elemento not in adjacentes:
                    adjacentes += (elemento,)
                    adicionado = True
    return ordena_intersecoes(adjacentes)

# Modificador

def coloca_pedra(goban, intersecao, pedra):
    """
    Modifica destrutivamente o goban selecionado, colocando
    a pedra dada na intersecao selecionada

    Pârametros:
        goban(lista): Goban selecionado
        intersecao(tuple): Intersecao selecionada
        pedra(pedra): Pedra

    Retorna:
        Goban modificado
    """
    coluna = ord(obtem_col(intersecao)) - 65
    linha = obtem_lin(intersecao) - 1
    goban[coluna][linha] = pedra
    return goban


def remove_pedra(goban, intersecao):
    """
    Modifica destrutivamente o goban selecionado, removendo
    a pedra na intersecao selecionada

    Pârametros:
        goban(lista): Goban selecionado
        intersecao(tuple): Intersecao selecionada

    Retorna:
        Goban modificado
    """
    coloca_pedra(goban,intersecao, pedra_para_str(cria_pedra_neutra()))
    return goban


def remove_cadeia(goban, intersecoes):
    """
    Modifica destrutivamente o goban selecionado, removendo as pedras
    nas interseções selecionadas

    Pârametros:
        goban(lista): Goban selecionado
        intersecoes(tuple): Tuplo de interseções

    Retorna:
        Goban modificado
    """
    for pedra in intersecoes:
        remove_pedra(goban, pedra)
    return goban

# Reconhecedor

def eh_goban(goban):
    """
    Verifica se o goban selecionado é, devidamente,
    um TAD goban

    Pârametros:
        goban(lista): Goban selecionado

    Retorna:
        boolean: Validade do goban
    """
    try:
        if type(goban) != list:
            return False
        if obtem_lin(obtem_ultima_intersecao(goban)) not in (9, 13, 19):
            return False
        for coluna in goban:
            if type(coluna) != list:
                return False
            if len(coluna) not in (9, 13, 19):
                return False
            if obtem_lin(obtem_ultima_intersecao(goban)) != len(coluna):
                return False
            for elemento in coluna:
                if not eh_pedra(elemento):
                    return False
    except ValueError:
        return False
    return True


def eh_intersecao_valida(goban, intersecao):
    """
    Verifica se uma interseção é válida num goban selecionado

    Pârametros:
        goban(lista): Goban selecionado
        intersecao(tuple): Interseção selecionada

    Retorna:
        boolean: Validade da interseção nesse território
    """

    tamanho = obtem_lin(obtem_ultima_intersecao(goban))

    # Verificação dos valores de entrada
    if not eh_intersecao(intersecao):
        return False
    if not (1 <= obtem_lin(intersecao) <= tamanho):
        return False
    if not 1 <= ord(obtem_col(intersecao)) - 64 <= tamanho:
        return False
    return True

# Teste

def gobans_iguais(g1, g2):
    """
    Verifica se dois gobans são iguais

    Pârametros:
        g1(lista): Goban selecionado
        g2(lista): Goban selecionado

    Retorna:
        boolean: Igualdade entre os dois gobans
    """
    # Verificação dos valores de entrada
    if not (eh_goban(g1) and eh_goban(g2)):
        return False

    tamanho1 = obtem_lin(obtem_ultima_intersecao(g1))
    tamanho2 = obtem_lin(obtem_ultima_intersecao(g2))

    if tamanho1 != tamanho2:
        return False

    for i in range(tamanho1):
        coluna = chr(65 + i)
        for k in range(tamanho1):
            linha = k + 1
            intersecao = cria_intersecao(coluna, linha)
            pedra_1 = obtem_pedra(g1, intersecao)
            pedra_2 = obtem_pedra(g2, intersecao)

            if not eh_pedra(pedra_1) or not eh_pedra(pedra_2):
                return False
            if not pedras_iguais(pedra_1, pedra_2):
                return False
    return True

# Transformador

def goban_para_str(goban):
    """
    Transforma um goban em uma string 

    Pârametros:
        goban(lista): Goban selecionado

    Retorna:
        str: Goban em string
    """
    tamanho = obtem_lin(obtem_ultima_intersecao(goban))
    contador = 0
    goban_str = '  '

    # Criação da linha de letras
    while contador < tamanho:
        goban_str += ' ' + chr(65 + contador)
        contador += 1

    linha_letras = goban_str
    goban_str += '\n'

    # Criação dos números e das linhas/colunas do goban
    for numero in range(tamanho - 1, -1, -1):
        pedras = ''
        for linha in goban:
            pedras += ' ' + linha[numero]
        if numero + 1 < 10:
            pedras = ' ' + str(numero + 1) + pedras + '  ' + str(numero + 1) + '\n'
        else:
            pedras = str(numero + 1) + pedras + ' ' + str(numero + 1) + '\n'
        goban_str += pedras

    goban_str += linha_letras

    return goban_str

# FAN

def obtem_territorios(goban):
    """
    Obtém os territórios de um goban 

    Pârametros:
        goban(lista): Goban selecionado

    Retorna:
        tuple: Tuplo com os territórios de um goban
    """

    tamanho = obtem_lin(obtem_ultima_intersecao(goban))
    final = ()
    adicionados = ()
    
    for num in range(tamanho):
        for letra in range(tamanho):

            intersecao = cria_intersecao(chr(letra + 65), num + 1)
            pedra = obtem_pedra(goban, intersecao)

            # Se a pedra na interseção é neutra e a interseção a ser testada
            # ainda não foi adicionada, vamos adicionar a cadeia dessa interseção
            if not eh_pedra_jogador(pedra) and intersecao not in adicionados:
                    cadeia = obtem_cadeia(goban, intersecao)
                    adicionados += cadeia
                    final += cadeia,
    return final


def obtem_adjacentes_diferentes(goban, intersecoes):
    """
    Obtém os adjacentes diferentes

    Pârametros:
        goban(lista): Goban selecionado
        intersecoes(tuple): Tuplo de interseções

    Retorna:
        tuple: Tuplo com os adjacentes diferentes ordenados
    """

    final = ()

    for intersecao in intersecoes:
        pedra = False
        # Se a pedra da interseção é de um jogador, tornamos a flag pedra True
        # Dizendo nos que estamos a tratar de pedras de jogadores
        if eh_pedra_jogador(obtem_pedra(goban, intersecao)):
            pedra = True

        # Para cada adjacente às nossas interseções, verificamos se
        # são pedras
        for adjacente in obtem_intersecoes_adjacentes(intersecao,obtem_ultima_intersecao(goban)):
            if adjacente not in final:
                if not eh_pedra_jogador(obtem_pedra(goban, adjacente)) and pedra:
                    final += adjacente,

                elif eh_pedra_jogador(obtem_pedra(goban, adjacente)) and not pedra:
                    final += adjacente,

    return ordena_intersecoes(final)


def jogada(goban, intersecao, pedra):
    """
    Modifica destrutivamente o goban selecionado com a pedra
    do jogador na intersecao selecionada 

    Pârametros:
        goban(lista): Goban selecionado
        intersecao(tuplo): Interseção selecionada
        pedra(pedra): Pedra do jogador

    Retorna:
        Goban modificado
    """
    # Colocamos a pedra na interseção 
    coloca_pedra(goban, intersecao, pedra)

    # No caso das pedras do adversário ficarem sem liberdades
    # Removêmo-las
    for adjacente in obtem_intersecoes_adjacentes(intersecao, obtem_ultima_intersecao(goban)):
        # Se alguma das pedras adjacentes à colocada for do outro jogador, verificamos se
        # a cadeia dessas pedras tem liberdades, caso não tenha, removêmo-la 
        if not pedras_iguais(obtem_pedra(goban, adjacente), pedra) and eh_pedra_jogador(obtem_pedra(goban, adjacente)):
            cadeia = obtem_cadeia(goban, adjacente)

            if obtem_adjacentes_diferentes(goban, cadeia) == ():
                remove_cadeia(goban, cadeia)

    return goban


def obtem_pedras_jogadores(goban):
    """
    Obtém o número de pedras brancas e pretas 

    Pârametros:
        goban(lista): Goban selecionado

    Retorna:
        tuple: Tuplo com o número de pedras brancas e pretas, respetivamente.
    """

    tamanho_goban = obtem_lin(obtem_ultima_intersecao(goban))
    brancas = 0
    pretas = 0

    # Contamos o número de pedras de jogador, interseção a interseção
    for coluna in range(tamanho_goban):
        for linha in range(tamanho_goban):
            intersecao = cria_intersecao(chr(coluna + 65), linha + 1)
            if eh_pedra_branca(obtem_pedra(goban, intersecao)):
                brancas += 1
            elif eh_pedra_preta(obtem_pedra(goban, intersecao)):
                pretas += 1
    return brancas, pretas

# Funções Adicionais

def calcula_pontos(goban):
    """
    Calcula os pontos num goban

    Pârametros:
        goban(lista): Goban selecionado

    Retorna:
        tuple: Tuplo com os pontos das brancas e pretas, respetivamente.
    """
    if obtem_pedras_jogadores(goban) == (0, 0):
        return 0, 0

    todos_territorios = [territorio for territorio in obtem_territorios(goban)]
    brancas = obtem_pedras_jogadores(goban)[0]
    pretas = obtem_pedras_jogadores(goban)[1]

    for territorio in todos_territorios:
        fronteira = obtem_adjacentes_diferentes(goban, territorio)
        pedra_tipo = obtem_pedra(goban, fronteira[0])
        count = 0

        # Para cada intersecao da fronteira, verificamos se sao todas do mesmo tipo de pedra
        for intersecao in fronteira:
            if pedras_iguais(pedra_tipo, obtem_pedra(goban, intersecao)):
                count += 1
        # Se todas as pedras da fronteira forem iguais, o tamanho
        # da fronteira será igual ao contador anterior, então verificamos
        # que tipo de pedra é e adicionamos o tamanho do território
        if len(fronteira) == count:
            if eh_pedra_branca(pedra_tipo):
                brancas += len(territorio)
            else:
                pretas += len(territorio)
    return brancas, pretas


def eh_jogada_legal(goban, intersecao, pedra, l):
    """
    Verifica a validade de uma jogada num goban

    Pârametros:
        goban(lista): Goban selecionado
        intersecao(tuplo): Interseção selecionada
        pedra(pedra): Pedra do jogador
        l(lista): Estado do tabuleiro que não pode ser obtido

    Retorna:
        boolean: Validade da jogada no goban selecionado
    """
    # Verificação dos valores de entrada
    if not eh_intersecao_valida(goban, intersecao):
        return False
    if eh_pedra_jogador(obtem_pedra(goban, intersecao)):
        return False
    
    # Criação de um novo goban e fazendo a jogada nele
    novo_goban = cria_copia_goban(goban)
    jogada(novo_goban, intersecao, pedra)

    # Verificação da regra de suicídio
    cadeia = [inter for inter in obtem_cadeia(novo_goban, intersecao)]
    liberdades = [lib for lib in obtem_adjacentes_diferentes(novo_goban, cadeia)]

    if len(liberdades) == 0:
        return False

    # Verificação da regra da Repetição
    if gobans_iguais(novo_goban, l):
        return False

    return True


def turno_jogador(goban, pedra, l):
    """
    Obtém a escolha do jogador em relação à sua jogada

    Pârametros:
        goban(lista): Goban selecionado
        pedra(pedra): Pedra do jogador
        l(lista): Estado do tabuleiro que não pode ser obtido

    Retorna:
        boolean: Devolve False caso o jogador tenha passado e
                 True caso o jogador tenha jogado legalmente
    """
    # Usamos um loop que para apenas quando o jogador
    # Passa ou faz uma jogada legal
    while True:
        try:
            resposta = input(f"Escreva uma intersecao ou 'P' para passar [{pedra_para_str(pedra)}]:")
            if resposta == "P":
                return False
            intersecao = str_para_intersecao(resposta)
            if eh_jogada_legal(goban, intersecao, pedra, l):
                jogada(goban, intersecao, pedra)
                break
            else:
                continue
        except ValueError:
            continue
    return True


def go(n, tuplo_brancas, tuplo_pretas):
    """
    Função que permite jogar um jogo de Go total

    Pârametros:
        goban(lista): Goban selecionado
        tuplo_brancas(tuplo): Tuplo de interseções com pedras brancas
        tuplo_brancas(tuplo): Tuplo de interseções com pedras pretas

    Retorna:
        boolean: True caso o jogador branco ganhe, False caso o contrário
    """
    # Verificação dos valores de entrada
    if type(tuplo_brancas) != tuple or type(tuplo_pretas) != tuple:
        raise ValueError('go: argumentos invalidos')

    try:
        brancos = tuple([str_para_intersecao(i) for i in tuplo_brancas])
        pretos = tuple([str_para_intersecao(i) for i in tuplo_pretas])
        goban = cria_goban(n, brancos, pretos)

    except ValueError:
        raise ValueError('go: argumentos invalidos')
    except TypeError:
        raise ValueError('go: argumentos invalidos')
    
    # Criamos duas cópias para verificar ambas na jogada das
    # pedras pretas e pedras brancas
    contador_pass = 0
    copia = cria_copia_goban(goban)

    # Enquanto ambos não passarem a vez ('P'), continuamos a jogar
    while contador_pass != 2:
        l = cria_copia_goban(goban)
        for pedra in (cria_pedra_preta(),cria_pedra_branca()):

            print(f"Branco ({pedra_para_str(cria_pedra_branca())}) tem {calcula_pontos(goban)[0]} pontos")
            print(f"Preto ({pedra_para_str(cria_pedra_preta())}) tem {calcula_pontos(goban)[1]} pontos")
            print(goban_para_str(goban))

            if eh_pedra_preta(pedra):
                jogada = turno_jogador(goban, pedra, copia)
                copia = cria_copia_goban(goban)
            else:
                jogada = turno_jogador(goban, pedra, l)

            if jogada:
                contador_pass = 0
            else:
                contador_pass += 1
            if contador_pass == 2:
                break

    print(f"Branco ({pedra_para_str(cria_pedra_branca())}) tem {calcula_pontos(goban)[0]} pontos")
    print(f"Preto ({pedra_para_str(cria_pedra_preta())}) tem {calcula_pontos(goban)[1]} pontos")
    print(goban_para_str(goban))

    return calcula_pontos(goban)[0] > calcula_pontos(goban)[1]
