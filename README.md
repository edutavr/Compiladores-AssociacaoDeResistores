# Projeto da disciplina de Compiladores (2024.2) da Universidade de Pernambuco

## Objetivos do projeto
  - Realização do cálculo da resistência equivalente da associação de resistores em série e/ou paralelo através da criação de uma gramática própria para isso, onde S representa a associação em série e P, em paralelo;<br/><br/>
  - Plotagem dos resistores associados entre si. (Obs.: Para rodar a plotagem do gráfico, através do matplotlib, é necessário baixar o código, pois o codespace do github não oferece suporte a essa biblioteca)

## Funcionamento do código
  - Na gramática ANTLR, são definidas as regras sintáticas e léxicas, de modo que são permitidas expressões utilizando parênteses e que, entre elas pode-se optar pelo operador 'P' ou pelo operador 'S' (circuito em paralelo ou em série). São definidas também diferentes unidades, que podem ser 'm', 'M', 'k' ou 'K'. Ademais, são permitidos números decimais na entrada do valor dos resistores;<br/><br/>
  - No código principal, foi implementada uma árvore binária para representar e avaliar expressões de resistores em série e paralelo. Cada nó da árvore corresponde a uma subexpressão, e as folhas da árvore correspondem a números (resistências). O código irá imprimir a estrutura hierárquica e irá calcular o valor da resistência equivalente, a exibindo no console.<br/>
      **Exemplo de funcionamento:**<br/>
      Para a expressão 20S5P30, a arvore binária correspondente será:
     ``` 
    Paralelo
    |  Série
    |  |  Resistor: 20 Ω
    |  |  Resistor: 5 Ω
    |  Resistor: 30 Ω
     ```
      Ainda tratando do código principal, o mesmo irá chamar o a classe Circuit do arquivo plotagem.py, para, através do matplotlib, retornar o desenho esquematizado do circuito elétrico. Em resumo, plotagem.py calcula as posições dos componentes do circuito em uma primeira passagem e, em seguida, desenha esses componentes na segunda passagem, gerando uma visualização gráfica do circuito elétrico com resistores em série e paralelo.

  ## Instruções para rodar o código
  1. **Instalação**:

```python
pip install antlr4-python3-runtime matplotlib
```
  2. **Execute o ANTLR**:

```py
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 Expressoes.g4
```
  3. **Inicie o arquivo 'Expressoes.py'**

  ## Autores do Projeto

  - Eduardo Távora Rocha
  - Felipe Romero Pachecho Segundo
