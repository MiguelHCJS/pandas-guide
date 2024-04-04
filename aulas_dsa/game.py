import random
from os import system, name


def limpa_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == '__main__':
    ...
