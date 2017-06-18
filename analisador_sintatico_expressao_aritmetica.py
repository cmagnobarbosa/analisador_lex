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
        self.tipo = ["int", "float", "char"]
        self.pos_global = -1

    def E(self, simb, lista, pos):
        """Pertence a expressao arimética"""
        # print simb
        if(simb in self.elemento or simb == "("):
            return self.T(simb, lista, pos)
            return self.Elinha(simb, lista, pos)
        else:
            print "Erro Caracter Posição ", pos, simb
            self.valida_expressao(simb, lista, pos)
            return pos
        return pos

    def T(self, simb, lista, pos):

        if(simb in self.elemento or simb == "("):

            return self.F(simb, lista, pos)
            return self.Tlinha(simb, lista, pos)
        else:
            # Elinha(simb, lista, pos)
            # print "simboloT ", simb, pos
            print "Erro Caracter Posicao  ", pos, simb
            return "T"
        return pos

    def F(self, simb, lista, pos):

        if(simb == "("):

            retorno = self.get_next_token(lista, pos)
            simb = retorno[0]
            pos = retorno[1]
            return self.E(simb, lista, pos)
            if(simb != ")"):
                # print "Erro Caracter Posicao F ", pos
                exit()
        elif(simb in self.elemento):
            retorno = self.get_next_token(lista, pos)
            simb = retorno[0]
            pos = retorno[1]
            return self.Elinha(simb, lista, pos)

        else:
            print "Erro Caracter Posicao ", pos, simb
            exit()
        return pos

    def get_next_token(self, lista, pos):
        """Puxa o proximo token"""
        """Retorna o elemento e a sua posicao"""
        pos += 1
        # print lista[pos]
        try:
            return lista[pos], pos
        except Exception as e:
            print "Erro Caracter", lista[pos - 1], "Posicao ", pos
            print "Estouro da pilha de Recursão ..."\
                "Último simbolo válido", lista[pos - 1]
            exit()

    def valida_expressao(self, simb, lista, pos):
        """Válida expressões que não são ariméticas."""
        if(simb not in self.elemento):
            print "Erro Caracter Posicao ", pos, simb
            return simb, pos

    def Elinha(self, simb, lista, pos):
        """Válida adição e subtração."""
        if(simb == "+"):
            retorno = self.get_next_token(lista, pos)
            simb = retorno[0]
            pos = retorno[1]
            return self.T(simb, lista, pos)
            # Elinha(simb, lista, pos)
        elif (simb == ")" or simb == ";"):
            print "Expressão Válida"
            return pos

        elif (simb == "-"):
            retorno = self.get_next_token(lista, pos)
            simb = retorno[0]
            pos = retorno[1]
            # print "simbolo2 ", simb, pos
            return self.T(simb, lista, pos)
        else:
            return self.Tlinha(simb, lista, pos)
            # return 0
            # print "Invalido"
        return pos

    def Tlinha(self, simb, lista, pos):
        """Válida multiplicação"""
        # print"Elinha ", simb, pos
        if(simb == "*"):
            retorno = self.get_next_token(lista, pos)
            simb = retorno[0]
            pos = retorno[1]
            # print "simbolo2 ", simb, pos
            return self.F(simb, lista, pos)
            return self.Tlinha(simb, lista, pos)
        elif(simb == "/"):
            retorno = self.get_next_token(lista, pos)
            simb = retorno[0]
            pos = retorno[1]
            return self.F(simb, lista, pos)
        elif (simb == ")" or simb == ";"):
            print "Expressão Válida"
        else:
            if(simb not in self.elemento):
                print "Erro Caracter Posicao ", pos, simb

        return pos

    def programa(self):
        """Função programa"""
        retorno = self.get_next_token(self.tokens, self.pos_global)
        simb = retorno[0]
        pos = retorno[1]
        print "First PROG ", simb
        if(simb is "$"):
            """Final da leitura"""
            print "Leitura Completa - Válido"
        if(simb in self.tipo):
            self.declaracao(pos)
        elif ("ID" in simb):
            """Válida uma Atribuição"""
            ret_pos = self.atribuicao(pos)
            retorno = self.get_next_token(self.tokens, ret_pos)
            simb = retorno[0]
            pos = retorno[1]
            if(simb is not ";"):
                print "Erro Faltando ; Posição", simb, pos
            elif(simb is "$"):
                print "leitura completa - valido"
            self.pos_global = pos
            self.programa()
        elif ("while" in simb):
            pass
        elif ("if" in simb):
            pass

    def atribuicao(self, pos):
        """Válida uma atribuicao"""
        simb = self.tokens[pos]
        if("ID" in simb):
            retorno = self.get_next_token(self.tokens, pos)
            simb = retorno[0]
            pos = retorno[1]
            if("=" in simb):
                retorno = self.get_next_token(self.tokens, pos)
                simb = retorno[0]
                pos = retorno[1]
                return self.E(simb, self.tokens, pos)

    def declaracao(self, pos):
        print "Declaracao "
        pass

    def conector(self, lista):
        """Realiza a ponte de conexão entre o Analisador Lexico e o Sintático"""
        print "Entrada Sintático ", lista
        cont = 0
        for i in lista:
            cont = cont + 1
            if(i[0] is "NUM" or i[0] is "Literal" or i[0] in " ID "):
                self.tokens.append(i[0])
            elif("Res" in i[0]):
                self.tokens.append(i[1])
                print self.tokens
            else:
                self.tokens.append(i[0])
        self.tokens.append("$")
        print self.tokens
        self.programa()
        # self.E(self.tokens[0], self.tokens, 0)
