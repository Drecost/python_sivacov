import os
from cidadao import Cidadao

class CidadaoView:

    def cadastrar(self):
        clear = 'cls' if os.name == 'nt' else 'clear'
        os.system(clear)

        cidadao = Cidadao()

        num_cid = int(input("Quantos registros de cidadao quer criar: "))
        for n in range(1, num_cid  + 1):
            print("Entre com os dados do cidadão # ", n)
            cpf = input("CPF: ")
            nome = input("Nome: ")    
            email = input("E-mail: ") 
            telefone = input("Telefone: ")
            cep = input("CEP: ")
            data_nascimento = input("Data de Nascimento: ")
            profissao = input("Profissão: ")
            cidadao.cadastrar( cpf,nome,email,telefone,cep,data_nascimento,profissao)    
            print() 

        print("Cidadãos cadastrados com sucesso!!!")

