# coding:utf-8
"""
Analisador Lexico
Licença: MIT
Carlos Magno Geraldo Barbosa
UFSJ
"""
import sys
import re


token = ""
numerico = ""
estado = 0
#separadores = [';', '[', ']', ')', '(', ')', '{', '}', ',', '=', '.']
#operadores = ['-', '+', '/', '*', '^']
lista_erros = []
token_geral = []
tabela_token = {}
linha = 0
coluna = 0
id_tabela = 0
acumula = ""

def aux_agrupa(elemento,i,lista,cont,elemento_double,next_elemento):
    """Auxilia a função que agrupa"""
    if elemento in i:
        if next_elemento in lista[cont+1]:
            lista.pop(cont+1)
            lista.insert(cont,[elemento_double])
            lista.pop(cont+1)

def agrupa(lista):
    """Agrupa os elementos na lista"""
    cont =0
    #print lista
    for i in lista:
        aux_agrupa("+",i,lista,cont,"++","+")
        aux_agrupa("-",i,lista,cont,"--","-")
        aux_agrupa("=",i,lista,cont,"==","=")
        aux_agrupa("&",i,lista,cont,"&&","&")
        aux_agrupa("|",i,lista,cont,"||","|")
        aux_agrupa("<",i,lista,cont,"<=","=")
        aux_agrupa(">",i,lista,cont,">=","=")
        aux_agrupa("!",i,lista,cont,"!=","=")
        cont= cont+1


def add_linha_coluna(token, linha, coluna):
    """Adiciona linha e coluna"""
    p_inicio = coluna - len(token)
    return "L:" + str(linha) + " C:(" + str(p_inicio) + "," + str(coluna) + ")"

def ver_iden(elemento):
    """Verifica se o elemento é um separador dos numeros"""
    if(re.match(r"[\w]", elemento)):
        return 0
    else:
        return 1

def ver_num(elemento):
    """Verifica se o elemento pertence ao grupo das constantes numericas"""
    if(re.match(r"[\d.]", elemento)):
        return 0
    else:
        """Se ele não pertence retorna 1"""
        return 1

def verifica_reservada(token):
    """Verifica se determinado token é reservado e retorna um código para o mesmo"""
    reservada_list = ['int', 'float', 'char', 'if', 'else', 'printf',
                      'for', 'while', 'return', 'continue', 'break', 'read']
    cont = 0
    for i in reservada_list:
        cont = cont + 1
        if (token == i):
            return cont

def exibe_imprime(nome,lista):
    """escreve no arquivo de saida"""
    arq = open(nome, "w")
    if(len(lista)==0):
        arq.write("Lista vazia\n")
    for i in lista:
        print i

        arq.write(str(i) + "\n")

    arq.close()

def imprime_tabela(tabela_token):
    "Imprime a tabela de tokens"
    arq_tabela = open("tabela_simbolos_simp", "w")
    arq_tabela.write("Tabela de Simbolos\n")
    for i in sorted(tabela_token):
        arq_tabela.write("Chave:" + str(i) + " " + str(tabela_token[i]) + "\n")
    arq_tabela.close()

def open_file():
    """Abre o arquivo de entrada"""
    try:
        nome = sys.argv[1]
        arquivo = open(nome, "r")
    except Exception as e:
        arquivo = open("teste2.c", "r")
    return arquivo

arquivo= open_file()
for i in arquivo:
    linha = linha + 1
    coluna = 0
    for k in i:
        id_tabela = (id_tabela + 1)
        coluna = coluna + 1
        if estado is 0:
            """Define o estado inicial"""
            if k is "/" and i[coluna] is "*" and estado == 0 and estado != 4:
                """Comentario"""
                estado = 4
                token_geral.append(["*/"])
            if re.search(r"^(#)|[/]{2}", i) and estado == 0 and estado != 4:
                """ignora o stdio e linha comentada"""
                break
            if re.match(r"([A-Za-z_])", k) and estado == 0 and estado != 4:
                """Pesquisa por identificadores validos"""
                estado = 1  # Identificador
            if re.match(r"[0-9]", k) and estado == 0 and estado != 4:
                """Pesquisa por Constante Numérica"""
                estado = 2  # Constante Numérica
            if re.match(r"[\"]", k) and estado == 0 and estado != 4:
                estado = 3

            if ver_num(k) and ver_iden(k) and estado==0 and estado!=4:
                """Se não for um identificador valido então é um separador"""
                if not re.match(r"\s",k):
                    token_geral.append([k])

        if estado is 1:
            """Valida Identificador"""
            if re.match(r"([\w])", k):
                token = token + k
            if ver_iden(k):
                """Lista com separadores"""
                estado = 0
                if verifica_reservada(token):

                    tabela_token[id_tabela] = ["Res Cod: " + str(
                        verifica_reservada(token)), token, add_linha_coluna(token, linha, coluna)]

                    token_geral.append(
                        ["Res Cod: " + str(verifica_reservada(token)), token, id_tabela])

                    if k is not " ":
                        token_geral.append([k])
                    token = ""
                else:

                    tabela_token[id_tabela] = ["ID ", token,
                                               add_linha_coluna(token, linha, coluna)]
                    token_geral.append(
                        ["ID ", token, id_tabela])

                    if ver_iden(k):
                        """Vai inserir o k como separador """
                        token_geral.append([k])
                        estado=0
                    token = ""

        if estado is 2:
            """Estado de indentificacao de constante numerica"""
            if re.match(r"[\w.]", k):
                numerico = numerico + k
            if ver_num(k):
                if(re.match(r"(^[0-9]*$|[0-9]+.[0-9]+)", numerico)):
                    valor = re.match(r"(^[0-9]*$|[0-9]+.[0-9]+)", numerico)
                    if valor is not None:
                        tabela_token[id_tabela] = [
                            "NUM", valor.group(), add_linha_coluna(valor.group(), linha, coluna)]

                        token_geral.append(
                            ["NUM", valor.group(), id_tabela])
                        if k is not " ":
                            token_geral.append([k])
                        estado = 0
                        numerico = ""
                else:
                    token_geral.append("[Token Inválido]")
                    lista_erros.append(
                        [numerico, add_linha_coluna(numerico, linha, coluna)])
                    numerico = ""
                    estado = 0
            else:
                if ver_num(k):
                    "Armazena token de separadores"
                    if k is not " ":
                        token_geral.append([k])
                    estado = 0

        if estado is 3:
            """Identifica Literal"""
            if re.match(r"[%a-zA-z0-9\"\s]", k):
                token = token + k
                if re.match(r"[\"]", k):
                    lit = re.match(r"[\"]+[%\w\s]+[\"]*", token)
                    if lit is not None:
                        tabela_token[id_tabela] = ["Literal", lit.group(
                        ), add_linha_coluna(lit.group(), linha, coluna)]

                        token_geral.append(
                            ["Literal", lit.group(), id_tabela])
                        token = ""
                        estado = 0

        if estado is 4:
            """Incrementa comentarios"""
            acumula = acumula + k
            if re.search(r"(\*\/)", acumula):
                token_geral.append("[*/]")
                estado = 0

agrupa(token_geral)
exibe_imprime("token_saida",token_geral)
exibe_imprime("lista_erros",lista_erros)
lista_erros=[]
print "Tabela", tabela_token
imprime_tabela(tabela_token)
print "Comentário:", acumula
