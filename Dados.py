import sqlite3
import os
import pathlib
import Funcoes

NM_BD = "\\nerdflix.bd"

def VerificarOuCriarBD():
    if not os.path.exists(os.path.abspath(os.getcwd())+NM_BD):                      
        cnx = sqlite3.connect(os.path.abspath(os.getcwd())+NM_BD)
        cur = cnx.cursor() #cria cursor para o banco.
        cur.execute('''CREATE TABLE produtos
               (id INTEGER, nome text, tipo text, preco real, disponivel text)''')

        cur.execute('''CREATE TABLE clientes
               (id INTEGER, nome text, endereco text, cpf text, cidade_uf text, idade text, celular text)''')

        cur.execute('''CREATE TABLE vendas
           (id INTEGER, id_cliente text, id_produto text, preco real, data date)''')
        cnx.commit()

        #inserir dados fixos
        #Clientes
        cur.execute('''INSERT INTO clientes (id, nome, endereco, cpf, cidade_uf, idade, celular) VALUES (1, 'Taina', '00000000000', 'Rua Freitas', 'Coronel Freitas-SC', '23', '49/00000-0000')''')
        cur.execute('''INSERT INTO clientes (id, nome, endereco, cpf, cidade_uf, idade, celular) VALUES (1, 'Julia', '00000000000', 'Rua Chapeco', 'Chapecó-SC', '23', '49/99999-0000')''')
        #Produtos
        cur.execute('''INSERT INTO produtos (id, nome, tipo, preco, disponivel) VALUES (1, 'The Big Bang Theory', '1', '20,50', 'SIM')''')
        cur.execute('''INSERT INTO produtos (id, nome, tipo, preco, disponivel) VALUES (2, 'Suits', '1', '20,50', 'SIM')''')
        cur.execute('''INSERT INTO produtos (id, nome, tipo, preco, disponivel) VALUES (3, 'Eternal Sunshine of the Spotless Mind', '2', '10,00', 'SIM')''')
        cur.execute('''INSERT INTO produtos (id, nome, tipo, preco, disponivel) VALUES (4, 'Prison Break', '1', '20,50', 'SIM')''')
        cur.execute('''INSERT INTO produtos (id, nome, tipo, preco, disponivel) VALUES (5, 'E o Vento Levou', '2', '10,00', 'SIM')''')
        cur.execute('''INSERT INTO produtos (id, nome, tipo, preco, disponivel) VALUES (6, 'Chernobyl', '3', '15,00', 'SIM')''')
        cnx.commit()
        cnx.close()
    
def GravarProd(id, nome, tipo, preco, disponivel, inserir):
    cnx = sqlite3.connect(os.path.abspath(os.getcwd())+NM_BD)
    cur = cnx.cursor() #cria cursor para o banco.
    disponivel = str(disponivel).upper()
    if inserir:
        cur.execute("INSERT INTO produtos (id, nome, tipo, preco, disponivel) VALUES  (?,?,?,?,?)", [id, nome, tipo, preco, disponivel])
    else:
        cur.execute("UPDATE produtos set nome=?, tipo=?, preco=?, disponivel=? WHERE id = ?", [nome, tipo, preco, disponivel, id])
    #finaliza gravação
    cnx.commit()
    cnx.close()

def ConsultarProd(codigo, tipo):          
    cnx = sqlite3.connect(os.path.abspath(os.getcwd())+NM_BD)
    cur = cnx.cursor() #cria cursor para o banco.
    if codigo != '':
        cur.execute("select id, nome, case when tipo = 1 then 'Série' when tipo = 2 then 'Filme' when tipo = 3 then 'Documentário' end as Tipo, preco, upper(disponivel), Tipo as Tipo1 from produtos WHERE id = ?", [codigo])
        Row = cur.fetchall()
        Consulta = []

        if len(Row) == 0:
            Funcoes.Mensagem('Nenhum Produto Localizado!', True)
        else:
            Consulta = Row[0]    
    else:
        if tipo != '':
            if tipo == '0':
                cur.execute("select id, nome, case when tipo = 1 then 'Série' when tipo = 2 then 'Filme' when tipo = 3 then 'Documentário' end as Tipo, preco, upper(disponivel) from produtos")
            else:
                if int(tipo) >= 4:
                    if int(tipo) == 4:
                        disp = 'SIM'
                    elif int(tipo) == 5:                
                        disp = 'NAO'
                    cur.execute("select id, nome, case when tipo = 1 then 'Série' when tipo = 2 then 'Filme' when tipo = 3 then 'Documentário' end as Tipo, preco, upper(disponivel) from produtos WHERE disponivel = ?", [disp])
                else:                    
                    if int(tipo) == 1:
                        tipo = 2
                    elif int(tipo) == 2:
                        tipo = 1
                    elif int(tipo) == 3:
                        tipo = 3                
                    cur.execute("select id, nome, case when tipo = 1 then 'Série' when tipo = 2 then 'Filme' when tipo = 3 then 'Documentário' end as Tipo, preco, upper(disponivel) from produtos WHERE tipo = ?", [tipo])                        
                      
        Row = cur.fetchall()
        Consulta = []
        if len(Row) == 0:
            Funcoes.Mensagem('Nenhum Produto Localizado!', True)
        else:
            Consulta = Row
    
    #fecha conexao com o banco    
    cnx.close()
    return Consulta

    
def GravarClie(id, nome, ender, cpf, cidadeUf, idade, celular):
    cnx = sqlite3.connect(os.path.abspath(os.getcwd())+NM_BD)
    cur = cnx.cursor() #cria cursor para o banco.
    cur.execute("INSERT INTO clientes (id, nome, endereco, cpf, cidade_uf, idade, celular) VALUES  (?,?,?,?,?,?,?)",(id, nome, ender, cpf, cidadeUf, idade, celular))
    #finaliza gravação
    cnx.commit()
    cur.close()

def ConsultarClie():          
    cnx = sqlite3.connect(os.path.abspath(os.getcwd())+NM_BD)
    cur = cnx.cursor() #cria cursor para o banco.
    
    cur.execute("SELECT * FROM clientes")
    Row = cur.fetchall()
    Consulta = []

    if len(Row) == 0:
        Funcoes.Mensagem('Nenhum Cliente Localizado!', False)
    else:
        Consulta = Row
  
    #fecha conexao com o banco    
    cnx.close()
    return Consulta

def RetornarNomeClie(Cod):
    Nome = ''
    cnx = sqlite3.connect(os.path.abspath(os.getcwd())+NM_BD)
    cur = cnx.cursor() #cria cursor para o banco.
    
    cur.execute("SELECT nome FROM clientes where ID = ?", [Cod])
    Row = cur.fetchall()
    Consulta = []

    if len(Row) == 0:
        Funcoes.Mensagem('Nenhum Cliente Localizado!', False)
    else:
        Nome = Row[0][0]
  
    #fecha conexao com o banco    
    cnx.close()
    return Nome



#projetado para cada venda ter apenas 1 produto, nao eh a intencao demonstrar o processo detalhado. Assim evitamos criar um "mestre-detalhe"
def GravarVenda(id, idClie, idProd, preco, data):
    cnx = sqlite3.connect(os.path.abspath(os.getcwd())+NM_BD)
    cur = cnx.cursor() #cria cursor para o banco.
    cur.execute("INSERT INTO vendas (id, id_cliente, id_produto, preco, data) VALUES  (?,?,?,?,?)",(id, idClie, idProd, preco, data))
    #finaliza gravação
    cnx.commit()
    cur.close()

def ProdIndisp(CodProd):
    cnx = sqlite3.connect(os.path.abspath(os.getcwd())+NM_BD)    
    cur = cnx.cursor() #cria cursor para o banco.
    cur.execute("update produtos set disponivel=? where id = ?",['NAO', CodProd])
    cur.fetchall()
    cnx.commit()
    cur.close()    

def RetornarIDVenda():
    cnx = sqlite3.connect(os.path.abspath(os.getcwd())+NM_BD)    
    cur = cnx.cursor() #cria cursor para o banco.
    cur.execute("select coalesce(max(id),0) from vendas")
    id = cur.fetchall()[0][0]
    if id == '':
        id = '0'
        
    cnx.close()
    return int(id)+1

def ConsultarVendas(IdVenda):          
    cnx = sqlite3.connect(os.path.abspath(os.getcwd())+NM_BD)
    cur = cnx.cursor() #cria cursor para o banco.
    
    if IdVenda == '':
        cur.execute("SELECT * FROM vendas")
    else:
        cur.execute("SELECT * FROM vendas where id = ?",[IdVenda])

    Row = cur.fetchall()
    Consulta = []

    if len(Row) == 0:
        Funcoes.Mensagem('Nenhuma Venda Localizada!', False)
    else:
        Consulta = Row
  
    #fecha conexao com o banco
    cnx.close()
    return Consulta

