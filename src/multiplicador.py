def Multiplicar(A, B):
    print(len(A[0]))
    print(len(B))
    if (len(A[0])) != (len(B)):
        print("Erro! Esta multiplicação não pode ser calculada")
    else:
        i = 0
        while(i < 4):
            j = 0
            while(j < 4):
                summ = 0
                k = 0
                while(k < 4):
                    summ = summ + A[i][k] * B[k][j]
                    k = k + 1
                A[i][j] = summ
                j = j + 1
            i = i + 1

    return A
