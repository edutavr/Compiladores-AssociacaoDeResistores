# Projeto da disciplina de Compiladores (2024.2) da Universidade de Pernambuco

## Objetivos do projeto:
  - Realização do cálculo da resistência equivalente da associação de resistores em série e/ou paralelo através da criação de uma gramática própria para isso, onde S representa a associação em série, e P, em paralelo;
  - Plotagem dos resistores associados entre si. (Obs.: Para rodar a plotagem do gráfico, através do matplotlib, é necessário baixar o código, pois o codespace do github não oferece suporte a essa biblioteca)

##

  Para rodar o código corretamente, siga os passos abaixo.

  1. **Instalação**:

```python
pip install antlr4-python3-runtime matplotlib
```
  2. **Execute o ANTLR**:

```py
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 Expressoes.g4
```
  3. **Inicie o arquivo 'Expressoes.py'**

