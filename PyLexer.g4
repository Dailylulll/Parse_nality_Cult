lexer grammar PyLexer;

WS  : [ \r\f]+ -> skip ;

NEWLINE
    : '\n'
    | '\r'
    ;

INDENT
    : 'indent'
    ;

DEDENT
    : 'dedent'
    ;
    
TAB :'    '
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
 
COMMENT
    : '#'+ .*? '\n'
    ;
    
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
    
CHAR: '\''[ -!#-&(-~]'\''
    ;
    
STRING
    : '"'~["]*'"'
    ;
BC
    : '\'\'\'' ( . | '\r' | '\n' )*? '\'\'\''
    ;
