# MIT License
#
# Copyright (c) 2021 Igor Costa Carvalho Campos Silva
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
