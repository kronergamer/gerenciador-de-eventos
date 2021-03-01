from interface import tela_principal, input_gui, imprimir
from data import salvar, ler

class Pessoa():
    def __init__(self):
        self.nome = None
        self.sobrenome = None
        self.salas = [" ", " "]
        self.cafes = [" ", " "]

    def gerar_string(self) :
        dados = self.nome+"/"+ self.sobrenome+"/"
        if self.salas != [" ", " "]:
            for i in self.salas :
                dados += i +"#"
        else:
            dados += " "+ "#"
        dados += "/"
        if self.cafes != ["", ""]:
            for i in self.cafes :
                dados += i +"#"
        else:
            dados += " "+ "#"
        dados += ","    
        return dados

    def verificar(self, nome, sobrenome, numeros) :
        for i in nome :
            if i in numeros : 
                return False
        self.nome = nome
        for i in sobrenome : 
            if i in numeros : 
                return False
        self.sobrenome = sobrenome
        return True

    def receber_lista(self, dados) :
        self.nome = dados[0]
        self.sobrenome = dados[1]
        self.salas = dados[2]
        self.cafeterias = dados[3] 

class Sala_de_eventos():
    def __init__(self, nome = None, lotacao = None):
        self.nome = nome
        self.pessoas = [[], []]
        self.lotacao = lotacao

    def verificar(self, lotacao) :
        if lotacao <= int(self.lotacao +1) :
            return True
        return False

    def gerar_string(self):
        dados = self.nome + "/" + str(self.lotacao) + "/" 
        if self.pessoas == [] :
            for i in self.pessoas[0] :
                dados += i.nome + i.sobrenome + "#"
        else:
            dados += " "+ "#"
        
        dados += "/"
        if self.pessoas == [] :
            for i in self.pessoas[1] :
                dados += i.nome + i.sobrenome + "#"
        else:
            dados += " "+ "#"
        dados += ","
        return dados

    def add_pessoa(self, pessoa, etapa) :
        print(self.pessoas[0])
        print(self.pessoas[1])
        self.pessoas[etapa].append(pessoa)
        pessoa.salas[etapa] = self.nome

    def receber_lista(self, dados) :
        self.nome = dados[0]
        self.lotacao = dados[1]
        if dados[2] != ['','']:
            self.pessoas = dados[2]
        else:
            self.pessoas = [[],[]]

    def dividir_sala(self) :
        meia_sala = [[],[]]
        for i in range(len(self.pessoas[0])) :
            if i == 0 or i%2 == 0 :
                meia_sala[0].append(self.pessoas[0][i])                
            else :
                meia_sala[1].append(self.pessoas[0][i])
                self.pessoas[0][i].sala[1] = self.nome
        self.pessoas[1] = meia_sala[1]
        return meia_sala[0] 

class Espaco_de_cafe():
    def __init__(self, nome =  None):
        self.nome = nome
        self.pessoas = [[], []]

    def gerar_string(self):
        dados = self.nome + "/"
        if self.pessoas == [] :
            for i in self.pessoas[0] :
                dados += i.nome + i.sobrenome + "#"
        else:
            dados += " "+ "#"
        dados += "/"
        if self.pessoas == [] :
            for i in self.pessoas[1] :
                dados += i.nome + i.sobrenome + "#"
        else:
            dados += " "+ "#"
        dados += ","
        return dados

    def add_pessoa(self, pessoa, etapa) :
        self.pessoas[etapa].append(pessoa)
        pessoa.cafes[etapa] = self.nome

    def receber_lista(self, dados) :
        self.nome = dados[0]
        if dados[1] !=['','']:
            self.pessoas = dados[1]
        else:
            self.pessoas = [[],[]]

def gerar_objetos(pessoas, salas, cafes):
    pessoa = []     
    sala = []
    cafe = []
    for i in pessoas:
        objeto = Pessoa()
        objeto.receber_lista(i)
        pessoa.append(objeto)
    for i in salas:
        objeto = Sala_de_eventos()
        objeto.receber_lista(i)
        sala.append(objeto)
    for i in cafes:
        objeto = Espaco_de_cafe()
        objeto.receber_lista(i)
        cafe.append(objeto)
    return pessoa, sala, cafe

def verificar_lotação(salas, lotacao): 
    for i in salas :
        auxiliar = i.verificar(lotacao)
        if not auxiliar :
            return False

def set_pessoas_salas(pessoas, salas, aumento):
    n_pessoas = len(pessoas)
    n_salas = len(salas)
    lotacao = n_pessoas//n_salas
    x = 0
    if verificar_lotação(salas, lotacao):
        for i in pessoas :
            if  x == len(salas):
                x = 0
            if  i.salas[0] == "" or aumento :
                salas[x].add_pessoa(i,0)
            x += 1
        alterar_etapa(salas)

def set_pessoas_cafeteria(pessoas, cafes, aumento):
    n_cafes = len(cafes)
    x = 0
    for i in pessoas :
        if x == n_cafes -1 :
            x = 0
        if i.cafes[0] == [] or aumento:
            cafes[x].add_pessoa(i, 0)
            if x + 1 == n_cafes: 
                cafes[0].add_pessoa(i, 1)
            else:    
                cafes[x+1].add_pessoa(i, 1) 
        x += 1

def selecionar(dados):
    pessoa = []
    sala = []
    cafe = []
    if dados[0] ==  1 :
        print("entrou")
        for i in dados[2] :
            print(i.nome + i.sobrenome == dados[1],i.nome + i.sobrenome, dados[1], i.sobrenome == dados[1],i.nome == dados[1] )
            if i.nome + i.sobrenome == dados[1]  : 
                print(i)       
                pessoa.append(i)    
            elif i.nome == dados[1] or i.sobrenome == dados[1]:
                pessoa.append(i)
        return pessoa
    if dados [0] == 2:
        for i in dados[2] :
                if i.nome == dados[1] :
                    sala.append(i)
        return sala
    if dados[0] == 3 :
        for i in dados[2] :
                if i.nome == dados[1] :
                  cafe.append(i)
        return cafe

def alterar_etapa(salas, auxiliar = None) :
    for i in salas :
        if auxiliar is not None :
            for pessoa in auxiliar :
                i.add_pessoa(pessoa,1)
        auxiliar = i.dividir_sala()
    for pessoa in auxiliar :
        salas[0].add_pessoa(pessoa,1)

def criar_evento(pessoas, salas, cafes):
    pessoas, salas, cafes = ler()
    pessoas, salas, cafes = gerar_objetos(pessoas, salas, cafes)
    return pessoas, salas, cafes

def main() :
    pessoas = []
    salas = []
    cafes = []
    pessoas_alocadas = True
    aumento = False 
    pessoas, salas, cafes = criar_evento(pessoas, salas,cafes)
    while True :
        if pessoas != [] and salas != [] and cafes != []:
            if  not pessoas_alocadas:
                set_pessoas_salas(pessoas, salas, aumento)
                set_pessoas_cafeteria(pessoas, cafes, aumento)
                pessoas_alocadas = True
                aumento = False 
        operacao = tela_principal()
        if operacao == 1 :
            nome, sobrenome = input_gui(0)
            numeros = ['0','1', '2', '3', '4','5', '6', '7', '8', '9']
            pessoa = Pessoa()
            pessoa.verificar(nome, sobrenome, numeros)
            pessoas.append(pessoa)
            pessoas_alocadas = False
        elif operacao == 2 :
            nome, lotacao = input_gui(1)
            sala = Sala_de_eventos(nome, lotacao)
            salas.append(sala)
            aumento = True
            pessoas_alocadas = False
        elif operacao == 3:
            nome = input_gui(2)
            cafe = Espaco_de_cafe(nome)
            cafes.append(cafe)
            aumento = True
            pessoas_alocadas = False
        elif operacao == 4 :
            nome, sobrenome= input_gui(0)
            dados = [ 1, nome + sobrenome, pessoas]
            valor = selecionar(dados)
            imprimir(valor)
        elif operacao == 5 :
            nome, lotacao = input_gui(1)
            dados = [ 2, nome, salas]
            valor = selecionar(dados)
            imprimir(valor)
        elif operacao == 6 :
            nome = input_gui(2)
            dados = [ 3, nome, cafes]
            valor = selecionar(dados)
            imprimir(valor)
        elif operacao == 7:
            dados =[ pessoas, salas, cafes]
            salvar(dados)
        elif operacao == 0 :
            dados =[ pessoas, salas, cafes]
            salvar(dados)
            exit(0)
        else: 
            print("erro valor invalido")