# coding:utf-8
import sys
import re


def converte_simbolos():
    """Substitui simbolos por números"""
    pass


def gera_marcador(elemento):
    if elemento is " ":
        return "|Sep, Space"
    else:
        print "Tipo ", type(elemento)
        return "|Sep, " + elemento + "|"


def formata_tokens(tokens):
    print tokens
    novos = tokens.split("|")
    for i in novos:
        print "<", i, ">"
arquivo = open("teste.c", "r")

token = ""
numerico = ""
estado = 0
separadores = [';', '[', ']', ')', '(', ')', '{', '}', ',', '=', '.']
sep_num = [';',',', '=']
operadores = ['-', '+', '/', '*']
op_log = ['&&', '||', '>', '<', '>=', '<=', '==', '!=']
lista_erros = []
Identificador = []
linha = 0
final = ""
for i in arquivo:
    linha = linha + 1
    final = ""
    for k in i:

        if estado is 0:
            """Define o estado inicial"""
            if re.match(r"([A-Za-z_])", k):
                estado = 1  # Identificador
            if re.match(r"[0-9]", k):

                estado = 2  # Constante Numerica
            if k in operadores:
                print "entrouu"
                token = token + k + "|"
                estado = 0

        if estado is 1:
            """Valida Identificador"""
            if re.match(r"([A-za-z0-9])", k):
                token = token + k
            if k in separadores or re.match(r"(\s)", k):
                """Lista com separadores"""
                estado = 0
                print "Valor presente em k:" , k
                token = "|Iden, " + token + ", L:" + \
                    str(linha) + gera_marcador(k) + ", L:" + str(linha) + "|"

        if estado is 2:
            """Estado de indentificacao de constante numerica"""
            if re.match(r"[\w.]", k):

                numerico = numerico + k
            if k in sep_num or k in operadores:

                if(re.match(r"(^[0-9]*$|[0-9]+.[0-9]+)", numerico)):
                    valor = re.match(r"(^[0-9]*$|[0-9]+.[0-9]+)", numerico)
                    if valor is not None:
                        token = token + "Num, " + valor.group() + ",L:" + str(linha) + gera_marcador(k)
                        estado = 0
                        numerico = ""
                else:
                    print "erro"
                    lista_erros.append([numerico, linha])
                    numerico = ""
            else:
                if k in sep_num:
                    print "valor"
                    "Armazena token de separadores"
                    token = token + "Sep," + k + ",L:" + str(linha) + "|"


formata_tokens(token)
print lista_erros
# print "Erro", lista_erros
