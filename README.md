# Controle de Níveis de Água

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Colorama](https://img.shields.io/badge/Biblioteca-Colorama-00875A?style=for-the-badge)
![ETEC](https://img.shields.io/badge/ETEC-Agenda_11-B71C1C?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-2EA44F?style=for-the-badge)
[![GitHub](https://img.shields.io/badge/GitHub-Repositório-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rodrigosegobia/Controle_Niveis_Agua)

**Sistema de simulação e monitoramento dos níveis de água de um reservatório, desenvolvido em Python com a biblioteca Colorama.**

---

## Sobre o projeto

O **Controle de Níveis de Água** é uma aplicação desenvolvida em Python que simula o monitoramento de um reservatório, apresentando cinco níveis de água e suas respectivas condições.

O sistema utiliza mensagens coloridas no terminal para facilitar a identificação de cada situação, desde um nível criticamente baixo até um nível muito alto, que também exige atenção.

O projeto aplica conceitos de programação estruturada, utilizando listas, funções, estruturas condicionais, repetição e bibliotecas.

Desenvolvido como atividade prática da **Agenda 11 – Bibliotecas**, do curso Técnico em Desenvolvimento de Sistemas da ETEC.

## Objetivo

Demonstrar como bibliotecas e recursos da linguagem Python podem ser utilizados para construir um sistema de monitoramento simples, organizado e funcional.

A proposta é apresentar informações de maneira clara, utilizando cores para diferenciar as condições do reservatório e facilitar sua interpretação.

## Funcionalidades

- Monitoramento simulado de cinco níveis de água.
- Identificação das situações por cores.
- Classificação automática conforme o nível informado.
- Validação de valores inválidos.
- Exibição organizada das mensagens no terminal.
- Restauração automática do estilo original do terminal após cada mensagem válida.
- Execução automática, sem necessidade de inserir dados manualmente.

## Classificação dos níveis

O reservatório possui cinco classificações, cada uma associada a uma condição e uma cor específica.

| Nível | Situação | Cor | Identificação no código |
|:---:|---|---|---|
| **1** | Muito baixo (crítico) | Vermelho | `Fore.RED` |
| **2** | Baixo | Amarelo | `Fore.YELLOW` |
| **3** | Médio | Verde | `Fore.GREEN` |
| **4** | Alto | Ciano | `Fore.CYAN` |
| **5** | Muito alto (alerta) | Azul | `Fore.BLUE` |

**Importante:** os níveis 1 e 5 representam situações que exigem atenção. O primeiro indica um volume criticamente baixo, enquanto o último representa um volume muito alto.

## Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| **Python** | Linguagem utilizada no desenvolvimento do sistema |
| **Colorama** | Biblioteca responsável pelas cores exibidas no terminal |
| **Pip** | Gerenciamento e instalação da biblioteca externa |
| **GitHub** | Armazenamento e versionamento do código-fonte |

## Estrutura do projeto

```text
Controle_Niveis_Agua/
│
├── RodrigoNunesSegobia_Ag11_DSI.py
│
└── README.md
```

**RodrigoNunesSegobia_Ag11_DSI.py:** arquivo principal que contém toda a lógica do sistema.

**README.md:** documentação com as informações do projeto, instruções de execução e código-fonte.

---

## Instalação e execução

### 1. Pré-requisitos

Para executar o projeto, é necessário ter o Python instalado no computador e acesso a um terminal, como o PowerShell ou o terminal integrado do Visual Studio Code.

### 2. Instalação da biblioteca

A biblioteca Colorama não acompanha a instalação padrão do Python e precisa ser instalada separadamente.

No terminal, execute:

```bash
python -m pip install colorama
```

O comando utiliza o gerenciador de pacotes `pip` para instalar a biblioteca necessária.

### 3. Execução do programa

Com a biblioteca instalada, abra o terminal na pasta que contém o arquivo Python e execute:

```bash
python RodrigoNunesSegobia_Ag11_DSI.py
```

Após a execução, o sistema apresenta automaticamente todos os níveis do reservatório, com suas respectivas cores e classificações.

---

## Demonstração do sistema

A aplicação apresenta as seguintes informações no terminal:

```text
 || CONTROLE DE NÍVEIS DE ÁGUA ||

Simulação do reservatório:

Nível 1: Muito baixo (crítico)
Nível 2: Baixo
Nível 3: Médio
Nível 4: Alto
Nível 5: Muito alto (alerta)

Monitoramento finalizado.
```

Cada mensagem referente ao nível do reservatório é exibida com sua cor correspondente, conforme a classificação definida anteriormente.

O resultado apresentado acima demonstra o conteúdo textual. As cores são aplicadas durante a execução em um terminal compatível.

---

## Código-fonte completo

A implementação utiliza duas listas para organizar as situações e suas respectivas cores, além de duas funções responsáveis pela validação e apresentação das mensagens.

O código foi organizado para manter a leitura simples, evitar repetições desnecessárias e facilitar a manutenção.

**Arquivo:** `RodrigoNunesSegobia_Ag11_DSI.py`

```python
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
```

---

## Funcionamento do código

### Organização dos dados

O sistema utiliza duas listas principais:

- **`situacoes`:** armazena as cinco classificações possíveis do reservatório.
- **`cores`:** armazena as cores correspondentes, seguindo a mesma ordem das situações.

Essa organização permite relacionar cada nível à sua descrição e cor sem a necessidade de repetir várias condições no código.

### Função `definir_cor(nivel)`

Responsável por verificar se o nível informado é um número inteiro entre 1 e 5.

Quando o valor é válido, a função retorna a cor correspondente. Caso contrário, retorna `None`, indicando que o nível não pode ser utilizado.

### Função `exibir_situacao(nivel)`

Responsável por apresentar as informações no terminal.

Primeiro, a função solicita a cor do nível informado. Em seguida, verifica se o valor é válido e apresenta a descrição correspondente.

Após a mensagem, utiliza `Style.RESET_ALL` para restaurar o estilo padrão do terminal.

### Simulação automática

A estrutura de repetição `for` percorre os cinco níveis cadastrados, executando a função `exibir_situacao()` para cada um deles.

Dessa forma, todas as situações são demonstradas automaticamente, sem necessidade de entrada de dados.

---

## Validação e tratamento de situações inválidas

O programa possui uma validação simples para impedir que níveis inexistentes sejam utilizados.

| Situação | Comportamento |
|---|---|
| Nível entre 1 e 5 | Exibe a situação e a cor correspondente |
| Nível menor que 1 | Retorna uma mensagem de erro |
| Nível maior que 5 | Retorna uma mensagem de erro |
| Valor não inteiro | Considera o valor inválido |
| Nível válido | Restaura o estilo após a mensagem |

A função de validação também evita que valores fora do intervalo permitido sejam utilizados para acessar posições inexistentes nas listas.

Esse cuidado contribui para a previsibilidade do programa e permite que sua lógica seja reaproveitada em futuras adaptações.

---

## Limitações da simulação

O sistema foi desenvolvido para fins educacionais e demonstra o funcionamento de um monitoramento por níveis previamente definidos.

Por esse motivo, não realiza medições reais de água, não utiliza sensores e não recebe informações de dispositivos externos.

A simulação percorre automaticamente os cinco níveis, demonstrando suas classificações e as cores utilizadas em cada situação.

---

## Considerações finais

O desenvolvimento do Controle de Níveis de Água demonstra a utilização de bibliotecas externas em conjunto com conceitos fundamentais da programação estruturada.

A biblioteca Colorama permite melhorar a apresentação das informações, enquanto o uso de listas, funções e estruturas de controle mantém o código organizado e de fácil compreensão.

A solução atende à proposta da atividade, apresentando um sistema simples, funcional e adequado aos conhecimentos estudados na Agenda 11.

---

## Informações acadêmicas

| Informação | Descrição |
|---|---|
| **Instituição** | ETEC – Escola Técnica Estadual |
| **Curso** | Técnico em Desenvolvimento de Sistemas |
| **Componente** | Desenvolvimento de Sistemas I |
| **Agenda** | 11 – Bibliotecas |
| **Atividade** | Controle de Níveis de Água |
| **Desenvolvedor** | Rodrigo Nunes Segobia |

---

### Repositório e desenvolvimento

Projeto acadêmico desenvolvido para aplicação prática dos conhecimentos de programação em Python.

[![GitHub](https://img.shields.io/badge/Ver_repositório-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rodrigosegobia/Controle_Niveis_Agua)
[![Perfil](https://img.shields.io/badge/Desenvolvedor-Rodrigo_Segobia-3776AB?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rodrigosegobia)

**Rodrigo Nunes Segobia | ETEC – Desenvolvimento de Sistemas I**
