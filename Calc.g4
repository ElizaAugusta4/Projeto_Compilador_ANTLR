grammar Calc;

prog: stat+ ;

stat: 'let' ID '=' expr ';' # VarDeclaration | expr # Expression ;

expr: expr ('*' | '/') expr                # MulDiv
    | expr ('+' | '-') expr                # AddSub
    | '(' expr ')'                         # Parens
    | ID                                   # Var
    | INT                                  # Int
    | '(' expr '>' expr ')' '?' expr ':' expr  # Ternary
    ;

MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
ID  : [a-zA-Z]+ ;
INT : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip ;