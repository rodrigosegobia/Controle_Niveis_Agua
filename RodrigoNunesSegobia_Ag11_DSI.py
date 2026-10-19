from colorama import Fore, Style


situacoes = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

cores = [
    Fore.RED,
    Fore.YELLOW,
    Fore.GREEN,
    Fore.CYAN,
    Fore.BLUE
]


def definir_cor(nivel):

    if type(nivel) is not int or nivel < 1 or nivel > len(situacoes):
        return None

    return cores[nivel - 1]


def exibir_situacao(nivel):
    cor = definir_cor(nivel)

    if cor is None:
        print("Erro: nível inválido. Informe um número inteiro de 1 a 5.")
        return

    situacao = situacoes[nivel - 1]

    print(f"{cor}Nível {nivel}: {situacao}{Style.RESET_ALL}")


print(" || CONTROLE DE NÍVEIS DE ÁGUA ||")
print("\nSimulação do reservatório:\n")

for nivel_atual in range(1, len(situacoes) + 1):
    exibir_situacao(nivel_atual)

print("\nMonitoramento finalizado.")
