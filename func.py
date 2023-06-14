def lerString (mensagem):
    while True:
        variavel = input(mensagem)
        if variavel.find(" ") >= 1:
            print("valor informado incorrentamente")
        elif len(variavel) >=1:
            return variavel