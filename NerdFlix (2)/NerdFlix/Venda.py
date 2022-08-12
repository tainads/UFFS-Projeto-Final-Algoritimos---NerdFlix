import Dados
import Funcoes
import os
import msvcrt
from datetime import date

def RegistarVenda():
    os.system('cls')     
    Funcoes.Moldura(2, 2, 30, 85, 'Registrar Vendas ')
    Funcoes.ImprimirCampo(4, 6, 42, 'Cód. do Comprador', ' ')    
    Funcoes.PosCur(4, 24)
    #le o código do cliente.
    CodClie = str(input())
    #busca os dados do cliente.
    NomeClie = Dados.RetornarNomeClie(CodClie)
    Funcoes.PosCur(4, 26)
    print(NomeClie, end='')

    contProd = 0
    IdVenda = Dados.RetornarIDVenda()
    CodDigitado = '-1'
    while CodDigitado != '':
        Funcoes.PosCur(5, 26)
        #Solicita o codigo do produto
        Funcoes.ImprimirCampo(5, 6, 40, 'Cód. do Produto', ' ')
        Funcoes.PosCur(5, 23)
        #ler o codigo do produto
        CodDigitado = str(input())
        if CodDigitado != '' :
            #exibir os dados do produto
            Funcoes.PosCur(6, 4)
            print(Funcoes.colored(000, 000, 000, ' '.ljust(70, '-'))) #Imprime linha dividindo a tela
            Funcoes.PosCur(7, 5)
            print('Código  Nome                                     Tipo            Preço')
            #Consulta o produto pelo código digitado.
            Res = Dados.ConsultarProd(CodDigitado, '')
    
            #se encontrou algum produto com o codigo digitado
            if (len(Res) > 0):
                #se produto não disponível então imprime uma mensagem para o usuário
                if (str(Res[4]) == 'NAO'):
                    Funcoes.Mensagem('Produto Não Disponível', True)
                else:
                    Funcoes.PosCur(8+contProd, 5)
                    contProd += 1
                    #imprime os dados do produto selecionado.
                    print(str(Res[0]).ljust(6, ' ')+'  '+str(Res[1]).ljust(40, ' ')+' '+str(Res[2]).ljust(14, ' ')+' '+str(Res[3]).ljust(12, ' ')+' ')
                    #marca produto como indisponivel.
                    Dados.ProdIndisp(CodDigitado)
                    #id, idClie, idProd, preco, data
                    Dados.GravarVenda(IdVenda, CodClie, Res[0], Res[3], date.today())
            


    #aguarda usuario teclar enter no "finalziar"
    Tecla = chr(0)
    while Tecla != chr(27) and Tecla != chr(13): #Tecla esc interrompe o laco.    
        Funcoes.PosCur(20, 38)
        print(Funcoes.colored(255, 255, 255, 'Finalizar'), end='')    
        Funcoes.PosCur(20, 34)
        msvcrt.kbhit() #pega a tecla pressionada.
        Tecla = msvcrt.getch().decode('ISO8859-1')
    
    ImprimirVenda(IdVenda)
    
    
def ImprimirVenda(id):
    os.system('cls')     
    if id == '':
        Funcoes.Moldura(2, 2, 40, 71, ' Relatório de Vendas ')
    else:
        Funcoes.Moldura(2, 2, 40, 71, 'Demonstrativo da Venda ')
       
    #id INTEGER, id_cliente text, id_produto text, preco real, data date
    Res = Dados.ConsultarVendas(id)

    cont = 0
    topo = 4
    if len(Res) > 0:
        cont = 0
        topo = 4
        while (cont < len(Res)):
            #zera o totalizador da venda
            TotalVenda = 0            
            IdVenda = Res[cont][0]
            #busca os dados do cliente.
            IdClie = Res[cont][1]
            NomeClie = Dados.RetornarNomeClie(IdClie)
            Funcoes.PosCur(topo+cont, 4)
            #imprime o nome do cliente
            print('Cliente:'+NomeClie.ljust(30, ' '), end='')
            print("Data da Venda: ", end='')
            print(str(Res[cont][4]), end='')
            topo += 1
            Funcoes.PosCur(topo+cont, 4)
            #Imprime linha dividindo a tela 
            print(Funcoes.colored(000, 000, 000, ''.ljust(65, '-'))) 
            
            topo += 1
            Funcoes.PosCur(topo+cont, 5)
            print("Cód. Prod. Descrição                              Preço ", end='')            
            topo += 1
            #enquanto for a mesma venda, imprime os produtos desta venda
            while cont < len(Res) and IdVenda == Res[cont][0]:
                #pega os dados do produto
                IdProd = str(Res[cont][2])
                ResPrd = Dados.ConsultarProd(IdProd, '')
                NomeProd = ResPrd[1]                
                #topo += 1
                Funcoes.PosCur(topo+cont, 5)

                print(str(Res[cont][2]).ljust(9, ' ')+'  '+str(NomeProd).ljust(38, ' ')+' '+str(Res[cont][3]).ljust(14, ' '))
                TotalVenda += float(str(Res[cont][3]).replace(',', '.'))
                cont += 1                
                Funcoes.PosCur(topo+cont, 5)
            
            Total = "{:.2f}".format(TotalVenda)
            print(f"                        Valor da Venda: R$ {Total}", end='')
            #Imprime linha dividindo a tela             
            topo += 1
            Funcoes.PosCur(topo+cont, 4)
            print(Funcoes.colored(000, 000, 000, ''.ljust(65, '='))) 
            topo += 1

    Funcoes.PosCur(topo+cont+2, 5)
    #aguarda usuario teclar enter no "finalziar"
    Tecla = chr(0) #inicializa com null
    #Tecla esc interrompe o laco.
    while Tecla != chr(27) and Tecla != chr(13): 
        Funcoes.PosCur(topo+cont+2, 38)
        print(Funcoes.colored(255, 255, 255, 'SAIR'), end='')
        Funcoes.PosCur(topo+cont+2, 34)
        msvcrt.kbhit() #pega a tecla pressionada.
        Tecla = msvcrt.getch().decode('ISO8859-1')    
