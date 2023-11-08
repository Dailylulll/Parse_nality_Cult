lexer grammar PyLexer;

WS  : [ \r\f]+ -> skip ;

NEWLINE
    : '\n'
    ;
    
TAB : '    ' 
    | '\t' 
    ;
    
ASSIGNMENT 
    : '='
    | '+='
    | '-='
    | '*='
    | '/='
    | '%='
    ;
           
OPERATOR
    : '+'
    | '-'
    | '*'
    | '/'
    | '%'
    ;

CONDITION
    : '=='
    | '!='
    | '<='
    | '>='
    | '<'
    | '>'
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

COLON
    : ':'
    ;

POUND
    : '#'
    ;

IF  : 'if'
    ;

ELIF: 'elif'
    ;

ELSE: 'else'
    ;

FOR : 'for'
    ;

WHILE
    : 'while'
    ;

RANGE
    : 'range'
    ;

IN  : 'in'
    ;
    
NOT : 'not'
    ;
    
AND : 'and'
    ;
    
OR  : 'or'
    ;

TICK3
    : '\'\'\''
    ;
   
fragment 
NEG : '-'
    |
    ;
    
fragment
DIGIT
    : [0-9]
    ;
    
INT : NEG DIGIT+ ;

BOOL 
    : 'True'
    | 'False'
    ;
    
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
    
CHAR: '\''[ -!#-&(-~]'\''
    ;
    
STRING
    : '"'[ -!#-&(-~]*'"'
    ;
    
CHAR_SET
    : [ -!#-&(-~]
    ;

