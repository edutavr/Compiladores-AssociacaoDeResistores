import sys
from antlr4 import *
from ExpressoesLexer import ExpressoesLexer
from ExpressoesParser import ExpressoesParser
from plotagem import Circuit 

resistores = []
# Avaliar expressões
def avalieExp(exp):
    if exp.getChildCount() == 1:  # Nó folha (NUMBER)
        return parse_number_with_unit(exp.getText())
    elif exp.getChildCount() == 3:  # Operações binárias ou parênteses
        if exp.getChild(1).getText() == 'S':  # Operação Série
            v1 = avalieExp(exp.getChild(0))
            v2 = avalieExp(exp.getChild(2))
            return v1 + v2
        elif exp.getChild(1).getText() == 'P':  # Operação Paralelo
            v1 = avalieExp(exp.getChild(0))
            v2 = avalieExp(exp.getChild(2))
            return 1 / (1 / v1 + 1 / v2)
        elif exp.getChild(0).getText() == '(' and exp.getChild(2).getText() == ')':  # Parêntese
            return avalieExp(exp.getChild(1))
    raise Exception("Não sei avaliar a expressão: " + exp.toStringTree())

# Função para interpretar números com sufixos
def parse_number_with_unit(number_str):
    import re

    resistores.append(number_str)
    # Verifica se há uma unidade no final
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


# Imprimir expressão de forma hierárquica
def imprimeExp(exp, indent=""):
    if exp.getChildCount() == 1:  # Nó folha (NUMBER)
        print(indent + "Resistor: " + exp.getText() + " Ω")
    elif exp.getChildCount() == 3:  # Operações binárias ou parênteses
        if exp.getChild(1).getText() == 'S':  # Operação Série
            print(indent + "Série")
            imprimeExp(exp.getChild(0), indent + "|  ")
            imprimeExp(exp.getChild(2), indent + "|  ")
        elif exp.getChild(1).getText() == 'P':  # Operação Paralelo
            print(indent + "Paralelo")
            imprimeExp(exp.getChild(0), indent + "|  ")
            imprimeExp(exp.getChild(2), indent + "|  ")
        elif exp.getChild(0).getText() == '(' and exp.getChild(2).getText() == ')':  # Parêntese
            print(indent + "Parêntese:")
            imprimeExp(exp.getChild(1), indent + "|  ")

expression = "20S5S30S4MS1m"
lexer = ExpressoesLexer(InputStream(expression))
stream = CommonTokenStream(lexer)
parser = ExpressoesParser(stream)
tree = parser.expr()

if parser.getNumberOfSyntaxErrors() > 0:
    print("Erro sintático")
    sys.exit(1)

print("ok")

# Imprime a estrutura hierárquica
print("\nEstrutura da expressão:")
imprimeExp(tree)

# Avalia a expressão
result = avalieExp(tree)

# Teste com uma expressão de resistores

print(f"\nResultado: {result} Ω")

circuito = Circuit(resistores)
circuito.draw()