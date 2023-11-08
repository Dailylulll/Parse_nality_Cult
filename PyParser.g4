parser grammar PyParser;
options { tokenVocab=ExprLexer; }

program
    : block EOF
    ;
    
block 
    : statement
    ;
      
statement
    : assignment statement
    | NEWLINE statement
    |
    ;
         
assignment
    : lvalue ASSIGNMENT rvalue
    ;
          
lvalue
    : ID
    ;
      
rvalue
    : (value | expr | list) (NEWLINE | )
    ;

list: LBRA list_element RBRA
    ;

list_element
    : rvalue ( COMMA list_element | )
    ;
    
expr: expr OPERATOR expr
    | value
    | LPAR expr RPAR
    ;
    
value
    : ID
    | literal
    ;
    
literal
    : number
    | float
    | BOOL
    | CHAR
    | STRING
    ;
    
number
    : INT
    | float
    ;
    
float
    : INT PERIOD INT 
    ;

