import Funcoes
import os
import msvcrt
import sys
import Dados
import time

Campo = {
    "NomeCampo": "CodProd",
    "TituloCampo": "Código do Produto",
    "Tamanho": 7,
    "Editavel": True,
    "Conteudo": "",
    "Topo": 4,
    "Esquerda": 7,}
LstCampos = [Campo]

Campo1 = {
    "NomeCampo": "NomeProd",
    "TituloCampo": "Descrição do Produto",
    "Tamanho": 40,
    "Editavel": True,
    "Conteudo": "",
    "Topo": 6,
    "Esquerda": 7,}
LstCampos.append(Campo1)

Campo2 = {
    "NomeCampo": "TipoProd",
    "TituloCampo": "Tipo (1-Série, 2-Filme, 3-Documentário)",
    "Tamanho": 3,
    "Editavel": True,
    "Conteudo": "",
    "Topo": 8,
    "Esquerda": 7,}
LstCampos.append(Campo2)

Campo3 = {
    "NomeCampo": "PrecoProd",
    "TituloCampo": "Preço",
    "Tamanho": 12,
    "Editavel": True,
    "Conteudo": "",
    "Topo": 10,
    "Esquerda": 7,}
LstCampos.append(Campo3)

Campo4 = {
    "NomeCampo": "DisponivelProd",
    "TituloCampo": "Disponível para Venda",
    "Tamanho": 5,
    "Editavel": True,
    "Conteudo": "",
    "Topo": 12,
    "Esquerda": 7,}
LstCampos.append(Campo4)

def ImprimirCadProd(Editar):
    if Editar:
        CarregarDadosPrd(LstCampos)
    #Limpa a tela.
    os.system('cls')     
    Funcoes.Moldura(2, 2, 20, 80, 'Cadastro de Produtos')
    Funcoes.montarFormulario(LstCampos, Editar)
    if Editar:
        LstCampos[0]["Editavel"] = False
    else:
        LstCampos[0]["Editavel"] = True

    Funcoes.LerCampos(LstCampos, 'PRODUTO', Editar)

def ImprimirConsultaProd():
    os.system('cls')     
    Funcoes.Moldura(2, 2, 30, 95, 'Consulta de Produtos ')
    Funcoes.ImprimirCampo(4, 6, 40, 'Código do Produto', ' ')
    Funcoes.PosCur(4, 26)
    CodDigitado = str(input())
    Funcoes.PosCur(6, 4)
    #Imprime linha dividindo a tela 
    print(Funcoes.colored(000, 000, 000, ' '.ljust(70, '-'))) 
    Funcoes.PosCur(7, 5)
    print('Produtos Encontrados: ')
    Funcoes.PosCur(8, 5)
    print('Código  Nome                                     Tipo              Preço      Disponível')
    Res = Dados.ConsultarProd(CodDigitado, '')
    
    Funcoes.PosCur(9, 5)
    if len(Res) > 0:
        print(str(Res[0]).ljust(6, ' ')+'  '+str(Res[1]).ljust(40, ' ')+' '+str(Res[2]).ljust(17, ' ')+' '+str(Res[3]).ljust(10, ' ')+' '+str(Res[4]).ljust(5, ' '))
        Tecla = chr(0)
        while Tecla != chr(27) and Tecla != chr(13): #Tecla esc interrompe o laco.    
            Funcoes.PosCur(28, 38)
            print(Funcoes.colored(255, 255, 255, 'SAIR'), end='')    
            Funcoes.PosCur(28, 34)
            msvcrt.kbhit() #pega a tecla pressionada.
            Tecla = msvcrt.getch().decode('ISO8859-1')
    
def GravarCadProd(LstCampos):
        Dados.GravarProd(LstCampos[0]["Conteudo"], LstCampos[1]["Conteudo"], LstCampos[2]["Conteudo"], LstCampos[3]["Conteudo"], LstCampos[4]["Conteudo"], LstCampos[0]["Editavel"])   

def ImprimirRelProd():
    os.system('cls')     
    Funcoes.Moldura(2, 2, 20, 120, 'Relatório de Produtos ')
    Funcoes.ImprimirCampo(4, 6, 4, 'Digite a Opção', ' ')
    Funcoes.PosCur(4, 24)
    print('  (0-Todos os Produtos 1-Somente Filmes 2-Séries 3-Documentários', end='')
    Funcoes.PosCur(5, 27)
    print('4-Todos os Produtos Disponíveis 5-Todos os Produtos Indisponíveis)', end='')
    Funcoes.PosCur(4, 23)
    Opcao = str(input())
    Funcoes.PosCur(6, 4)
     
    print(Funcoes.colored(000, 000, 000, ' '.ljust(110, '-'))) #Imprime linha dividindo a tela
    
    Funcoes.PosCur(8, 5)
    print('Código  Nome                                     Tipo          Preço       Disponível')
    Res = Dados.ConsultarProd('', Opcao)
    
    if len(Res) > 0:
        cont = 0
        while (cont < len(Res)):
            Funcoes.PosCur(9+cont, 5)
            print(str(Res[cont][0]).ljust(6, ' ')+'  '+str(Res[cont][1]).ljust(40, ' ')+' '+str(Res[cont][2]).ljust(14, ' ')+' '+str(Res[cont][3]).ljust(12, ' ')+' '+str(Res[cont][4]).ljust(11, ' '))
            cont += 1

        Tecla = chr(0)
        while Tecla != chr(27) and Tecla != chr(13): #Tecla esc interrompe o laco.    
            Funcoes.PosCur(20, 38)
            print(Funcoes.colored(255, 255, 255, 'SAIR'), end='')    
            Funcoes.PosCur(20, 34)
            msvcrt.kbhit() #pega a tecla pressionada.
            Tecla = msvcrt.getch().decode('ISO8859-1')

def CarregarDadosPrd(LstCampos):
    os.system('cls')     
    Funcoes.Moldura(2, 2, 30, 95, 'Alterar Produto ')
    Funcoes.ImprimirCampo(4, 6, 40, 'Código do Produto', ' ')
    Funcoes.PosCur(4, 26)
    CodDigitado = str(input())
    Res = Dados.ConsultarProd(CodDigitado, '')

    if len(Res) > 0:
        LstCampos[0]["Conteudo"] = str(Res[0])
        LstCampos[1]["Conteudo"] = str(Res[1])
        LstCampos[2]["Conteudo"] = str(Res[5])
        LstCampos[3]["Conteudo"] = str(Res[3])
        LstCampos[4]["Conteudo"] = str(Res[4])
