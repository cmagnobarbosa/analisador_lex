# Gerador de código

O gerador de código gera um código em uma versão simplificada de assembly.

Soma - > Add

subtração -> Sub

Multiplicação -> Multi

Divisão -> Div

Load

Store

if -> beq


# Analisador Semântico

O analisador Semântico, realiza a verificação de tipos, cria tabela de simbolos.

*Geração de warning para variáveis não inicializadas.

# analisador Sintático

 a = 8 +8

 ID = NUM + NUM


Gramática

Programa -> **Declaracao**|**Atribuicao**|**Condicao**|**Repeticao**|$

Atribuicao ->
 id = **Expressao**;| **Programa**

Declaracao ->
**Tipo** id;|**tipo** **Atribuicao**|**Programa**

Tipo ->
int|float|char

Repeticao ->
while(**Expressao**){**Bloco**};|**Programa**

Expressao -> (**Expressao**);|**Programa**


condicao -> if(**Expressao**){**Bloco**};|**Programa**

Bloco -> **Programa**|$
