grammar for;

// =========================================================
// REGLAS DEL PARSER (Sintaxis y estructura del código)
// =========================================================

programa: (sentencia)* ;

sentencia
    : asignacion
    | cicloFor 
    ;

asignacion
    : ID ASIG expresion PUNTO_COMA 
    ;

cicloFor
    : 'for' P_ABRIR inicializacion PUNTO_COMA condicion PUNTO_COMA paso P_CERRAR LL_ABRIR programa LL_CERRAR
    ;

inicializacion
    : asignacionSimple 
    | /* vacío */
    ;

paso
    : ID (INCREMENTO | DECREMENTO)
    | asignacionSimple
    ;

asignacionSimple
    : ID ASIG expresion
    ;

condicion
    : expresion MAYOR expresion      # MayorQue
    | expresion MENOR expresion     # MenorQue
    | expresion IGUAL_A expresion   # IgualA
    ;

// Regla ÚNICA de Expresión con Precedencia (La forma recomendada en ANTLR4)
expresion
    : expresion MULT expresion      # Multiplicacion
    | expresion DIV expresion       # Division
    | expresion SUMA expresion      # Suma
    | expresion RESTA expresion     # Resta
    | P_ABRIR expresion P_CERRAR    # Parentesis
    | ID                            # Identificador
    | NUM                           # Numero
    ;


// =========================================================
// REGLAS DEL LEXER (Tokens y reconocimiento de caracteres)
// =========================================================

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUM: [0-9]+;

// Operadores y Puntuación
ASIG: '=';

MAYOR: '>';
MENOR: '<';
IGUAL_A: '==';

SUMA: '+';
RESTA: '-';
MULT: '*';
DIV: '/';

INCREMENTO: '++';
DECREMENTO: '--';

P_ABRIR: '(';
P_CERRAR: ')';
LL_ABRIR: '{';
LL_CERRAR: '}';
PUNTO_COMA: ';';

// Espacios en Blanco (Corregido)
WS: [ \t\r\n]+ -> skip;