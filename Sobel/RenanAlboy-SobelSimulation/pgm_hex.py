import os, sys
from numpy import *
from numpy.linalg import *
from PIL import Image

def hexToPgm(file_in, file_out):
    arq = open(file_in, 'r+')
    out = open(file_out, 'w+')

    larg = 640
    altura = 480

    linhas = arq.readlines()
    out_mat = zeros((altura,larg))
    out_mat[1:0][1:0] = 0

    for x in range(larg):
        for y in range(altura):
            i = (y*larg)+x
            #print(i)
            count  = linhas[i]
            #print(count)
            out_mat[y][x] = int(count, base=16)
    #print(out_mat)

    for i in range(0, larg):
        #print('\n')
        for j in range(0, altura):
            a = str(out_mat[i][j])
            out.write(a)
            #print('Elemento: ', i, ',', j)
            #print('   ')
	
hexToPgm('resultado.hex', 'saida.txt')	
