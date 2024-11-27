grammar Expressoes;
// Regras sintáticas (parser rules)
expr: expr 'S' expr       # SeriesOperation
    | expr 'P' expr       # ParallelOperation
    | '(' expr ')'        # ParenthesizedExpression
    | NUMBER              # Number
    ;

// Regras léxicas (lexer rules)
NUMBER: [0-9]+ ('.' [0-9]+)? [mMkK]?; // Números com ou sem unidade

// Definição dos operadores e parênteses
S: 'S';                      // Operador Série
P: 'P';                      // Operador Paralelo
LPAREN: '(';                 // Parêntese esquerdo
RPAREN: ')';                 // Parêntese direito

// Ignorar espaços em branco
WS: [ \t\r\n]+ -> skip;