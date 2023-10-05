
def usuario_escolhe_jogada(n, m):
    # Além dos parâmetros que traz valores externos, é necessário essa variável para dentro dessa função.
    """n = valor de peças que o tabuleiro começa, m = valor máximo de peças que podem ser retiradas por jogada."""
    a = int(input('informe quantos palitos deseja retirar: '))

    if m >= a > 0 and a <= n:
        return a
    else:
        print("O valor digitado é inválido, tente novamente!")
        while a > m or a <= 0 or a > n:
            a = int(input('informe quantos palitos deseja retirar: '))
            if (a > m or a <= 0) or a > n:
                print("O valor digitado é inválido, tente novamente!")
        return a


def computador_escolhe_jogada(n, m):
    k = 0
    i = 1
    while i <= m:
        if n - 1 != 0:
            if (n-i) % (m + 1) == 0:
                k = i
                i = m+1
            else:
                i = i + 1
        else:
            k = i
            i = m+1
    if k == 0:
        k = m
    print('computador joga: ', k)
    return k


def partida():
    """Se "n" for mutiplo de "m+1" o jogador começa (Estrategia vencedora)."""
    """Loop de jogadas entre usuário e computador."""

    n = int(input("Quantas peças? "))
    m = int(input('Limite de peças por jogada? '))

    if n < m or (n == 0 or m == 0):
        while n <= m or (n == 0 or m == 0):
            print("Valores inválidos!\nPor favor, tente novamente!")
            n = int(input("Quantas peças? "))
            m = int(input('Limite de peças por jogada? '))

    if n % (m+1) == 0:
        print('Você começa!')
        while n > 0:
            n = n - usuario_escolhe_jogada(n, m)
            print("Peças restantes", n)
            if n == 0:
                return print("Você ganhou!")
            else:
                if n > 0:
                    n = n - computador_escolhe_jogada(n, m)
                    if n == 0:
                        return print("computador ganhou!")
            print("Peças restantes", n)
    else:
        print('Computador começa!')
        while n > 0:
            n = n - (computador_escolhe_jogada(n, m))
            print("Peças restantes", n)
            if n == 0:
                return print("O computador ganhou!")
            else:
                if n > 0:
                    n = n - usuario_escolhe_jogada(n, m)
                    print("Peças restantes", n)
                    if n == 0:
                        return print("Você ganhou!")


def campeonato():
    usuario = 0
    computador = 0
    if partida() == "Você ganhou!":
        usuario = usuario + 1
        print("Você ganhou!")
    else:
        computador = computador + 1
    print("Placar: Você[{}] x [{}]Computador" .format(usuario, computador))

    if partida() == "Você ganhou!":
        usuario = usuario + 1
        print("Você ganhou!")
    else:
        computador = computador + 1
    print("Placar: Você[{}] x [{}]Computador" .format(usuario, computador))

    if partida() == "Você ganhou!":
        usuario = usuario + 1
        print("Você ganhou!")
    else:
        computador = computador + 1
    print("Placar: Você[{}] x [{}]Computador" .format(usuario, computador))

    print('**** Final do campeonato! ****')
    return 'Placar: Você {} X {} Computador'.format(usuario, computador)


def principal():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    modalidade = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n'))
    while modalidade > 2 or modalidade < 1:
        print('Valor inválido! Tente novamente')
        modalidade = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n'))
    if modalidade == 1:
        print('Você escolheu partida única!')
        partida()
    if modalidade == 2:
        print("Voce escolheu um campeonato!")
        campeonato()


if __name__ == '__main__':
    principal()
