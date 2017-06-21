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
        self.lista = []
        self.tabela = []
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

            simb, pos = self.get_next_token(lista, pos)
            return self.E(simb, lista, pos)
            if(simb != ")"):
                # print "Erro Caracter Posicao F ", pos
                exit()
        elif(simb in self.elemento):
            simb, pos = self.get_next_token(lista, pos)
            return self.Elinha(simb, lista, pos)

        else:
            print "Erro Caracter Posicao ", pos, simb
            return pos
        return pos

    def get_next_token(self, lista, pos):
        """Puxa o proximo token"""
        """Retorna o elemento e a sua posicao"""
        # print "Valor ", pos, type(pos)

        # print lista[pos]
        pos += 1
        try:
            return lista[pos], pos
        except Exception as e:
            if(lista[pos - 1] in " $ "):
                print "Leitura completa - Verifique os erros encontrados."
                exit()
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
            simb, pos = self.get_next_token(lista, pos)
            return self.T(simb, lista, pos)
            # Elinha(simb, lista, pos)
        elif (simb == ")" or simb == ";"):
            print "Expressão Válida"
            return pos

        elif (simb == "-"):
            simb, pos = self.get_next_token(lista, pos)
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
            simb, pos = self.get_next_token(lista, pos)
            # print "simbolo2 ", simb, pos
            return self.F(simb, lista, pos)
            return self.Tlinha(simb, lista, pos)
        elif(simb == "/"):
            simb, pos = self.get_next_token(lista, pos)
            return self.F(simb, lista, pos)
        elif (simb == ")" or simb == ";"):
            print "Expressão Válida"
        else:
            if(simb not in self.elemento):
                print "Erro Caracter Posicao ", pos, simb

        return pos

    def valido(self):
        print "Leitura Completa."
        return 0

    def erro(self, simb, pos):
        """Indica que ocorreu um erro"""
        print "Erro Caracter ", simb, " Posição ", pos
        try:
            print "Linha Coluna", self.tabela[self.lista[pos - 1][2]][2]
            return pos
        except Exception as e:
            print "erro"

        return pos

    def programa(self):
        """Função programa"""
        # print "Pos Global ", self.pos_global
        simb, pos = self.get_next_token(self.tokens, self.pos_global)
        print "First PROG ", simb
        if(simb is "$"):
            """Final da leitura"""
            return self.valido()
        elif(simb in self.tipo):
            """Válida uma declaração"""
            ret_pos = self.declaracao(pos)
            simb = self.tokens[ret_pos]
            simb, pos = self.get_next_token(self.tokens, ret_pos)
            if(simb not in " $ "):
                print "programa", pos
                self.pos_global = pos
                return self.programa()
            elif(simb in " $ "):
                return self.valido()
            if(simb not in " ; "):
                print simb
                return self.erro(simb, pos)

        elif ("ID" in simb):
            """Válida uma Atribuição"""
            ret_pos = self.atribuicao(pos)
            sim, pos = self.get_next_token(self.tokens, ret_pos)
            if(simb in "$"):
                return self.valido
            # elif(simb is not ";"):
            #     print "Erro Faltando ; Posição", simb, pos
            #     print self.tokens[ret_pos]
            self.pos_global = pos
            return self.programa()
        elif ("while" in simb):
            """Válida a estrutura de repetição while"""
            ret_pos = self.repeticao(pos)
            self.pos_global = ret_pos
            self.programa()
        elif ("if" in simb):
            """Valida a estrutura condicional"""

            pass
        else:
            print self.tokens[pos + 1]
            print simb
            # print "Simbolo ", simb, pos
            return pos

    def atribuicao(self, pos):
        """Válida uma atribuicao"""
        simb = self.tokens[pos]
        print "Simbolo ", simb
        if("ID" in simb):
            retorno = self.get_next_token(self.tokens, pos)
            simb = retorno[0]
            pos = retorno[1]
            if("=" in simb):
                retorno = self.get_next_token(self.tokens, pos)
                simb = retorno[0]
                pos = retorno[1]
                print "Atribuição Válida"
                return self.E(simb, self.tokens, pos)
            else:
                return self.erro(simb, pos)

    def declaracao(self, pos):
        """Verifica a declaracao"""
        # print "Declaracao ", self.tokens[pos]

        simb = self.tokens[pos]
        if(simb in self.tipo):
            """Verifica se simolo é int, float ou char."""
            retorno = self.get_next_token(self.tokens, pos)
            simb = retorno[0]
            pos = retorno[1]
            if(simb in " ID "):
                retorno = self.get_next_token(self.tokens, pos)
                simb = retorno[0]
                pos = retorno[1]
                if(simb is ";"):
                    print "Declaração Válida."
                    return pos
                else:
                    return self.atribuicao(pos - 1)
                    # self.pos_global = pos - 2
                    # # print self.tokens[pos - 2]
                    # return pos - 2
            else:
                pass
                # return self.erro()

    def repeticao(self, pos):
        """Define a estrutura de repeticao"""
        simb = self.tokens[pos]
        if(simb in "while"):
            simb, pos = self.get_next_token(self.tokens, pos)
            ret_pos = self.E(simb, self.tokens, pos)
            simb, pos = self.get_next_token(self.tokens, ret_pos)
            if(simb in "$"):
                print "Leitura Completa - Válido"
                return pos
            elif("{" in simb):
                simb, pos = self.get_next_token(self.tokens, pos)
                self.pos_global = pos - 1
                ret_pos = self.bloco()
                simb = self.tokens[ret_pos]
                if("}" in simb):
                    simb, pos = self.get_next_token(self.tokens, ret_pos)
                    if(";" in simb):
                        print "While válido"
                        return pos
                else:
                    self.erro(simb, pos)

    def bloco(self):
        return self.programa()

    def conector(self, lista, tabela):
        """Realiza a ponte de conexão entre o Analisador Lexico e o Sintático"""
        # print "Entrada Sintático ", lista
        # print lista
        self.lista = lista
        self.tabela = tabela
        print "Tabela ", tabela
        cont = 0
        for i in lista:
            cont = cont + 1
            if(i[0] is "NUM" or i[0] is "Literal" or i[0] in " ID "):
                self.tokens.append(i[0])
            elif("Res" in i[0]):
                self.tokens.append(i[1])
            else:
                self.tokens.append(i[0])
        self.tokens.append("$")
        print "Entrada Sintático ", self.tokens

        retorno_final = self.programa()
        if(retorno_final is 0 or retorno_final is None):
            print "Retorno sem erros"
        else:
            print retorno_final
            print "Leitura Completa - Verifique erros"
        # self.E(self.tokens[0], self.tokens, 0)
