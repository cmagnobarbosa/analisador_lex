# coding: utf-8
"""
Analisador Sintático
Semantico
Carlos Magno
"""
# NUM LITERAL ID


class Sintatico(object):
    """docstring for Sintatico."""

    def __init__(self):
        self.tokens = []
        self.lista = []
        self.tabela = []
        self.tabela_declaracao = {}
        self.elemento = ["NUM", " ID ", " Literal ",
                         "int", "float", "char", "while", "if"]
        self.tipo = ["int", "float", "char"]
        self.pos_global = -1
        self.indica_erro = 0
        self.cont = 0

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
        """Logico"""
        if(simb is ">" or simb is "<"):
            return self.T(simb, lista, pos)
        else:
            return pos

    def T(self, simb, lista, pos):

        if(simb in " NUM " or simb in " ID " or simb in "Literal" or simb == "("):

            return self.F(simb, lista, pos)
            return self.Tlinha(simb, lista, pos)
        else:

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
            retorno_geracao, tipo_retorno = self.gera_codigo("Add", pos, None)
            return self.T(simb, lista, pos), retorno_geracao, tipo_retorno
            # Elinha(simb, lista, pos)
        elif (simb == ")" or simb == ";"):
            print "Expressão Válida"
            return pos

        elif (simb == "-"):
            simb, pos = self.get_next_token(lista, pos)
            retorno_geracao, tipo_retorno = self.gera_codigo("Sub", pos, None)

            return self.T(simb, lista, pos), retorno_geracao, tipo_retorno
        else:
            return self.Tlinha(simb, lista, pos)

        return pos

    def Tlinha(self, simb, lista, pos):
        """Válida multiplicação"""
        # print"Elinha ", simb, pos
        if(simb == "*"):
            simb, pos = self.get_next_token(lista, pos)
            retorno_geracao, tipo_retorno = self.gera_codigo("Mult", pos, None)
            # print "simbolo2 ", simb, pos
            return self.F(simb, lista, pos), retorno_geracao, tipo_retorno
            return self.Tlinha(simb, lista, pos)
        elif(simb == "/"):
            simb, pos = self.get_next_token(lista, pos)
            retorno_geracao, tipo_retorno = self.gera_codigo("Div", pos, None)
            return self.F(simb, lista, pos), retorno_geracao, tipo_retorno
        elif (simb == ")" or simb == ";"):
            print "Expressão Válida"
        else:
            if(not(simb in " NUM " or simb in " ID " or simb in "Literal")):
                self.erro(simb, pos)
                self.indica_erro = 1

        return pos

    def valido(self, pos):
        print "Leitura Completa."
        return pos

    def consulta_tabela(self, posicao):
        """Retorna o elemento"""
        # print "Pos", posicao
        if(posicao >= len(self.lista)):
            posicao -= 1
        for i in range(posicao, -1, -1):
            for palavras in self.elemento:
                if(self.lista[i][0] in palavras):
                    return self.tabela[self.lista[i][2]][2].split(" ")[0], self.tabela[self.lista[i][2]][1]

    def erro(self, simb, pos):
        """Indica que ocorreu um erro"""
        print "Erro Caracter ", simb
        validos = ["Literal", "ID", "NUM", "int", "float", "char"]
        self.indica_erro = 1
        try:
            print "Linha ", self.consulta_tabela(pos)[0]
            return pos
        except Exception as e:
            print "Linha ", self.consulta_tabela(pos)[0]

        return pos

    def retorna_registrador(self, pos):
        """Retorna o registrador"""
        return self.tabela_declaracao[self.consulta_tabela(pos)[1]][2]

    def compara_tipo(self, a, b):
        """ Compara os tipos"""
        if(tipo_a != tipo_b):
            print "Erro - Tipos diferentes", tipo_a, tipo_b
            self.erro("Tipos Diferentes", a)

    def verifica_tipos(self, tipo_a, tipo_b):
        """Verica se os tipos são compativeis"""
        if(tipo_a in self.elemento):
            retorno = tipo_a
        else:
            retorno = tipo_b
        if(tipo_a not in self.elemento):
            tipo_a = self.tabela_declaracao[self.consulta_tabela(tipo_a)[1]][0]
        if(tipo_b not in self.elemento):
            tipo_b = self.tabela_declaracao[self.consulta_tabela(tipo_b)[1]][0]
        if(tipo_a != tipo_b):
            print "Erro - Tipos diferentes", tipo_a, tipo_b
            self.erro("Tipos Diferentes", retorno)
        else:

            return retorno

    def gera_codigo(self, opcao, pos, retorno_geracao):
        """Realiza a geração de código"""
        arquivo = open("geracao", "a")
        self.cont += 1
        registrador = "$S" + str(self.cont)
        if(opcao == "Load"):
            simb = self.consulta_tabela(pos)[1]
            exp = "Load " + registrador + "," + str(simb)
            arquivo.write(exp)
            arquivo.write('\n')
            lista = self.tabela_declaracao[simb]
            lista.append(registrador)
            self.tabela_declaracao[simb] = lista
            # print self.tabela_declaracao[simb]
        elif(opcao == "Add" or opcao == "Sub" or opcao == "Mult" or opcao == "Div"):
            # print self.tabela_declaracao
            simb = self.retorna_registrador(pos - 2)
            simb2 = self.retorna_registrador(pos)
            tipo_retorno = self.verifica_tipos(pos - 2, pos)
            retorno_geracao = opcao + " " + registrador + \
                "," + str(simb) + "," + str(simb2)
            arquivo.write(retorno_geracao)
            arquivo.write('\n')
            return retorno_geracao, tipo_retorno
        elif(opcao == "Store"):
            exp = "Store " + str(self.retorna_registrador(pos)) + \
                "," + str(retorno_geracao.split(" ")[1].split(",")[0])
            print exp
            arquivo.write(exp)
            arquivo.write('\n')
        arquivo.close()

    def programa(self):
        """Função programa"""
        # self.pos_global -= 1
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

    def declaracao_virgula(self, pos, tipo):
        """Válida declaração multipla"""
        simb, pos = self.get_next_token(self.tokens, pos)
        self.adiciona_tabela(pos, tipo)
        if("ID" in simb):
            self.gera_codigo("Load", pos, None)
            simb, pos = self.get_next_token(self.tokens, pos)

            if("," in simb):
                self.declaracao_virgula(pos)
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
        pos_geracao = pos
        if("ID" in simb):
            simb, pos = self.get_next_token(self.tokens, pos)

            if("=" in simb):
                simb, pos = self.get_next_token(self.tokens, pos)
                pos, retorno_geracao, tipo_retorno = self.E(
                    simb, self.tokens, pos)
                print "Atribuição Válida"
                self.gera_codigo("Store", pos_geracao, retorno_geracao)
                self.verifica_tipos(tipo_retorno, pos_geracao)
                simb, pos = self.get_next_token(self.tokens, pos)
                if(simb is not ";" and simb is not "$"):
                    self.pos_global = pos - 1
                    pos = self.programa()
                    return pos
                else:
                    return pos
            else:

                return self.erro(simb, pos)
        else:
            print "Símbolo", simb
            return pos

    def adiciona_tabela(self, pos, tipo):
        """Verifica se o elemento já esta na tabela"""
        # print self.lista[pos], self.lista
        simb = self.lista[pos][1]
        linha = self.consulta_tabela(pos)
        if(simb in self.tabela_declaracao):
            print "Erro Simbolo:", simb, ",Já declarado ", self.tabela_declaracao[simb][1]
            self.indica_erro = 1
        else:
            print "Adicionado na lista de símbolos"
            self.tabela_declaracao[simb] = [tipo, linha]

    def declaracao(self, pos):
        """Verifica a declaracao"""

        simb = self.tokens[pos]

        if(simb in self.tipo):
            """Verifica se simolo é int, float ou char."""
            tipo = simb
            simb, pos = self.get_next_token(self.tokens, pos)
            # print simb
            if(simb in " ID "):
                # print self.tokens[pos - 1], self.lista[pos][1],
                # self.consulta_tabela(pos)
                self.adiciona_tabela(pos, tipo)
                self.gera_codigo("Load", pos, None)
                simb, pos = self.get_next_token(self.tokens, pos)
                if(simb is ";"):
                    print "Declaração Válida."
                    return pos
                elif("," in simb):
                    return self.declaracao_virgula(pos, tipo)
                else:
                    pos -= 1
                    # print pos
                    valor = self.atribuicao(pos)
                    if(valor is None):
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
                print "Leitura Completa"
                return pos
            elif("{" in simb):
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
        # print lista
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
