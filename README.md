# analisador_lex
Analisador Lexico - Compiladores UFSJ
- Carlos Magno

# Sobre o Analisador
Este analisador apresenta uma implementação simples de analisador lexico. O mesmo está escrito em python 2.7. Este trabalho faz parte da implementação da etapas de análise de um compilador.

# Arquivo principal
O arquivo principal do projeto é o anlex.py.

# Como Executar

Para executar o analisador em um ambiente Linux ou Windows é necessario possuir o python 2.7 instalado. Com o python instalado abra o terminal e siga os passos abaixo.

Neste caso o arquivo de teste a ser carregado é o teste2.c
> python anlex.py 

Para executar o teste com um arquivo em C personalizado digite:
>python anlex.py nome_do_arquivo.c

# Arquivos de Saida
Ao executar o analisador serão gerados três arquivos:
- Lista de erros. (lista_erros)
- Tabela de simbolos.(tabela_simbolos_simp)
- Arquivo com os tokens gerados. (tokens_saida)
# Formato de saída
Os seguintes formatos são gerados.
Modelo Geral
>[separador]

>[identificador,nome/valor,entrada_tabela_de_simbolos]

Entrada
>float d=7.77;

Constante Númerica
>['NUM', '7.77', 13]

Identificador
>['ID ', 'd', 8]

Tipo Reservado
>['Res Cod: 2', 'float', 6]

>[2,float,6]
