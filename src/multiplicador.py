def Multiplicar(A, B):
    print(len(A[0]))
    print(len(B))
    if (len(A[0])) != (len(B)):
        print("Erro! Esta multiplicação não pode ser calculada")
    else:
        C = []
        i = 0
        while(i < len(A)):
            line = []
            j = 0
            while(j < len(B[0])):
                line.append(0)
                j = j + 1

            C.append(line)
            i = i + 1


        i = 0
        while(i < 4):
            j = 0
            while(j < 4):
                summ = 0
                k = 0
                while(k < 4):
                    summ = summ + A[i][k] * B[k][j]
                    k = k + 1
                C[i][j] = summ
                j = j + 1
            i = i + 1

    return C
