# coding:utf-8
"""
Analisador Lexico
Licença: MIT
Carlos Magno Geraldo Barbosa
UFSJ
"""
import sys
import re

def add_linha_coluna(token,linha,coluna):
    """Adiciona linha e coluna"""
    p_inicio = coluna-len(token)
    return "L:"+str(linha)+ " C:("+str(p_inicio)+","+str(coluna)+")"

def conta_mais(linha,token_geral):
    n_mais= ""
    op=['+','-','*','^']
    lista = []
    flag =0
    #print linha
    for k in op:

        for i in linha:
            if i is k:
                n_mais=n_mais+ k
                if i is "^":
                    token_geral.append("[^]")
                    flag =1
                if i is "*":
                    token_geral.append("[*]")
                    flag =1
            if (len(n_mais) == 2):
                if k is "+":
                    lista.append(["++"])
                    token_geral.append(["++"])
                if k is "-":
                    lista.append("--")
                    token_geral.append(["--"])
                n_mais= ""
        if n_mais is not "" and not flag:
            lista.append(n_mais)
            token_geral.append("["+str(n_mais)+"]")
            n_mais=""
    #print lista
def add_operadores(linha):
    grupo_op = re.search(r"\+{2}|\-{2}|(\+\-)|(\-\+)|\*{2}|(\^\-)|(\^){2}",linha)
    if grupo_op is not None:
        return 1
    else:
        return 0

def verifica_reservada(token):
    reservada_list = ['int', 'float', 'char', 'if', 'else', 'printf',
                      'for', 'while', 'return', 'continue', 'break', 'read']
    cont = 0
    #print token
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
operadores = ['-', '+', '/', '*','^']
op_log = ['&&', '||', '>', '<', '>=', '<=', '==', '!=']
lista_erros = []
token_geral = []
tabela_token= {}
linha = 0
coluna = 0
flag = 0
id_tabela = 0
cont_flag =0
flag_linha =0
acumula = ""
for i in arquivo:
    linha = linha + 1
    coluna = 0
    flag_linha = 0
    for k in i:
        id_tabela = id_tabela + 1
        coluna = coluna + 1
        acumula = acumula+ k
        if estado is 0:
            """Define o estado inicial"""
            if re.match(r"([A-Za-z_])", k):
                """Pesquisa por identificadores validos"""
                estado = 1  # Identificador
            if re.match(r"[0-9]", k):
                """Pesquisa por Constante Numérica"""
                estado = 2  # Constante Numérica
            if re.match(r"[\"]", k):
                estado = 3
            if k in operadores:
                if flag_linha == 0:
                    conta_mais(i,token_geral)
                    flag_linha = 1
                if flag:
                    estado = 0
        if estado is 1:
            """Valida Identificador"""
            if re.match(r"([\w])", k):
                token = token + k
            if k in separadores or re.match(r"(\s)", k) or k in operadores:

                """Lista com separadores"""
                estado = 0
                reservado = re.match(
                    r"(int)|(float)|(char)|(if)|(else)|(printf)|(for)|(while)|(return)|(continue)|(break)|(read)", token)
                if reservado is not None:
                    tabela_token[id_tabela]= ["Reservado Cod: " + str(verifica_reservada(token)), reservado.group(),add_linha_coluna(token,linha,coluna)]
                    token_geral.append(
                        ["Reservado Cod: " + str(verifica_reservada(token)), reservado.group(),add_linha_coluna(token,linha,coluna)])
                    if k is not " " and not add_operadores(i):
                            token_geral.append(["Sep ", k,add_linha_coluna(token,linha,coluna)])
                    token = ""
                else:
                    tabela_token[id_tabela]= ["Iden ", token,add_linha_coluna(token,linha,coluna)]
                    token_geral.append(["Iden ", token,add_linha_coluna(token,linha,coluna)])
                    if k is not " " and not add_operadores(i):
                            token_geral.append(["Sep ", k,add_linha_coluna(token,linha,coluna)])
                    token = ""

        if estado is 2:
            """Estado de indentificacao de constante numerica"""
            if re.match(r"[\w.]", k):
                numerico = numerico + k
            if k in sep_num or k in operadores or re.match(r"\s", k):

                if(re.match(r"(^[0-9]*$|[0-9]+.[0-9]+)", numerico)):
                    valor = re.match(r"(^[0-9]*$|[0-9]+.[0-9]+)", numerico)
                    if valor is not None:
                        tabela_token[id_tabela]= ["Num", valor.group(),add_linha_coluna(valor.group(),linha,coluna)]
                        token_geral.append(
                            ["Num", valor.group(),add_linha_coluna(valor.group(),linha,coluna)])
                        if k is not " " and not add_operadores(i):
                            token_geral.append(["Sep", k,add_linha_coluna(k,linha,coluna)])
                        estado = 0
                        numerico = ""
                else:
                    lista_erros.append([numerico,add_linha_coluna(numerico,linha,coluna)])
                    numerico = ""
                    estado = 0
            else:
                if k in sep_num:
                    "Armazena token de separadores"
                    if k is not " " and not add_operadores(i):
                        token_geral.append(["Sep", k,add_linha_coluna(k,linha,coluna)])
                    estado = 0

        if estado is 3:
            if re.match(r"[a-zA-z0-9\"\s]", k):
                token = token + k
                if re.match(r"[\"]", k):
                    lit = re.match(r"[\"]+[\w\s]+[\"]*", token)
                    if lit is not None:
                        tabela_token[id_tabela]= ["Literal", lit.group(),add_linha_coluna(lit.group(),linha,coluna)]
                        token_geral.append(
                            ["Literal", lit.group(),add_linha_coluna(lit.group(),linha,coluna)])
                        token = ""
                        estado = 0

# print "Identificadores ", token_geral
exibe_tokens(token_geral)
print "Erros ", lista_erros
print "Tabela ", tabela_token
#print "tt",acumula
