# coding: utf-8
"""
Analisador Sintático
Carlos Magno
"""
# tokens = ["(", "a", "+", "a", ")", "$"]

# NUM LITERAL ID


class Sintatico(object):
    """docstring for Sintatico."""

    def __init__(self):
        self.tokens = []
        self.elemento = ["NUM", "ID", "Literal"]

    def E(self, simb, lista, pos):
        # print simb
        if(simb in self.elemento or simb == "("):
            self.T(simb, lista, pos)
            self.Elinha(simb, lista, pos)
        else:
            print "Erro Caracter Posicao ", pos, simb
            return 0

    def T(self, simb, lista, pos):

        if(simb in self.elemento or simb == "("):

            self.F(simb, lista, pos)
            self.Tlinha(simb, lista, pos)
        else:
            #Elinha(simb, lista, pos)
            # print "simboloT ", simb, pos
            print "Erro Caracter Posicao ", pos, simb
            return 0

    def F(self, simb, lista, pos):

        if(simb == "("):

            retorno = self.get_next_token(lista, pos)
            simb = retorno[0]
            pos = retorno[1]
            self.E(simb, lista, pos)
            if(simb != ")"):
                print "Erro Caracter Posicao ", pos
                exit()
        elif(simb in self.elemento):
            retorno = self.get_next_token(lista, pos)
            simb = retorno[0]
            pos = retorno[1]
            self.Elinha(simb, lista, pos)

        else:
            print "Erro Caracter Posicao ", pos, simb
            exit()

    def get_next_token(self, lista, pos):
        """Puxa o proximo token"""
        pos += 1
        # print lista[pos]
        return lista[pos], pos

    def Elinha(self, simb, lista, pos):
        """Válida adição e subtração."""
        if(simb == "+"):
            retorno = self.get_next_token(lista, pos)
            simb = retorno[0]
            pos = retorno[1]
            self.T(simb, lista, pos)
            #Elinha(simb, lista, pos)
        elif (simb == ")" or simb == "$"):
            print "Válido"
        elif (simb == "-"):
            retorno = self.get_next_token(lista, pos)
            simb = retorno[0]
            pos = retorno[1]
            # print "simbolo2 ", simb, pos
            self.T(simb, lista, pos)
        else:
            self.Tlinha(simb, lista, pos)
            # return 0
            # print "Invalido"

    def Tlinha(self, simb, lista, pos):
        """Válida multiplicação"""
        # print"Elinha ", simb, pos
        if(simb == "*"):
            retorno = self.get_next_token(lista, pos)
            simb = retorno[0]
            pos = retorno[1]
            # print "simbolo2 ", simb, pos
            self.F(simb, lista, pos)
            self.Tlinha(simb, lista, pos)
        elif(simb == "/"):
            retorno = self.get_next_token(lista, pos)
            simb = retorno[0]
            pos = retorno[1]
            self.F(simb, lista, pos)
        elif (simb == ")" or simb == "$"):
            print "Válido"
        else:
            return 0

    def conector(self, lista):
        """Realiza a ponte de conexão entre o Analisador Lexico e o Sintatico"""
        print "Entrada Sintatico ", lista
        for i in lista:
            # print i
            if(i[0] is "NUM" or i[0] is "Literal" or i[0] is "ID"):
                self.tokens.append(i[0])
            else:
                self.tokens.append(i[0])
        print self.tokens
        self.E(self.tokens[0], self.tokens, 0)

# if __name__ == '__main__':
#     sin = Sintatico()
#
#     sin.E(tokens[0], tokens, 0)
