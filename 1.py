A = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
    ]

var = 0

for i in A:
    if(var == 5):
        print('\n')

    print ('  '.join(map(str, i)))
    var+=1

linha = input('Digite a Linha:  ')

if(linha == 'A' or 'a'):
    linha = 0
elif(linha == 'B' or 'b'):
    linha = 1
elif(linha == 'C' or 'c'):
    linha = 2
elif(linha == 'D' or 'd'):
    linha = 3
elif(linha == 'E' or 'e'):
    linha = 4
elif(linha == 'F' or 'f'):
    linha = 5
elif(linha == 'G' or 'g'):
    linha = 6
elif(linha == 'H' or 'h'):
    linha = 7
elif(linha == 'I' or 'i'):
    linha = 8
elif(linha == 'J' or 'j'):
    linha = 9
elif(linha == 'K' or 'k'):
    linha = 10
elif(linha == 'L' or 'l'):
    linha = 11
elif(linha == 'M' or 'm'):
    linha = 12
elif(linha == 'N' or 'n'):
    linha = 13
elif(linha == 'O' or 'o'):
    linha = 14
elif(linha == 'P' or 'p'):
    linha = 15
elif(linha == 'Q' or 'q'):
    linha = 16
elif(linha == 'R' or 'r'):
    linha = 17
elif(linha == 'S' or 's'):
    linha = 18
elif(linha == 'T' or 't'):
    linha = 19
elif(linha == 'U' or 'u'):
    linha = 20
else:
    print ('Digita uma letra certa')


coluna = input('Digite as Colunas: ')

