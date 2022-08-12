import os
import CadProd
import msvcrt
import CadClie

#funcao para imprimir uma moldura Topo = Posicao a partir do topo, Esquerda = Posicao a partir da margem esquerda, Altura = Altura da moldura, Largura = Largura da moldura.
def Moldura(Topo, Esquerda, Altura, Largura, Titulo):
    PosCur(Topo, Esquerda) #posiciona o cursor
    TopoAtual = Topo+1
    #inicia a impressao da moldura

    if Titulo != '': #calcula a posicao do titulo
        TamTitulo = len(Titulo)
        Parte = (Largura-2-TamTitulo)//2
        print('╔'.ljust(Parte,'═')+Titulo.ljust(Parte+TamTitulo,'═')+'╗')
    else:
        print('╔'.ljust(Largura-2,'═')+'╗')
    for TopoAtual in range(Topo+1, Topo+Altura):
        PosCur(TopoAtual, Esquerda)
        print('║'.ljust(Largura-2,' ')+'║'+colored(000, 000, 000, '█'))

    PosCur(TopoAtual+1, Esquerda)
    print('╚'.ljust(Largura-2, '═')+'╝'+colored(000, 000, 000, '█'))
    PosCur(TopoAtual+2, Esquerda)
    print(colored(000, 000, 000, ' '.ljust(Largura, '█')))

#Imprime o menu principal na posicao especificada.
def MenuPrincipal(Topo, Esquerda, IdxOpcaoSelecionada):
    
    PosCur(Topo+1, Esquerda)
    if IdxOpcaoSelecionada == 1:
        print(' =>Clientes<=')
    else:
        print('   Clientes  ')

    PosCur(Topo+2, Esquerda)
    if IdxOpcaoSelecionada == 2:
        print(' =>Produtos<=')
    else:    
        print('   Produtos  ')

    PosCur(Topo+3, Esquerda)
    if IdxOpcaoSelecionada == 3:
        print(' =>Vendas<=')
    else:
        print('   Vendas  ')

    PosCur(Topo+4, Esquerda)
    if IdxOpcaoSelecionada == 4:
        print(' =>Rel Vendas<=')
    else:
        print('   Rel Vendas  ')

    PosCur(Topo+5, Esquerda)
    if IdxOpcaoSelecionada == 5:
        print(' =>Sair<=')
    else:
        print('   Sair  ')

    PosCur(Topo+10, Esquerda)

def  SubMenu(IdxOpcao):
    if IdxOpcao == 5:
        exit
    else:
        print(f'submenu: {IdxOpcao}')

def LimparTela():
    #cls='\x1b[H'
    #print(cls, end='', flush=True)    
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def PosCur(Topo, Esquerda):
    print(f"\r\033[{Topo};{Esquerda}H", end="")

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def printColor(corFundo, corFonte, texto):
    print(f'\033[{corFundo};{corFonte}m' + texto, end='')

def subMenuCliente(Topo, Esquerda, IdxOpcaoSelecionada):
    
    PosCur(Topo+1, Esquerda)
    if IdxOpcaoSelecionada == 1:
        print(' =>Consultar<=')
    else:
        print('   Consultar  ')

    PosCur(Topo+2, Esquerda)
    if IdxOpcaoSelecionada == 2:
        print(' =>Cadastrar<=')
    else:
        print('   Cadastrar  ')

#    PosCur(Topo+3, Esquerda)
#    if IdxOpcaoSelecionada == 3:
#        print(' =>Alterar<=')
#    else:    
#        print('   Alterar  ')

def subMenuProd(Topo, Esquerda, IdxOpcaoSelecionada):
    
    PosCur(Topo+1, Esquerda)
    if IdxOpcaoSelecionada == 1:
        print(' =>Consultar<=')
    else:
        print('   Consultar  ')

    PosCur(Topo+2, Esquerda)
    if IdxOpcaoSelecionada == 2:
        print(' =>Cadastrar<=')
    else:
        print('   Cadastrar  ')

    PosCur(Topo+3, Esquerda)
    if IdxOpcaoSelecionada == 3:
        print(' =>Alterar<=')
    else:    
        print('   Alterar  ')        

    PosCur(Topo+4, Esquerda)
    if IdxOpcaoSelecionada == 4:
        print(' =>Relatório<=')
    else:    
        print('   Relatório  ')                

def ImprimirCampo(Topo, Esquerda, Tamanho, Titulo, Conteudo):

    PosCur(Topo, Esquerda+1)
    print(Titulo+': ', end='')
    print(colored(128, 128, 128, str(Conteudo).ljust(Tamanho, '█')))
    
    


def montarFormulario(LstCampos, Editar):
#LstCampos eh uma lista de objetos de dados. Formato esperado:
#Campo = {
#    "NomeCampo": "NomeProduto",
#    "TituloCampo": "Nome Exibido Abaixo do Campo",
#    "Tamanho": 20,
#    "Editavel": True,
#    "Conteudo": "Qualquer Conteudo",
#    "Topo": 5,
#    "Esquerda": 5,
# }    
    #imprime os campos na tela
    for cont in range(len(LstCampos)) :
        Campo = LstCampos[cont]
        if Editar:
            Conteudo = Campo["Conteudo"]
        else:
            Conteudo = ''
            
        ImprimirCampo(Campo["Topo"], Campo["Esquerda"], Campo["Tamanho"], Campo["TituloCampo"], Conteudo)


def PosicionaCursorCampo(LstCampos, CampoAtivo):
    Topo = LstCampos[CampoAtivo]["Topo"]
    #pega o inicio do campo na tela para posicionar o cursor
    Esquerda = LstCampos[CampoAtivo]["Esquerda"] + len(LstCampos[CampoAtivo]["TituloCampo"])+3
    PosCur(Topo, Esquerda)

def LerCampos(LstCampos, Tela, Editar):
    CampoAtivo = 0
    Palavra = ''

    while CampoAtivo < len(LstCampos):        
        PosicionaCursorCampo(LstCampos, CampoAtivo)
        if LstCampos[CampoAtivo]["Editavel"] == True:
            Palavra = str(input())

        if Palavra != '':
            LstCampos[CampoAtivo]["Conteudo"] = Palavra

        CampoAtivo += 1
        if CampoAtivo >= len(LstCampos):
            if Tela == 'PRODUTO':                    
                CadProd.GravarCadProd(LstCampos)
            elif Tela == 'CLIENTE':
                CadClie.GravarCadClie(LstCampos)

    #msvcrt.kbhit() #pega a tecla pressionada.
    #Tecla = msvcrt.getch().decode('ISO8859-1') #armazena o valor da tecla decodificado.    
    #while Tecla != chr(27): #Tecla esc interrompe o laco.            
        #if Tecla.isalpha():
            #Palavra = Palavra+Tecla
            #print(Funcoes.colored(255, 255, 255, Palavra), end='')
            
        #if (Tecla == '\t') or (Tecla == chr(13)): #teclou tab ou enter entao vai para o proximo campo
        #    CampoAtivo +=1

        #msvcrt.kbhit() #pega a tecla pressionada.
        #Tecla = msvcrt.getch().decode('ISO8859-1') #armazena o valor da tecla decodificado.

def Mensagem(msg, menor):
    if menor:
        Moldura(20, 26, 6, 40, ' Alerta ')
        PosCur(23, 34)
    else:
        Moldura(8, 10, 10, 60, '')
        PosCur(12, 29)
    
    print(msg)
    Tecla = chr(0)
    while Tecla != chr(27) and Tecla != chr(13): #Tecla esc interrompe o laco.    
        if menor:
            PosCur(24, 46)
        else:
            PosCur(22, 20)

        print(colored(255, 255, 255, 'OK'), end='')    
        if menor:
            PosCur(24, 46)
        else:
            PosCur(16, 38)
        
        msvcrt.kbhit() #pega a tecla pressionada.
        Tecla = msvcrt.getch().decode('ISO8859-1')    
        if menor:
            ApagarMensagem(20, 26, 6, 40)


def ApagarMensagem(Topo, Esquerda, Altura, Largura):
    PosCur(Topo, Esquerda) #posiciona o cursor
    TopoAtual = Topo+1
    print(' '.ljust(Largura-1,' '))
    for TopoAtual in range(Topo+1, Topo+Altura):
        PosCur(TopoAtual, Esquerda)
        print(' '.ljust(Largura-1,' ')+colored(000, 000, 000, ' '))

    PosCur(TopoAtual+1, Esquerda)
    print(' '.ljust(Largura-1, ' ')+colored(000, 000, 000, ' '))
    PosCur(TopoAtual+2, Esquerda)
    print(colored(000, 000, 000, ' '.ljust(Largura, ' ')))
