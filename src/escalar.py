def Escalador(A, a):
    i = 0
    while(i < 4):
        j = 0
        while(j < 4):
            A[i][j] = A[i][j] * a
            j = j + 1

        i = i + 1

    return A
