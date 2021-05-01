def Ler(filename):
    matriz = []
    i = 0

    with open(filename) as file_object:
        for line in file_object:
            linha = line.split("\t")
            n = len(linha)
            linha[n-1] = linha[n-1].replace("\n", "")
            j = 0
            while(j < n):
                linha[j] = int(linha[j])
                j = j + 1

            matriz.append(linha)
            i = i + 1

    return matriz
