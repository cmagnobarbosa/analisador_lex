# coding:utf-8
"""
Analisador Lexico
Licença: MIT
Carlos Magno Geraldo Barbosa
UFSJ
"""
import sys
import re


def converte_simbolos():
    """Substitui simbolos por números"""
    pass


def add_token(lista, token, linha):
    pass


def verifica_reservada(token):
    reservada_list = ['int', 'float', 'char', 'if', 'else', 'printf',
                      'for', 'while', 'return', 'continue', 'break', 'read']
    cont = 0
    for i in reservada_list:
        cont = cont + 1
        if (token in i):
            return cont


def exibe_tokens(lista):
    for i in lista:
        print i
try:
    nome = sys.argv[1]
    arquivo = open(nome, "r")
except Exception as e:
    arquivo = open("teste2.c", "r")


token = ""
numerico = ""
estado = 0
separadores = [';', '[', ']', ')', '(', ')', '{', '}', ',', '=', '.', '\n']
sep_num = [';', ',', '=']
operadores = ['-', '+', '/', '*']
op_log = ['&&', '||', '>', '<', '>=', '<=', '==', '!=']
lista_erros = []
token_geral = []
linha = 0
final = ""
for i in arquivo:
    linha = linha + 1
    final = ""
    for k in i:

        if estado is 0:
            """Define o estado inicial"""
            if re.match(r"([A-Za-z_])", k):
                """Pesquisa por identificadores validos"""
                estado = 1  # Identificador
            if re.match(r"[0-9]", k):
                """Pesquisa por Constante Numérica"""
                estado = 2  # Constante Numérica
            if re.match(r"[\+]{2}|[\+]", k):
                estado = 4
            if re.match(r"[\"]", k):
                estado = 3
        if estado is 1:
            """Valida Identificador"""
            if re.match(r"([A-za-z0-9])", k):
                token = token + k

            else:
                if k in operadores:
                    lit = re.match(r"[\+]{2}|[\+]", k)
                    if lit is not None:
                        token = token + lit.group()
                    estado = 0
            if k in separadores or re.match(r"(\s\+\-\*)", k):

                """Lista com separadores"""
                estado = 0
                reservado = re.match(
                    r"(int)|(float)|(char)|(if)|(else)|(printf)|(for)|(while)|(return)|(continue)|(break)|(read)", token)
                if reservado is not None:
                    token_geral.append(
                        ["Reservado Cod: " + str(verifica_reservada(token)), reservado.group(), " l: " + str(linha)])
                    if k is not " ":
                        token_geral.append(["Sep ", k, "l:" + str(linha)])
                    token = ""
                else:

                    token_geral.append(["Iden ", token, "l: " + str(linha)])
                    if k is not " ":
                        token_geral.append(["Sep ", k, "l:" + str(linha)])
                    token = ""
            else:
                if k is operadores:
                    estado = 0

        if estado is 2:
            """Estado de indentificacao de constante numerica"""
            if re.match(r"[\w.]", k):
                numerico = numerico + k
            if k in sep_num or k in operadores:

                if(re.match(r"(^[0-9]*$|[0-9]+.[0-9]+)", numerico)):
                    valor = re.match(r"(^[0-9]*$|[0-9]+.[0-9]+)", numerico)
                    if valor is not None:

                        token_geral.append(
                            ["Num", valor.group(), "l:" + str(linha)])
                        if k is not " ":
                            token_geral.append(["Sep", k, "l:" + str(linha)])
                        else:
                            if k in operadores:
                                print token
                                token = token + k
                        estado = 0
                        numerico = ""
                else:
                    lista_erros.append([numerico, "l:" + str(linha)])
                    numerico = ""
                    estado = 0
            else:
                if k in sep_num:
                    "Armazena token de separadores"
                    if k is not " ":
                        token_geral.append(["Sep", k, "l:" + str(linha)])
                    estado = 0

        if estado is 3:
            if re.match(r"[a-zA-z0-9\"\s]", k):
                token = token + k
                if re.match(r"[\"]", k):
                    lit = re.match(r"[\"]+[\w\s]+[\"]*", token)
                    if lit is not None:
                        token_geral.append(
                            ["Literal", lit.group(), "l: " + str(linha)])
                        token = ""
                        estado = 0

        if estado is 4:
            if re.match(r"[\+]{2}|[\+]", k):
                token = token + k
            else:
                lit = re.search(r"[\+]{2}|[\+]", token)
                word= re.search(r"[\w]",token)
                if word is not None:
                    token_geral.append(["Iden ",word.group(), "l: " + str(linha)])
                if lit is not None:
                    token_geral.append([lit.group(), "l: " + str(linha)])
                token = " "
                estado = 0

# print "Identificadores ", token_geral
exibe_tokens(token_geral)
print "Erros ", lista_erros
