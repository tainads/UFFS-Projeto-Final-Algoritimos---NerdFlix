import Funcoes
import os
import msvcrt
import sys
import Dados
Campo = {
    "NomeCampo": "CodClie",
    "TituloCampo": "Código do Cliente",
    "Tamanho": 7,
    "Editavel": True,
    "Conteudo": "",
    "Topo": 4,
    "Esquerda": 7,}
LstCamposClie = [Campo]

Campo1 = {
    "NomeCampo": "NomeClie",
    "TituloCampo": "Nome Cliente",
    "Tamanho": 40,
    "Editavel": True,
    "Conteudo": "",
    "Topo": 6,
    "Esquerda": 7,}
LstCamposClie.append(Campo1)

Campo2 = {
    "NomeCampo": "CpfClie",
    "TituloCampo": "CPF",
    "Tamanho": 14,
    "Editavel": True,
    "Conteudo": "",
    "Topo": 8,
    "Esquerda": 7,}
LstCamposClie.append(Campo2)

Campo3 = {
    "NomeCampo": "EnderecoClie",
    "TituloCampo": "Endereço",
    "Tamanho": 40,
    "Editavel": True,
    "Conteudo": "",
    "Topo": 10,
    "Esquerda": 7,}
LstCamposClie.append(Campo3)

Campo4 = {
    "NomeCampo": "CidadeUFClie",
    "TituloCampo": "Cidade-UF",
    "Tamanho": 40,
    "Editavel": True,
    "Conteudo": "",
    "Topo": 12,
    "Esquerda": 7,}
LstCamposClie.append(Campo4)

Campo5 = {
    "NomeCampo": "IdadeClie",
    "TituloCampo": "Idade",
    "Tamanho": 3,
    "Editavel": True,
    "Conteudo": "",
    "Topo": 14,
    "Esquerda": 7,}    
LstCamposClie.append(Campo5)    

Campo6 = {
    "NomeCampo": "CelClie",
    "TituloCampo": "Celular",
    "Tamanho": 20,
    "Editavel": True,
    "Conteudo": "",
    "Topo": 16,
    "Esquerda": 7,}    
LstCamposClie.append(Campo6)

def ImprimirCadClie():
    #Limpa a tela.
    os.system('cls')     
    Funcoes.Moldura(2, 2, 20, 80, 'Cadastro de Clientes')
    Funcoes.montarFormulario(LstCamposClie, False)
    Funcoes.LerCampos(LstCamposClie, 'CLIENTE', False)

def ImprimirRelClie():
    os.system('cls')     
    Funcoes.Moldura(2, 2, 20, 120, 'Relatório de Clientes ')    
    Funcoes.PosCur(4, 4)    
    print(Funcoes.colored(000, 000, 000, ' '.ljust(110, '-'))) #Imprime linha dividindo a tela    
    Funcoes.PosCur(6, 5)
    #nome text, endereco text, cpf text, cidade_uf text, idade text, celular
    print('Código  Nome                           Endereço                     CPF         Cidade-UF')
    Res = Dados.ConsultarClie()
    
    if len(Res) > 0:
        cont = 0
        while (cont < len(Res)):
            Funcoes.PosCur(7+cont, 5)
            print(str(Res[cont][0]).ljust(6, ' ')+'  '+str(Res[cont][1]).ljust(30, ' ')+' '+str(Res[cont][3]).ljust(28, ' ')+' '+str(Res[cont][2]).ljust(12, ' ')+' '+str(Res[cont][4]).ljust(11, ' '))
            cont += 1

        Tecla = chr(0)
        while Tecla != chr(27) and Tecla != chr(13): #Tecla esc interrompe o laco.    
            Funcoes.PosCur(20, 38)
            print(Funcoes.colored(255, 255, 255, 'SAIR'), end='')    
            Funcoes.PosCur(20, 34)
            msvcrt.kbhit() #pega a tecla pressionada.
            Tecla = msvcrt.getch().decode('ISO8859-1')    

def GravarCadClie(LstCampos):
        Dados.GravarClie(LstCampos[0]["Conteudo"], LstCampos[1]["Conteudo"], LstCampos[2]["Conteudo"], LstCampos[3]["Conteudo"], LstCampos[4]["Conteudo"], LstCampos[5]["Conteudo"], LstCampos[6]["Conteudo"])   
