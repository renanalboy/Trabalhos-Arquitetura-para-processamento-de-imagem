# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 08:52:32 2017

@author: Renan Alboy
"""

import numpy as np
from PIL import Image


#função da conversão da matriz em vetor
def convertToArray(matriz, col, row):
    total = col*row
    vector = np.zeros(total)
    init = 0
    k = 0
    
    for i in range(init, row):
        for j in range(init, col):
            vector[k] = matriz[i][j]
            k = k + 1
    
    return vector
            
# Faz o apendice do vetros          
def completaVetor(vet, total):

        vet_append_a = np.zeros(9)
        vet_append_b = vet
        vet_append_c = np.zeros(9)
        
        for i in range(0,9):
            vet_append_a[i]=vet[i+1]
        
        for i in range(0,9):
            vet_append_c[i]=vet[total-10+i]
            
        vet_append = vet_append_a.tolist() + vet_append_b.tolist() + vet_append_c.tolist()                  
        
        return vet_append

    
    
#Filtro gaussiano
def gauss(array_base, curva):
    
    acumulate = 0
    t = len(array_base)-1 
    
    for i in range(0,9):
        acumulate = int(((array_base[i] + array_base[t-i]) // curva[i])) + acumulate
        
    acumulate = int((array_base[9] // curva[9])) + acumulate
    
    return acumulate
 
#      
def operacao(array, original, total, flag):
    array_return = np.zeros(total)
    
    if(flag == 1):
        for i in range(0,total):
            array_return[i] = original[i] - array[i]
    else:
        for i in range(0, total):
            if(array[i] != 0):
                array_return[i] = original[i] // array[i]
            else:
                array_return[i] = original[i] // 1
            
    return array_return 

#Faz o clip nos elementos do vetor, deixando-os em um range entre 50 e 255
def clipImage_gauss(vet_cliped, total):
    vet_retorno = vet_cliped
    
    for i in range(len(vet_cliped)):
        if(vet_retorno[i] < 50.0):
            vet_retorno[i] = 50
        elif(vet_cliped[i] > 255.0):
            vet_retorno[i] = 255
        else:
            vet_retorno[i] = vet_retorno[i]
           
#        print( vet_retorno)
        return vet_retorno
    
#transforma um vetor em uma matriz
def convToMatriz(line, row, vet):
    k = 0
    mat = np.zeros((line,row),dtype=np.uint8)
    for i in range(0,line):
        for j in range(0,row):
            mat[i][j] = vet[k]
            k=k+1
            
    return mat
    
#Converte a matriz em imagem png
def convToImage(line, row, vet):
    k=0
    w, h = line, row
    data = np.zeros((h, w, 3), dtype=np.uint8)
    
    for i in range(0,h):
        for j in range(0,w):
            data[i][j] = vet[k]
            k=k+1
            
    data[256, 256] = [255, 0, 0]
    img = Image.fromarray(data, 'RGB')
    img.save('image/normal.png')
    #img.show()
    
    
#Coloca anexo em araay_result para a utilização da imagem como vetor, tendo como
#objetivo a passagem do filtro gaussiano 5x5 em formato de vetor
def anexo(vet, n):
    
    vet_append_a = np.zeros(n)
    vet_append_b = vet
    vet_append_c = np.zeros(n)
            
    vet_append = vet_append_a.tolist() + vet_append_b.tolist() + vet_append_c.tolist()
    
    return vet_append

#Filtro gaussiano 5x5 (em formato de array)
def gauss_5x5(array_base, curva):
    
    acumulate = 0
    
    for i in range(0,25):
        acumulate = ((array_base[i]*curva[i]) + acumulate)//1
        
    return acumulate

#Filtro sobel
def sobel_filter(array_base,sobel):
    
    acumulate = 0
    
    for i in range(0,9):
        #print(i)
        acumulate = ((array_base[i]*sobel[i]) + acumulate)
        
    return acumulate


#Converte a matriz em imagem png
def convToImage2(line, row, vet):
    k=0
    w, h = line, row
    data = np.zeros((h, w, 3), dtype=np.uint8)
    
    for i in range(0,h):
        for j in range(0,w):
            data[i][j] = vet[k]
            k=k+1
            
    data[256, 256] = [255, 0, 0]
    img = Image.fromarray(data, 'RGB')
    img.save('image/sobel.png')
    #img.show()
    
    
    
    
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    