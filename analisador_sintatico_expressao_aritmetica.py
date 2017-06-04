# coding: utf-8
"""
Analisador Sintático
Carlos Magno

"""
tokens = "(a+a)$"


def E(simb, lista, pos):
    # print simb
    if(simb == 'a' or simb == "("):
        T(simb, lista, pos)
        Elinha(simb, lista, pos)
    else:
        print "Erro Posicão",pos,"Caracter ",lista[pos]
        exit()


def T(simb, lista, pos):

    if(simb == "a" or simb == "("):

        F(simb, lista, pos)
        Elinha(simb, lista, pos)
    else:
        #Elinha(simb, lista, pos)
        # print "simboloT ", simb, pos
        print "Erro Posicão",pos,"Caracter ",lista[pos]
        exit()


def F(simb, lista, pos):

    if(simb == "("):

        retorno = get_next_token(lista, pos)
        simb = retorno[0]
        pos = retorno[1]
        E(simb, lista, pos)
        if(simb != ")"):
            print "Erro Posicão",pos,"Caracter ",lista[pos]
            exit()
    elif(simb == "a"):
        retorno = get_next_token(lista, pos)
        simb = retorno[0]
        pos = retorno[1]
        Elinha(simb, lista, pos)

    else:
        print "Erro Posicão",pos,"Caracter ",lista[pos]
        exit()


def get_next_token(lista, pos):

    pos += 1
    # print "Retorno ", lista[pos], pos
    return lista[pos], pos


def Elinha(simb, lista, pos):
    # print"Elinha ", simb, pos
    if(simb == "+"):
        retorno = get_next_token(lista, pos)
        simb = retorno[0]
        pos = retorno[1]
        # print "simbolo2 ", simb, pos
        T(simb, lista, pos)
        #Elinha(simb, lista, pos)
    elif (simb == ")" or simb == "$"):
        print "valido"
    else:
        # print simb
        #print "Erro Posicão",pos,"Caracter ",lista[pos]
        exit()


E(tokens[0], tokens, 0)
