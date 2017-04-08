# coding:utf-8
import sys
import re

def gera_marcador(elemento):
    if elemento is " ":
        return "|Sep, Space"
    else:
        return "|Sep, "+str(elemento)

def formata_tokens(tokens):
    novos=tokens.split("|")
    for i in novos:
        print "<",i,">"
arquivo = open("teste.c", "r")

token = ""
numerico = ""
estado = 0
separadores = [';', '\\', '\n','[', ']', ')', '(', ')', '{', '}', ',', '=']
operadores = ['-', '+', '/', '*']
op_log = ['&&', '||', '>', '<', '>=', '<=', '==', '!=']
lista_erros = []
Identificador=[]
linha = 0
final =""
for i in arquivo:
    linha = linha + 1
    final = ""
    for k in i:
        # print "Letra ",k
        if estado is 0:
            """Define o estado inicial"""
            if re.match(r"([A-Za-z_])", k):
                #token = token + k
                estado = 1  # Identificador

            if re.match(r"[0-9]", k):
                    estado = 2  # Constante Numerica
            if k in operadores:
                print "entrou"
                print k
        if estado is 1:

            """Valida Identificador"""
            if re.match(r"([\w])", k):
                token = token + k
            if k in separadores or re.match(r"(\s)",k):
                """Lista com separadores"""
                estado = 0
                token = "|Iden, "+token + ", L:"+str(linha) + gera_marcador(k)+ ", L:" + str(linha)+"|"

        if estado is 2:
            """Estado de indentificacao de constante numerica"""
            if re.match(r"[\w.]", k):
                numerico = numerico + k
            else:
                final = final + str(k)+", L:" + str(linha)+"|"
            if k in separadores or operadores:

                if(re.match(r"(^[0-9]*$|[0-9].[0-9]+)",numerico)):
                    valor = re.match(r"(^[0-9]*$|[0-9].[0-9]+)",numerico)
                    if valor is not None:
                        token = token + "|Num, "+valor.group()+",L:"+str(linha)+"|"
                        estado = 0
                        numerico = ""
                else:
                    lista_erros.append([numerico,linha])
                    numerico = ""
    token = token + final

formata_tokens(token)
print lista_erros
#print "Erro", lista_erros
