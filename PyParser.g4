parser grammar PyParser;
options { tokenVocab=PyLexer; }

program
    : block EOF?
    ;
    
block
    : ((statement | comment) TAB* NEWLINE*)* 
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

if  : IF bexpr COLON NEWLINE INDENT block DEDENT (elif | else)?
    ; 

elif: ELIF bexpr COLON NEWLINE INDENT block DEDENT (elif | else)?
    ;

else: ELSE COLON NEWLINE INDENT block DEDENT 
    ;

while
    : WHILE bexpr COLON NEWLINE INDENT block DEDENT 
    ;

for : FOR lvalue IN iterable COLON NEWLINE INDENT block DEDENT 
    ;

iterable
    : lvalue
    | RANGE LPAR INT COMMA INT RPAR
    ;

bexpr
    : bexpr logic_op bexpr
    | bexpr CONDITION bexpr
    | BOOL logic_op BOOL
    | value CONDITION value
    | LPAR bexpr RPAR
    | NOT bexpr
    | NOT value
    | BOOL
    ;
    
logic_op
    : OR
    | AND
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
 
