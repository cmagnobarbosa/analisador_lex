# coding: utf-8
"""
Analisador Sintático
Carlos Magno

"""
tokens = "(a-a+a//a)"


def E(simb, lista, pos):
    # print simb
    if(simb == 'a' or simb == "("):
        T(simb, lista, pos)
        Elinha(simb, lista, pos)
    else:
        print "Erro Caracter Posicao ", pos, simb
        exit()


def T(simb, lista, pos):

    if(simb == "a" or simb == "("):

        F(simb, lista, pos)
        Tlinha(simb, lista, pos)
    else:
        #Elinha(simb, lista, pos)
        # print "simboloT ", simb, pos
        print "Erro Caracter Posicao ", pos, simb
        return 0


def F(simb, lista, pos):

    if(simb == "("):

        retorno = get_next_token(lista, pos)
        simb = retorno[0]
        pos = retorno[1]
        E(simb, lista, pos)
        if(simb != ")"):
            print "Erro Caracter Posicao ", pos
            exit()
    elif(simb == "a"):
        retorno = get_next_token(lista, pos)
        simb = retorno[0]
        pos = retorno[1]
        Elinha(simb, lista, pos)

    else:
        print "Erro Caracter Posicao ", pos, simb
        exit()


def get_next_token(lista, pos):
    """Puxa o proximo token"""
    pos += 1
    return lista[pos], pos


def Elinha(simb, lista, pos):
    """Válida adição e subtração."""
    if(simb == "+"):
        retorno = get_next_token(lista, pos)
        simb = retorno[0]
        pos = retorno[1]
        # print "simbolo2 ", simb, pos
        T(simb, lista, pos)
        #Elinha(simb, lista, pos)
    elif (simb == ")" or simb == "$"):
        print "Válido"
    elif (simb == "-"):
        retorno = get_next_token(lista, pos)
        simb = retorno[0]
        pos = retorno[1]
        # print "simbolo2 ", simb, pos
        T(simb, lista, pos)
    else:
        Tlinha(simb, lista, pos)
        # return 0
        # print "Invalido"
        exit()


def Tlinha(simb, lista, pos):
    """Válida multiplicação"""
    # print"Elinha ", simb, pos
    if(simb == "*"):
        retorno = get_next_token(lista, pos)
        simb = retorno[0]
        pos = retorno[1]
        # print "simbolo2 ", simb, pos
        F(simb, lista, pos)
        Tlinha(simb, lista, pos)
    elif(simb == "/"):
        retorno = get_next_token(lista, pos)
        simb = retorno[0]
        pos = retorno[1]
        F(simb, lista, pos)
    elif (simb == ")" or simb == "$"):
        print "Válido"
    else:
        return 0
        exit()

E(tokens[0], tokens, 0)
