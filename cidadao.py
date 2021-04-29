import sqlite3
from conexao import Conexao

class Cidadao:

    def cadastrar(self,cpf,nome,email,telefone,cep,data_nascimento,profissao):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'INSERT INTO Cidadao (cpf,nome,email,telefone,cep,data_nascimento,profissao) VALUES (?,?,?,?,?,?,?)'
            cursor.execute(sql,(cpf,nome,email,telefone,cep,data_nascimento,profissao))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de cidadãos: {}".format(e))
            return False

