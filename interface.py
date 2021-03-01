def tela_principal() :
    print("cadastrar pessoa - 1")
    print("cadastrar sala de evento - 2")
    print("cadastrar  cafeteria de café - 3")
    print("consultar pessoa - 4")
    print("consultar sala - 5")
    print("consultar cafeteria - 6")
    print("salvar - 7")
    print("Sair - 0")
    operacao = int(input("digite o valor da operação desejada: ")) 
    return operacao
def input_gui(operacao) :
    if operacao == 0 :
        nome = input("colocar nome: ")
        sobrenome = input("colocar sobrenome: ")
        return nome, sobrenome
    elif operacao == 1:
        nome = input("digite o nome da sala: ")
        lotacao =int(input("digite o numero de locação: "))
        return nome, lotacao
    else :
        nome = input("digite o nome da cafeteria: ")
        return nome
def imprimir(valor) :
    print(valor)
