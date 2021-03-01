def salvar(dados):
    # Salva os dados do programa em arquivo txt na forma de string
    # Composição de dados na possição zero 
    pessoas = ""
    salas = ""
    cafes = ""
    for i in dados[0] :
        pessoas += i.gerar_string()
    for i in dados[1] :
        salas += i.gerar_string()
    for i in dados[2] :
        cafes += i.gerar_string()
    arquivo =  open("data.txt", "w+")
    arquivo.write(pessoas + "\n")
    arquivo.write(salas + "\n")
    arquivo.write(cafes + "\n")
    arquivo.close() 
def ler():
    # Ler dados gravados em txt e transformalos em listas para que o programa consiga tranformalos em objetos novamente
    arquivo = open("data.txt", "r")
    auxiliar = list(arquivo)
    pessoas = []
    salas = []
    cafes = []
    try:
        au_pessoas = auxiliar[0]

    except IndexError:
        au_pessoas = []
    try:
        au_salas = auxiliar[1] 
    except IndexError:
        au_salas = []
    try:
        au_cafes = auxiliar[2]
    except IndexError:
        au_cafes = []
    if au_pessoas != []:
        au_pessoas = au_pessoas.split(",")

        au_pessoas.remove("\n")
        for pessoa in au_pessoas:
            pessoa = pessoa.split("/")
            pessoa[2] = pessoa[2].split("#")
            pessoa[3] = pessoa[3].split("#")
            pessoas.append(pessoa)
    if au_salas != []:
        au_salas = au_salas.split(",")
        au_salas.remove("\n")
        for sala in au_salas:
            sala = sala.split("/")
            sala[2] = sala[2].split("#")
            sala[3] = sala[3].split("#")
            salas.append(sala)

    if au_cafes != []:
        au_cafes = au_cafes.split(",")
        au_cafes.remove("\n")
        for cafe in au_cafes:
            cafe = cafe.split("/")
            cafe[1] = cafe[1].split("#")
            cafe[2] = cafe[2].split("#")
            cafes.append(cafe)
    arquivo.close()    
    return pessoas, salas, cafes


