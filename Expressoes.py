import sys
from antlr4 import *
from ExpressoesLexer import ExpressoesLexer
from ExpressoesParser import ExpressoesParser
from plotagem import Circuit

niveis = {} # Dicionário para armazenar os níveis dos resistores

# Avaliar expressões
def avalieExp(exp):
    if exp.getChildCount() == 1:  # Nó folha (NUMBER)
        return parse_number_with_unit(exp.getText()), exp.getText()
    elif exp.getChildCount() == 3:  # Operações binárias ou parênteses
        if exp.getChild(1).getText() == 'S':  # Operação Série
            v1, comp1 = avalieExp(exp.getChild(0))
            v2, comp2 = avalieExp(exp.getChild(2))
            return v1 + v2, ["S", comp1, comp2]
        elif exp.getChild(1).getText() == 'P':  # Operação Paralelo
            v1, comp1 = avalieExp(exp.getChild(0))
            v2, comp2 = avalieExp(exp.getChild(2))
            return 1 / (1 / v1 + 1 / v2), ["P", comp1, comp2]
        elif exp.getChild(0).getText() == '(' and exp.getChild(2).getText() == ')':  # Parêntese
            return avalieExp(exp.getChild(1))
    raise Exception("Não sei avaliar a expressão: " + exp.toStringTree())

# Função para interpretar números com sufixos
def parse_number_with_unit(number_str):
    import re
    match = re.match(r"([0-9]+(?:\.[0-9]+)?)([mMkK]?)", number_str)
    if not match:
        raise ValueError(f"Número inválido: {number_str}")
    
    base_number = float(match.group(1))
    unit = match.group(2)

    # Converte baseado na unidade
    if unit == 'm':  # mili
        return base_number * 10**-3
    elif unit in ['k', 'K']:  # quilo
        return base_number * 10**3
    elif unit == 'M':  # mega
        return base_number * 10**6
    else:  # Sem unidade
        return base_number

def calcular_niveis(estrutura, nivel_ant=0, nivel_atual=0):
    # Se for um resistor (valor isolado), associar ao nível atual
    if isinstance(estrutura, str):
        nivel_atual = nivel_ant + 1
        niveis[estrutura] = (nivel_atual, nivel_ant)
        return nivel_atual

    # Se for uma associação, processar recursivamente
    if isinstance(estrutura, list):
        tipo = estrutura[0]  # Primeiro elemento define o tipo ('P' ou 'S')

        if tipo == 'S':  # Associação em série
            for sub_estrutura in estrutura[1:]:
                nivel_ant = calcular_niveis(sub_estrutura, nivel_ant, nivel_atual)
            return nivel_ant
        elif tipo == 'P':  # Associação em paralelo
            max_nivel = nivel_atual + 1
            sub_niveis = []
            for sub_estrutura in estrutura[1:]:
                sub_nivel = calcular_niveis(sub_estrutura, nivel_ant, nivel_atual)
                sub_niveis.append(sub_nivel)
            max_nivel = max(sub_niveis)
            for sub_estrutura in estrutura[1:]:
                if isinstance(sub_estrutura, str):
                    niveis[sub_estrutura] = (max_nivel, nivel_ant)
            return max_nivel

# Imprimir expressão de forma hierárquica
def imprimeExp(exp, indent=""):
    if isinstance(exp, str):  # Resistor individual
        print(indent + "Resistor: " + exp + " Ω")
    elif isinstance(exp, list):  # Estrutura complexa
        tipo = "Série" if exp[0] == "S" else "Paralelo"
        print(indent + tipo)
        for sub_exp in exp[1:]:
            imprimeExp(sub_exp, indent + "|  ")

expression = "(((10kP20k)S(5kP8k))P(2k))S(1K)S(7K)"
lexer = ExpressoesLexer(InputStream(expression))
stream = CommonTokenStream(lexer)
parser = ExpressoesParser(stream)
tree = parser.expr()

if parser.getNumberOfSyntaxErrors() > 0:
    print("Erro sintático")
    sys.exit(1)

# Avalia a expressão
result, structure = avalieExp(tree)

# Imprime a estrutura hierárquica
print("\nEstrutura da expressão:")
imprimeExp(structure)
print(structure, end="\n\n")
calcular_niveis(structure)
print(niveis)

print(f"\nResultado total: {result:.2f} Ω")

# Desenhar o circuito
circuito = Circuit(structure, niveis)
circuito.draw()