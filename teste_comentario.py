import re
"""Arquivo para testar uma implementação para ler comentario"""

arquivo = open("teste.c","r")

acumula = ""
estado = 0
for i in arquivo:
    for k in i:
        if k is "/" and i[1] is "*":
            estado = 1
        if estado is 1:
            acumula=acumula + k
            if re.search(r"\*\/",acumula):
                estado = 0
print acumula
