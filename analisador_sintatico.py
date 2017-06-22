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
        self.elemento = ["NUM", " ID ", " Literal ",
                         "int", "float", "char", "while", "if"]
        self.tipo = ["int", "float", "char"]
        self.pos_global = -1
        self.indica_erro = 0

    def E(self, simb, lista, pos):
        """Pertence a expressao arimética"""
        # print simb
        if(simb in " NUM " or simb in " ID " or simb in "Literal" or simb == "("):
            return self.T(simb, lista, pos)
            return self.Elinha(simb, lista, pos)
            return self.logicos(simb, lista, pos)
        else:
            # print "Erro Caracter Posição ", pos, simb
            self.erro(simb, pos)
            self.indica_erro = 1
            return pos
        return pos

    def logicos(self, simb, lista, pos):
        print "entrou"
        if(simb is ">" or simb is "<"):
            return self.T(simb, lista, pos)
        else:
            return pos

    def T(self, simb, lista, pos):

        if(simb in " NUM " or simb in " ID " or simb in "Literal" or simb == "("):

            return self.F(simb, lista, pos)
            return self.Tlinha(simb, lista, pos)
        else:

            # Elinha(simb, lista, pos)
            # print "simboloT ", simb, pos
            # print "Erro Caracter Posicao", pos, simb
            self.erro(simb, pos)
            self.indica_erro = 1
            return pos
        return pos

    def F(self, simb, lista, pos):

        if(simb == "("):

            simb, pos = self.get_next_token(lista, pos)
            return self.E(simb, lista, pos)
            if(simb != ")"):
                # print "Erro Caracter Posicao F ", pos
                exit()
        elif(simb in " NUM " or simb in " ID " or simb in "Literal"):
            simb, pos = self.get_next_token(lista, pos)
            return self.Elinha(simb, lista, pos)

        else:

            # print "Erro Caracter Posicao", pos, simb
            self.erro(simb, pos)
            self.indica_erro = 1
            return pos
        return pos

    def get_next_token(self, lista, pos):
        """Puxa o proximo token"""
        """Retorna o elemento e a sua posicao"""
        maximo = len(self.tokens) - 1
        try:
            pos += 1
            return lista[pos], pos
        except Exception as e:
            return lista[maximo], maximo

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
            if(not(simb in " NUM " or simb in " ID " or simb in "Literal")):
                # print "Erro Caracter Posicao ", pos, simb
                print "fora"
                self.erro(simb, pos)
                self.indica_erro = 1

        return pos

    def valido(self, pos):
        print "Leitura Completa."
        # print pos
        return pos

    def consulta_tabela(self, posicao):
        """Retorna a Linha do erro"""
        # print "Pos", posicao
        if(posicao >= len(self.lista)):
            posicao -= 1
        for i in range(posicao, -1, -1):
            for palavras in self.elemento:
                if(self.lista[i][0] in palavras):
                    return self.tabela[self.lista[i][2]][2].split(" ")[0]

    def erro(self, simb, pos):
        """Indica que ocorreu um erro"""
        print "Erro Caracter ", simb
        validos = ["Literal", "ID", "NUM", "int", "float", "char"]
        self.indica_erro = 1
        try:
            print "Linha ", self.consulta_tabela(pos), "\n"
            return pos
        except Exception as e:
            print "Linha ", self.consulta_tabela(pos)

        return pos

    def programa(self):
        """Função programa"""
        #self.pos_global -= 1
        simb, pos = self.get_next_token(self.tokens, self.pos_global)
        print "First PROG ", simb
        if(simb is "$"):
            """Final da leitura"""
            return self.valido(pos)
        elif(simb in self.tipo):
            """Válida uma declaração"""
            pos = self.declaracao(pos)
            simb = self.tokens[pos]
            if(simb not in " $ "):
                self.pos_global = pos
                return self.programa()
            elif(simb in " $ "):
                return self.valido(pos)
            if(simb not in " ; "):
                # print simb
                return self.erro(simb, pos)

        elif ("ID" in simb):
            """Válida uma Atribuição"""
            ret_pos = self.atribuicao(pos)
            sim, pos = self.get_next_token(self.tokens, ret_pos)
            if(simb in "$"):
                return self.valido
            self.pos_global = pos
            return self.programa()
        elif ("while" in simb):
            """Válida a estrutura de repetição while"""
            ret_pos = self.repeticao(pos)
            self.pos_global = ret_pos
            self.programa()
        elif (simb in " if "):
            """Valida a estrutura condicional"""
            simb, pos = self.get_next_token(self.tokens, pos)
            pos = self.condicional(pos)

        else:
            # print simb
            return pos

    def condicional(self, pos):
        """Valida um  condicao"""
        simb = self.tokens[pos]
        pos = self.E(simb, self.tokens, pos)
        simb, pos = self.get_next_token(self.tokens, pos)
        if(simb in " { "):

            self.pos_global = pos
            pos = self.programa()
            simb = self.tokens[pos]
            if(simb in " } "):
                simb, pos = self.get_next_token(self.tokens, pos)
                if(simb in " ; "):
                    print "Condicional Correto"
                else:
                    self.erro(simb, pos)
                    return pos

        else:
            self.erro(simb, pos)
            return pos

    def atribuicao_virgula(self, pos):
        simb, pos = self.get_next_token(self.tokens, pos)
        if("ID" in simb):
            simb, pos = self.get_next_token(self.tokens, pos)
            if("," in simb):
                self.atribuicao_virgula(pos)
            elif(";" in simb):
                return pos
            else:
                self.erro(simb, pos)
                return pos
        else:
            self.erro(simb, pos)
            return pos

    def atribuicao(self, pos):
        """Válida uma atribuicao"""
        simb = self.tokens[pos]
        # print simb
        if("ID" in simb):
            simb, pos = self.get_next_token(self.tokens, pos)
            if("=" in simb):
                simb, pos = self.get_next_token(self.tokens, pos)
                print "Atribuição Válida"
                pos = self.E(simb, self.tokens, pos)
                simb, pos = self.get_next_token(self.tokens, pos)
                if(simb is not ";" and simb is not "$"):
                    self.pos_global = pos - 1
                    pos = self.programa()
                    return pos
                    # self.erro(simb, pos)
                    # self.indica_erro = 1
                # return pos
            elif("," in simb):
                return self.atribuicao_virgula(pos)
            else:

                return self.erro(simb, pos)
        else:
            print "Simbolo", simb

    def declaracao(self, pos):
        """Verifica a declaracao"""

        simb = self.tokens[pos]

        if(simb in self.tipo):
            """Verifica se simolo é int, float ou char."""
            simb, pos = self.get_next_token(self.tokens, pos)
            # print simb
            if(simb in " ID "):
                simb, pos = self.get_next_token(self.tokens, pos)
                if(simb is ";"):
                    print "Declaração Válida."
                    return pos
                else:
                    pos -= 1
                    # print pos
                    valor = self.atribuicao(pos)
                    if(valor is None):
                        print "erro"
                        self.indica_erro = 1
                        exit()
                    return valor

    def repeticao(self, pos):
        """Define a estrutura de repeticao"""
        simb = self.tokens[pos]
        # print "while"
        if(simb in "while"):
            simb, pos = self.get_next_token(self.tokens, pos)
            pos = self.E(simb, self.tokens, pos)
            simb, pos = self.get_next_token(self.tokens, pos)
            if(simb in "$"):
                print "Leitura Completa - Válido"
                return pos
            elif("{" in simb):
                print "aqui"
                simb, pos = self.get_next_token(self.tokens, pos)
                self.pos_global = pos
                ret_pos = self.bloco()
                simb = self.tokens[ret_pos - 2]
                if("}" in simb):

                    simb, pos = self.get_next_token(self.tokens, ret_pos - 2)
                    if(";" in simb):
                        print "While válido"
                        return pos
                else:
                    print "erro"
                    self.erro(simb, pos)

    def bloco(self):
        """Bloco de programa"""
        return self.programa()

    def conector(self, lista, tabela):
        """Realiza a ponte de conexão entre o Analisador Lexico e o Sintático"""
        # print "Entrada Sintático ", lista
        print lista
        self.lista = lista
        self.tabela = tabela
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

        self.programa()
        if(self.indica_erro is 0):
            print "Retorno sem erros"
        else:
            print "Leitura Completa - Verifique erros"
