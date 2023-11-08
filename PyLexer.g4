lexer grammar PyLexer;
    
INT : [0-9]+ ;

BOOL 
    : 'True'
    | 'False'
    ;
    
STRING 
    : '"'[ -!#-&(-~]*'"';
    
CHAR
    : '\''[ -!#-&(-~]'\'';
    
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;

WS  : [ \r\f]+ -> skip ;

NEWLINE: '\n'
       ;
    
TAB : '    ' 
    | '\t' 
    ;
    
ASSIGNMENT : '='
           | '+='
           | '-='
           | '*='
           | '/='
           | '%='
           ;
           
OPERATOR: '+'
        | '-'
        | '*'
        | '/'
        | '%'
        ;

COMPARISON: '=='
          | '<='
          | '>='
          | '<'
          | '>'
          | 'not'
          | 'and'
          | 'or'
          ;
          
LBRA
    : '['
    ;

RBRA
    : ']'
    ;

LPAR
    : '('
    ;
    
RPAR
    : ')'
    ;

COMMA
    : ','
    ;
    
PERIOD
    : '.'
    ;



