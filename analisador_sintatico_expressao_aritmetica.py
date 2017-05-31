"""
Analisador Sintático
Carlos Magno

"""
tokens = ['$',"(","b","+", "a","+","b",")"]


def E(simb,lista):
    print simb
    if(simb == 'a' or simb == "("):

        T(simb,lista)

        Elinha(simb,lista)
    else:

        print "Erro E"


def T(simb, lista):

    if(simb == "a" or simb == "("):

        F(simb, lista)
        Elinha(simb, lista)
    else:

        print "Erro T"


def F(simb,lista):
    if(simb == "("):
        E(simb,lista)
        simb = get_next_token(lista)
        if(simb != ")"):
            print "Erro F"
    elif(simb == "a"):
        simb = get_next_token(lista)

    else:
        print "Erro F"
def get_next_token(lista):
    return lista.pop()

def Elinha(simb,lista):
    if(simb == "+"):
        simb = get_next_token(lista)
        print "simbolo ",simb
        T(sim,lista)
        Elinha(simb,lista)
    elif (simb == ")" or simb == "$"):
        print "valido"
    else:
        print "Simbolo ",simb, "Lista ",lista
        print "erro Elinha"

tokens.reverse()
Elinha(tokens.pop(),tokens)
