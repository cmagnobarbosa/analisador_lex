# coding:utf-8
import sys
import re


arquivo = open("teste.c", "r")

token = ""
numerico = ""
estado = 0
separadores = [';', '\\', '\n','[', ']', ')', '(', ')', '{', '}', ',', '=']
operadores = ['-', '+', '/', '*']
op_log = ['&&', '||', '>', '<', '>=', '<=', '==', '!=']
lista_erros = []
linha = 0
for i in arquivo:
    linha = linha + 1
    for k in i:
        # print "Letra ",k
        if estado is 0:
            """Define o estado inicial"""
            if re.match(r"([A-Za-z_])", k):
                #token = token + k
                estado = 1  # Identificador
            if re.match(r"[0-9]", k):
                estado = 2  # Constante Numerica

        if estado is 1:
            """Valida Identificador"""
            if re.match(r"([\w])", k):
                token = token + k
            if k in separadores or re.match(r"(\s)",k):

                """Lista com separadores"""
                estado = 0
                token = "|"+token + ",L: "+str(linha) + "|Sep, " + k + ",L:" + str(linha)+"|"

        if estado is 2:
            """Estado de indentificacao de constante numerica"""
            if re.match(r"[0-9.]", k):
                numerico = numerico + k
                #print "Num",numerico
            if k in separadores:
                valor = re.match(r"([0-9]+$)|([0-9]+\s)",numerico)
                if valor is not None:
                    token = token + "[Num "+valor.group()+"]"
                    estado = 0
                    numerico = ""
                    #if k is not " ":
                        #token = "[Num, " + token + ",L:"+str(linha) +  "] [Sep, " + k + ",L:" + str(linha) + "]"


print token
#print "Erro", lista_erros
