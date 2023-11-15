parser grammar PyParser;
options { tokenVocab=PyLexer; }

program
    : block EOF
    ;
    
block
    : (TAB* (statement | comment)+ NEWLINE*)*
    ;
      
statement
    : assignment 
    | if
    | while
    | for
    ;
         
assignment
    : lvalue ASSIGNMENT rvalue
    ;

if  : IF bexpr COLON NEWLINE block (elif | else)?
    ; 

elif: ELIF bexpr COLON NEWLINE block (elif | else)?
    ;

else: ELSE COLON NEWLINE block
    ;

while
    : WHILE bexpr COLON NEWLINE block
    ;

for : FOR lvalue IN iterable COLON NEWLINE block
    ;

iterable
    : lvalue
    | RANGE LPAR INT COMMA INT RPAR
    ;

bexpr
    : bexpr logic_op bexpr
    | LPAR bexpr RPAR
    | NOT bexpr
    | value
    ;
    
logic_op
    : OR
    | AND
    | CONDITION
    ;
          
lvalue
    : ID
    ;
      
rvalue
    : (value | expr | list)
    ;

list: LBRA rvalue ( COMMA rvalue)* RBRA
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
    | STRING
    | CHAR
    ;
    
number
    : INT
    | float
    ;
    
float
    : INT PERIOD INT 
    ;

comment
    : (COMMENT | BC)
    ;
 
