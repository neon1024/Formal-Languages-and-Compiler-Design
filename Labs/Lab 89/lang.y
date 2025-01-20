%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void yyerror(const char *s);
extern int yylex();
extern int currentLine;
%}

/* Declare a union for semantic values */
%union {
    int num;
    char* str;
}

/* Declare tokens and their types */
%token <str> IDENTIFIER STRING_CONST CHAR_CONST
%token <num> NUMBER_CONST
%token INPUT OUTPUT IF ELSE INT STRING CHAR RETURN MAIN
%token EQ NE LE GE

/* Precedence rules for operators */
%left '+' '-'
%left '*' '/'
%left EQ NE LE GE '<' '>'
%right '='

/* Declare non-terminal types */
%type <num> expression condition
%type <str> type

%%

/* Grammar rules */

program:
    MAIN '(' ')' '{' statement_list '}' { printf("Program parsed successfully.\n"); }
    ;

statement_list:
    statement
    | statement_list statement
    ;

statement:
    declaration ';'
    | assignment ';'
    | INPUT '(' STRING_CONST ')' '=' IDENTIFIER ';' { printf("Input assignment\n"); }
    | OUTPUT '(' IDENTIFIER ')' ';' { printf("Output statement\n"); }
    | IF '(' condition ')' '{' statement_list '}' ELSE '{' statement_list '}' { printf("If-else statement\n"); }
    ;

declaration:
    IDENTIFIER ':' type { printf("Declaration of %s with type %s\n", $1, $3); }
    | IDENTIFIER ':' type '=' expression { printf("Declaration and assignment of %s\n", $1); }
    ;

assignment:
    IDENTIFIER '=' expression { printf("Assignment to %s\n", $1); }
    ;

condition:
    expression '>' expression { printf("Condition: Greater than\n"); $$ = $1 > $3; }
    | expression '<' expression { printf("Condition: Less than\n"); $$ = $1 < $3; }
    | expression EQ expression { printf("Condition: Equals\n"); $$ = $1 == $3; }
    ;

expression:
    NUMBER_CONST { $$ = $1; }
    | IDENTIFIER { printf("Using variable %s\n", $1); $$ = 0; } /* Assuming variables are initialized to 0 for simplicity */
    | expression '+' expression { printf("Addition\n"); $$ = $1 + $3; }
    | expression '-' expression { printf("Subtraction\n"); $$ = $1 - $3; }
    | expression '*' expression { printf("Multiplication\n"); $$ = $1 * $3; }
    | expression '/' expression { printf("Division\n"); $$ = $1 / $3; }
    ;

type:
    INT { $$ = "int"; }
    | STRING { $$ = "string"; }
    | CHAR { $$ = "char"; }
    ;

%%

/* Error handling function */
void yyerror(const char *s)
{
    fprintf(stderr, "Error: %s at line %d\n", s, currentLine);
}

/* Main function */
int main()
{
    return yyparse();
}
