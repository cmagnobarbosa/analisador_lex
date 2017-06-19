# analisador Sintático

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
