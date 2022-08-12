import Funcoes
import keyboard
import msvcrt
import os
import sqlite3
import CadProd
import CadClie
import Dados
import Venda

import platform
if platform.system().lower() == 'windows':
    from ctypes import windll, c_int, byref
    stdout_handle = windll.kernel32.GetStdHandle(c_int(-11))
    mode = c_int(0)
    windll.kernel32.GetConsoleMode(c_int(stdout_handle), byref(mode))
    mode = c_int(mode.value | 4)
    windll.kernel32.SetConsoleMode(c_int(stdout_handle), mode)

os. system('color Df') #seta a cor de fundo e da letra
Dados.VerificarOuCriarBD()
IdxOpcao = 0
os.system('cls')
Funcoes.Moldura(2, 10, 6, 19, ' Nerdflix')
Funcoes.MenuPrincipal(2, 12, IdxOpcao)

#Constantes
MENU_PRINCIPAL = 1
SUB_MENU_CLIENTES = 2
SUB_MENU_PRODUTOS = 3

SEL_CLIE = 1
SEL_PROD = 2
SEL_VENDAS = 3
SEL_REL_VENDAS = 4
SEL_SAIR = 4

SEL_CONS_PROD = 1
SEL_CAD_PROD = 2
SEL_EDIT_PROD = 3
SEL_REL_PROD = 4
SEL_CAD_CLIE = 2
SEL_REL_CLIE = 1

TamanhoMenuAtual = 5
Tecla = chr(0) # inicializa com null.
MenuAtual = 1 #menu atual 1 = Principal 2 = submenu Cliente 3 = submenu produto 
 #Inativa todos cadastros
CadProdAtivo = False
EditProdAtivo = False
CadClieAtivo = False 
ConsProdAtivo = False
RelProdAtivo = False
RelClieAtivo = False

while Tecla != chr(27): #Tecla esc interrompe o laco.    
    Funcoes.PosCur(1, 5)    
    #print(Funcoes.colored(255, 255, 255, 'Selecione uma opção ou tecle ESC para sair.'), end='')    
    msvcrt.kbhit() #pega a tecla pressionada.
    Tecla = msvcrt.getch().decode('ISO8859-1') #armazena o valor da tecla decodificado.
    if Tecla == chr(80): #para baixo.
        if IdxOpcao < TamanhoMenuAtual:
            IdxOpcao += 1 #vai para o proximo abaixo.
        else:
            IdxOpcao = SEL_CLIE #se esta no ultimo entao volta para o primeiro.
    elif Tecla == chr(72): #para cima.
        if IdxOpcao > 1:
            IdxOpcao -= 1 #vai para o proximo a cima.
        else:
            IdxOpcao = SEL_SAIR #se esta no primeiro entao volta para o ultimo.

    elif Tecla == chr(75): #esquerda
        if MenuAtual == SUB_MENU_CLIENTES:
            MenuAtual = MENU_PRINCIPAL
            TamanhoMenuAtual = 2
            IdxOpcao = SEL_CLIE
            os.system('cls')
        if MenuAtual == SUB_MENU_PRODUTOS: 
            MenuAtual = MENU_PRINCIPAL
            TamanhoMenuAtual = 4
            IdxOpcao = SEL_PROD
            os.system('cls')

        #elif IdxOpcao == 5:             
    elif Tecla == chr(13): #enter.
        if (MenuAtual == MENU_PRINCIPAL) & (IdxOpcao == SEL_CLIE):
            MenuAtual = SUB_MENU_CLIENTES
            TamanhoMenuAtual = 3
        elif (MenuAtual == MENU_PRINCIPAL) & (IdxOpcao == SEL_PROD):
            MenuAtual = SUB_MENU_PRODUTOS
            IdxOpcao = 1
            TamanhoMenuAtual = 4
        elif (MenuAtual == SUB_MENU_PRODUTOS) & (IdxOpcao == SEL_CAD_PROD):            
            CadProdAtivo = True
        elif (MenuAtual == SUB_MENU_PRODUTOS) & (IdxOpcao == SEL_EDIT_PROD):            
            EditProdAtivo = True           
        elif (MenuAtual == SUB_MENU_PRODUTOS) & (IdxOpcao == SEL_CONS_PROD):
            ConsProdAtivo = True            
        elif (MenuAtual == SUB_MENU_PRODUTOS) & (IdxOpcao == SEL_REL_PROD):            
            RelProdAtivo = True
        elif (MenuAtual == SUB_MENU_CLIENTES) & (IdxOpcao == SEL_CAD_CLIE):
            CadClieAtivo = True
        elif (MenuAtual == SUB_MENU_CLIENTES) & (IdxOpcao == SEL_REL_CLIE):    
            RelClieAtivo = True
        elif (MenuAtual == MENU_PRINCIPAL) & (IdxOpcao == SEL_VENDAS):            
            Venda.RegistarVenda()
        elif (MenuAtual == MENU_PRINCIPAL) & (IdxOpcao == SEL_REL_VENDAS):            
            Venda.ImprimirVenda('')
        elif (MenuAtual == MENU_PRINCIPAL) & (IdxOpcao == SEL_SAIR):
            os. system('color 07')#volta a cor normal
            os.system('cls')
            break
        
    if MenuAtual == MENU_PRINCIPAL:
        os.system('cls')
        Funcoes.Moldura(2, 10, 6, 19, ' Nerdflix')
        Funcoes.MenuPrincipal(2, 12, IdxOpcao)

    elif MenuAtual == SUB_MENU_CLIENTES:
        if CadClieAtivo:
            CadClie.ImprimirCadClie()
            CadClieAtivo = False            
        elif RelClieAtivo:
            CadClie.ImprimirRelClie()
            RelClieAtivo = False

        os.system('cls')
        Funcoes.Moldura(2, 10, 6, 19, ' Nerdflix')
        Funcoes.MenuPrincipal(2, 12, SEL_CLIE) #imprime novamente o menu principal        

        #nao utiliza elif por que se estiver saido do cadastro precisa imprimir a tela do menu.        
        if not CadClieAtivo:
            Funcoes.Moldura(3, 24, 4, 18, '')
            Funcoes.subMenuCliente(3, 25, IdxOpcao)

    elif MenuAtual == SUB_MENU_PRODUTOS:
        if CadProdAtivo:
            CadProd.ImprimirCadProd(False)
            CadProdAtivo = False
        elif EditProdAtivo:
            CadProd.ImprimirCadProd(True)
            EditProdAtivo = False            
        elif ConsProdAtivo:
            CadProd.ImprimirConsultaProd()            
            ConsProdAtivo = False            
        elif RelProdAtivo:
            CadProd.ImprimirRelProd()
            RelProdAtivo = False
        os.system('cls')
        Funcoes.Moldura(2, 10, 6, 19, ' Nerdflix')
        Funcoes.MenuPrincipal(2, 12, SEL_PROD) #imprime novamente o menu principal            

        #nao utiliza elif por que se estiver saido do cadastro precisa imprimir a tela do menu.    
        if not CadProdAtivo:
            Funcoes.Moldura(4, 24, 5, 19, '')
            Funcoes.subMenuProd(4, 25, IdxOpcao)