def eh_territorio(territorio):
    """
    Verificamos se um território é válido

    Pârametros:
        territorio (tuplo): Território

    Retorna:
        booleano: Validade do território
    """

    # Verificamos os dados de entrada
    if type(territorio) != tuple or len(territorio) == 0:
        return False

    # Verificamos o primeiro tuplo para, em caso de erro, acontecer Short-Circuit
    if type(territorio[0]) != tuple or not (1 <= len(territorio) <= 26) or not (1 <= len(territorio[0]) <= 99):
        return False

    # Definimos fora do loop esta variável para apenas calcular o tamanho do 1ºtuplo uma única vez
    numeros_len = len(territorio[0])

    # Para cada tuplo no territorio
    for tuplo in territorio:
        # Verificamos se cada tuplo é devidamente um tuplo e se tem o mesmo tamanho que o primeiro
        if type(tuplo) != tuple or len(tuplo) != numeros_len:
            return False

        # Para cada intersecao em cada tuplo
        for intersecao in tuplo:
            # Verificamos se cada intersecao é devidamente uma interseção e se o seu valor é 0 ou 1
            if type(intersecao) != int or intersecao not in (0, 1):
                return False

    # Se nenhum dos pârametros falhar, devolvemos que o territorio fornecido é válido
    return True


def obtem_ultima_intersecao(territorio):
    """
    Descubrimos qual é a última interseção do território

    Pârametros:
        territorio (tuplo): Território

    Retorna:
        tuplo: Última interseção do território
    """

    # A letra associada à última interseção é dada através do número de tuplos do território
    # e do seu code point no Unicode (sendo 65 o code point da letra 'A')
    letra = chr(len(territorio) + 64)
    # O número associado à última interseção é igual ao tamanho do primeiro tuplo
    numero = len(territorio[0])

    # Tuplo com a última interseção
    return letra, numero


def eh_intersecao(intersecao):
    """
    Verificamos se uma interseção é válida

    Pârametros:
        intersecao (tuplo): Interseção

    Retorna:
        booleano: Validade da interseção
    """

    # Definição de todas as letras e números válidos
    # Letras são definidas consoante o seu code point no Unicode ('A' = 65 e 'Z' = 90)
    letras = [chr(i) for i in range(65, 91)]
    numeros = [i for i in range(1, 100)]

    # Validação dos valores de entrada
    if type(intersecao) != tuple or len(intersecao) != 2:
        return False
    # Verficação dos valores da interseção
    # Se é uma letra válida | Se é um número válido | Se o número é inteiro
    if intersecao[0] not in letras or intersecao[1] not in numeros or type(intersecao[1]) != int:
        return False

    # Validade da interseção
    return True


def eh_intersecao_valida(territorio, intersecao):
    """
    Verificamos se uma interseção é válida num território

    Pârametros:
        territorio (tuplo): Território
        intersecao (tuplo): Interseção

    Retorna:
        booleano: Validade da interseção nesse território
    """

    # Validação do valor de entrada
    if not eh_intersecao(intersecao):
        return False

    letra_intersecao = ord(intersecao[0]) - 64

    # Verificação se a letra da interseção está contida nas letras do território e
    # Verificação se o número da interseção está contido nos números do território
    if letra_intersecao <= len(territorio) and intersecao[1] <= len(territorio[0]):
        return True

    # Se as condições anteriores não forem cumpridas, devolvemos False
    return False


def eh_intersecao_livre(territorio, intersecao):
    """
    Verificamos se uma interseção é livre num território

    Pârametros:
        territorio (tuplo): Território
        intersecao (tuplo): Interseção

    Retorna:
        booleano: True se a interseção estiver livre, False se estiver ocupada
    """
    letra_intersecao = ord(intersecao[0]) - 65
    numero_intersecao = intersecao[1]

    # Verificamos se dentro do território, essa interseção corresponde a um
    # 0, sendo a interseção livre
    # 1, sendo a interseção ocupada por uma montanha
    if territorio[letra_intersecao][numero_intersecao-1] == 0:
        return True

    # Se as condições anteriores não forem cumpridas, devolvemos False
    return False


def obtem_intersecoes_adjacentes(territorio, intersecao):
    """
    Obtemos as interseções adjacentes a outra interseção

    Pârametros:
        territorio (tuplo): Território
        intersecao (tuplo): Interseção

    Retorna:
        tuple: Todas as interseções adjacentes válidas à interseção dada
    """

    # Número total de letras
    letras_len = len(territorio)
    # Número total de numeros
    numeros_len = len(territorio[0])
    # Letra da interseção em número
    letra = ord(intersecao[0]) - 64
    # Número da interseção
    numero = intersecao[1]

    # Tuplo das interseções adjacentes
    intersecoes_adjacentes = ()

    # Verificação se existe uma interseção abaixo da interseção dada
    if numero - 1 > 0:
        intersecoes_adjacentes = ((intersecao[0], numero - 1),)

    # Verificação se existe uma interseção à esquerda da interseção dada
    if letra - 1 > 0:
        intersecoes_adjacentes += ((chr(letra - 1 + 64), numero),)

    # Verificação se existe uma interseção à direita da interseção dada
    if letra + 1 <= letras_len:
        intersecoes_adjacentes += ((chr(letra + 1 + 64), numero),)

    # Verificação se existe uma interseção acima da interseção dada
    if numero + 1 <= numeros_len:
        intersecoes_adjacentes += ((intersecao[0], numero + 1),)

    return intersecoes_adjacentes


def ordena_intersecoes(territorio):
    """
    Ordenamos as interseções de um território

    Pârametros:
        territorio (tuplo): Território

    Retorna:
        tuple: Todas as interseções ordenadas por número e letra
    """

    # Ordenar a lista por números e de seguida por letras
    lista_ordenada = sorted(territorio, key=lambda x: (x[1], x[0]))
    return tuple(lista_ordenada)


def territorio_para_str(territorio):
    """
    Transformamos um território num string

    Pârametros:
        territorio (tuplo): Território

    Retorna:
        string: Território em string
    """
    # Verificação do valor de entrada
    if not eh_territorio(territorio):
        raise ValueError('territorio_para_str: argumento invalido')

    # Número de letras e números respetivamente
    letras_len = len(territorio)
    numeros_len = len(territorio[0])

    # Criação de um loop de maneira a criar um string com as letras do território
    contador = 0
    territorio_str = '  '
    while contador < letras_len:
        territorio_str += ' ' + chr(65 + contador)
        contador += 1
    # Armazenamos na variável linha_cima o valor da primeira linha do territorio para adicionar no final
    linha_cima = territorio_str
    territorio_str += '\n'

    # Criação de um loop, começando pelo fim dos números
    for numero in range(numeros_len - 1, -1, -1):
        # Variável que armazena o "relevo" do território
        relevo = ''
        # Criação de um loop, para cada linha do território
        for linha in territorio:
            if linha[numero] == 0:
                relevo += ' .'
            else:
                relevo += ' X'

        # Diferenciação entre a criação de strings quando o número é igual/superior a 10
        if numero + 1 < 10:
            relevo = ' ' + str(numero + 1) + relevo + '  ' + str(numero + 1) + '\n'
        else:
            relevo = str(numero + 1) + relevo + ' ' + str(numero + 1) + '\n'

        # Adicionamos o relevo ao territorio_str
        territorio_str += relevo
    # Adicionamos a linha de cima ao territorio
    territorio_str += linha_cima

    return territorio_str


def obtem_cadeia(territorio, intersecao):
    """
    Obtemos a cadeia em relação a uma interseção

    Pârametros:
        territorio (tuplo): Território
        intersecao (tuplo): Interseção

    Retorna:
        tuple: Todos os elementos da cadeia
    """
    # Validação dos valores de entrada
    if not eh_intersecao_valida(territorio, intersecao) or not eh_territorio(territorio):
        raise ValueError('obtem_cadeia: argumentos invalidos')

    adjacentes = (intersecao,)

    # Variável com referência do relevo da intersecao
    livre = False
    if eh_intersecao_livre(territorio, intersecao):
        livre = True

    # Variável booleana, sendo True enquanto forem adicionadas interseções à variável adjacentes
    adicionado = True
    # Criação de um loop
    while adicionado:
        # Flag fica com valor False
        adicionado = False
        # Criação de loop para cada elemento na variável "adjacentes"
        for intersecao_ in adjacentes:
            # Vamos buscar todos os adjacentes de cada intersecao na variável "adjacentes"

            # Para todas as interseções adjacentes de cada interseção em "adjacentes"
            for elemento in obtem_intersecoes_adjacentes(territorio, intersecao_):
                # Verificamos se o relevo de cada interseção é igual ao relevo da interseção dada
                # Se essa interseção não estiver nos adjacentes, adicionamo-la
                # Se algum elemento for adicionado, continuamos o loop
                if eh_intersecao_livre(territorio, elemento) == livre and elemento not in adjacentes:
                    adjacentes += (elemento,)
                    adicionado = True

    return ordena_intersecoes(adjacentes)


def obtem_vale(territorio, intersecao):
    """
    Obtemos os vales em relação a uma montanha

    Pârametros:
        territorio (tuplo): Território
        intersecao (tuplo): Interseção

    Retorna:
        tuple: Todos os vales
    """
    # Validação dos valores de entrada
    if not eh_intersecao_valida(territorio, intersecao) or not eh_territorio(territorio):
        raise ValueError('obtem_vale: argumentos invalidos')
    if eh_intersecao_livre(territorio, intersecao):
        raise ValueError('obtem_vale: argumentos invalidos')

    vales = ()

    # Criação de loop para cada elemento numa cadeia e para cada adjacente a esse elemento
    for elemento in obtem_cadeia(territorio, intersecao):
        for adjacente in obtem_intersecoes_adjacentes(territorio, elemento):
            # Para cada adjacente, verificamos se tem o mesmo relevo que a interseção dada
            # Verificamos se esse adjacente já está em "vales"
            if eh_intersecao_livre(territorio, adjacente) and adjacente not in vales:
                vales += (adjacente,)

    return ordena_intersecoes(vales)


def verifica_conexao(territorio, primeira_inter, segunda_inter):
    """
    Verificamos se duas interceções estão conectadas

    Pârametros:
        territorio (tuplo): Território
        primeira_inter (tuplo): Interseção
        segunda_inter (tuplo): Interseção

    Retorna:
        boolean: Validade da conexão
    """
    # Verificação dos valores de entrada
    if not (eh_intersecao_valida(territorio, primeira_inter) and eh_intersecao_valida(territorio, segunda_inter)):
        raise ValueError('verifica_conexao: argumentos invalidos')
    if not eh_territorio(territorio):
        raise ValueError('verifica_conexao: argumentos invalidos')

    # Criação de um loop, onde verificamos se a "segunda_inter" está na cadeia da "primeira_inter"
    for intersecao in obtem_cadeia(territorio, primeira_inter):
        if segunda_inter == intersecao:
            return True

    return False


def calcula_numero_montanhas(territorio):
    """
    Cálculo do número de montanhas de um território

    Pârametros:
        territorio (tuplo): Território

    Retorna:
        int: Número de montanhas de um território
    """
    # Verificação dos valores de entrada
    if not eh_territorio(territorio):
        raise ValueError('calcula_numero_montanhas: argumento invalido')

    numero_montanhas = 0
    # Criação de um loop, onde contamos o número de montanhas
    for tuplo in territorio:
        for intersecao in tuplo:
            if intersecao == 1:
                numero_montanhas += 1

    return numero_montanhas


def calcula_numero_cadeias_montanhas(territorio):
    """
     Cálculo do número de cadeias de montanhas de um território

     Pârametros:
         territorio (tuplo): Território

     Retorna:
         int: Número de cadeias de montanhas de um território
     """
    # Verificação dos valores de entrada
    if not eh_territorio(territorio):
        raise ValueError('calcula_numero_cadeias_montanhas: argumento invalido')

    # Definição de variáveis
    cadeias = ()
    numero_cadeias_m = 0
    letras_len = len(territorio)
    numeros_len = len(territorio[0])

    # Criação de um loop para verificar o território inteiro
    for letras in range(letras_len):
        for numeros in range(numeros_len):
            # Passagem de numerais para tuplos
            let = chr(65 + letras)
            num = numeros + 1
            # Verificação e contagem de cada interseção
            # Apenas fazemos a contagem das interseções que são montanhas e não estão em "cadeias"
            if (let, num) not in cadeias and territorio[letras][numeros] == 1:
                numero_cadeias_m += 1
                cadeias += obtem_cadeia(territorio, (let, num))

    return numero_cadeias_m


def calcula_tamanho_vales(territorio):
    """
     Cálculo do número de vales de um território

     Pârametros:
         territorio (tuplo): Território

     Retorna:
         int: Número de vales
     """
    # Verificação dos valores de entrada
    if not eh_territorio(territorio):
        raise ValueError('calcula_tamanho_vales: argumento invalido')

    # Definição de variáveis
    letras_len = len(territorio)
    numero_len = len(territorio[0])
    cadeias = ()
    montanhas = ()
    vales = ()

    # Criação de um loop para verificar o território inteiro
    for letras in range(letras_len):
        for numeros in range(numero_len):
            # Passagem de numerais para tuplos
            let = chr(65 + letras)
            num = numeros + 1
            # Para cada interseção que não está em "cadeias" e é uma montanha
            # Adicionamos essa cadeia a "cadeias" e essa interseção(montanha) a "montanhas"
            if (let, num) not in cadeias and territorio[letras][numeros] == 1:
                cadeias += (obtem_cadeia(territorio, (let, num)))
                montanhas += ((chr(65 + letras), numeros + 1),)
    
    # Criação de um loop para percorrer todas as montanhas em "montanhas"
    for cada_montanha in montanhas:
        todos_vales = obtem_vale(territorio, cada_montanha)
        # Criação de um loop para percorrer todos os vales em "todos_vales"
        for cada_vale in todos_vales:
            # Se esse vale ainda não foi adicionado, adicionamos a "vales"
            if cada_vale not in vales:
                vales += (cada_vale,)

    return len(vales)
