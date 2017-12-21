# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 20:02:35 2017

@author: Renan Alboy
"""

import numpy as np
from PIL import Image
import functions as fc

# =============================================================================#
#              Entrada e tyratamento inicial do arquivo
# =============================================================================#
#Inicialização para valores da imagem
col = 288
row =  384
total = col*row
array_result = []

#Inicialização da imagem original e de saída/ conversão para tons de cinza
image_in = Image.open('image/110_5.tif')
img = image_in.convert('L')
img.save('image/gray_fingerprint_image.tif')

#Vetor que representa a curva que será passada sobre o imput
#Valores obtido a partir da geração de filtro no matlab utilizando
#gamma =5 como parametro
curva = [714, 500,370, 286, 233, 194, 167, 143, 152, 139, 152, 143, 167, 194, 233, 286, 379, 500, 714]

#abrir a imagem como uma matriz e também converte a matris para um array. 
#Matriz da img em tons de cinza
image_original = np.asarray(Image.open('image/gray_fingerprint_image.tif'))

array_original = fc.convertToArray(image_original, col, row)

#Vetor com as expanções laterais
array_completo = fc.completaVetor(array_original, total)
for i in range(0,total+18):
    array_completo[i] = int(array_completo[i]*256)
#print(array_completo)

# =============================================================================#
#               Bloco do primeiro filtro gaussiano
# =============================================================================#
#Aplicação do primeiro filtro de gauss
#Primeira passagem
for i in range(len(array_original)):
        array_analise = array_completo[i:i+19]
        pixel = fc.gauss(array_analise,curva)
        array_result = array_result + [pixel]

#Segunda Passagem do filtro gaussiano na primeira etapa . 
#Por reutilizar a função completaVetor necessita que seus parâmetros sejam em array 
#e não list. Assim, é necessário passar array_result pra array para que seja possível
#a concatenação do preambulo e do posambulo.
        
array_teste = np.zeros(total)

for i in range(0, total):
    array_teste[i] = array_result[i]

#Aplica o segundo filtro gaussiano na primeira parte   
array_completo_b = fc.completaVetor(array_teste, total)        
for i in range(len(array_result)):
        array_analise = array_completo_b[i:i+19]
        pixel = fc.gauss(array_analise,curva)
        array_result[i] = pixel

#retorna ao valor normal para utilização dos dados processados sem a multiplicação
#por 256 (conversão para int de 16 bits)
for i in range(0, total):
    array_result[i] = (array_result[i]//256)

#Aplicação da subtração do vetor original (em tons de cinza) com o vetor alterado
#array_result -> armazena os dados para a utilização após a passagem do segundo filtro
#servindo como o que será dividido pelos valores processados e array_gauss_2
array_result = fc.operacao(array_result, array_original, total, 1)
array_gauss_2 = fc.operacao(array_result, array_original, total, 1)
   
# =============================================================================#
#               Bloco da aplicação da lockup table
# =============================================================================#
#look uptable
for i in range(0,total):
    array_gauss_2[i] = (array_gauss_2[i]**0.75)
    
# =============================================================================#
#               Bloco do segundo filtro gaussiano
# =============================================================================#
       
#Complemenata array com extenções para o segundo filtro gaussiano
curva2 = [10000, 5000, 2000, 714, 294, 140, 80, 54, 42, 39, 42, 54, 80, 140, 294, 714, 5000, 2000, 10000 ]
#
for i in range(0,total):
    array_teste[i] = int(array_gauss_2[i]) 
array_completo_2 = fc.completaVetor(array_teste, total)
for i in range(len(array_result)):
        array_analise = array_completo_2[i:i+19]
        pixel = fc.gauss(array_analise,curva2)
        array_gauss_2[i] = pixel

#Clipa da imagem em [50 a 255]
clip = fc.clipImage_gauss(array_gauss_2, total)

#Aplicação da divisão do vetor alterado pelo primeiro filtra com o vetor alterado
#pelo 
array_result = fc.operacao(array_gauss_2, array_result, total, 2)

# =============================================================================#
#               Multiply 128 , add 128 e clip no range de [0 255]
# =============================================================================#
      
#Multiply 128
for i in range(0,total):
    array_result[i] = (array_result[i]*128)
   
#Acumulate
for i in range(0,total):
    array_result[i] = (array_result[i]+128)//100

# Último clip ([0 255])
for i in range(0,total):
    if(array_result[i] > 255):
        array_result[i] = 255
  
# =============================================================================#
#               Final da Normalização
#               Retorno da do array -> matriz -> Imagem
# =============================================================================#
#Volta a imagem para o formato de matriz
image = fc.convToMatriz(col, row, array_result)
#print(image)

#Transforma matriz em imagem novamente        
fc.convToImage(col, row, array_result)

#fechamaneto dos arquivos
image_in.close()
img.close()

# =============================================================================#
#               Armazenamento de informações para o próximo passo
# =============================================================================#
#Array para continuação do processo

#formato da imagem em array
array_segundo = array_result

#Formato da imagem em matriz
normalizada = fc.convToMatriz(col, row, array_result)

# =============================================================================#
#    Inicio da pós-normalização: 
#   Após a normalização da imagem o processo tem continuidade para a obtenção 
#   de uma imagem mais apurada da impressão digital.
# =============================================================================#

# =============================================================================#
#    Bloco de passagem do filtro gaussiano 5x5 após a normalização
# =============================================================================#

#Extende a array da imagem já normalizada para que seja aplicado o filtro
#gaussiano 5x5(também em formato de array)
array_segundo_ext = fc.anexo(array_segundo, 12)

#kernel para gaussiano 5x5
kernel = [1, 4, 7, 4, 1, 4, 16, 26, 16, 4, 7, 26, 41, 26, 7, 1, 4, 7, 4, 1, 4, 16, 26, 16, 4]

#Aplicação do filtro gaussiano 5x5 (em vetor) sobre a array
array_gauss_5x5 = np.zeros(len(array_result))

for i in range(len(array_result)):
    array_analise = array_segundo_ext[i:i+25]
    pixel = fc.gauss_5x5(array_analise,kernel)
    array_gauss_5x5[i] = pixel
        
# =============================================================================#
#    Bloco de passagem do filtro sobel
# =============================================================================#

#Extende array resultante do gauss 5x5 para passagem do filtro sobel
array_sobel_ext_x = fc.anexo(array_gauss_5x5, 8)

#Array da matriz do filtro sobel sobre o exixo X
sobel_x = [-1, 0, 1, -2, 0, 2, -1, 0, 1]
#Array da matriz do filtro sobel sobre o exixo Y
sobel_y = [1, 2, 1, 0, 0, 0, -1, -2, -1]

#Aplicação do filtro sobel no array array_sobel_ext

array_sobel = np.zeros(len(array_result))
array_sobel_x = np.zeros(len(array_result))
array_sobel_y = np.zeros(len(array_result))

#aplicação do filtro sobre em eixo X
for i in range(len(array_result)):
    array_analise = array_sobel_ext_x[i:i+9]
    pixel_x = fc.sobel_filter(array_analise,sobel_x)
    array_sobel_x[i] = pixel_x
    
#Aplicação do filtro em eixo Y
array_sobel_ext_y = fc.anexo(array_sobel_x, 8)   
    
for i in range(len(array_result)):
    array_analise = array_sobel_ext_y[i:i+9]
    pixel_y = fc.sobel_filter(array_analise,sobel_y)
    array_sobel[i] = pixel_y
    
for i in range(len(array_sobel)):
    array_sobel[i] = array_sobel[i]//1000   

# =============================================================================#
#    Gera imagem do array após a passagem do sobel
# =============================================================================#

#Volta a imagem para o formato de matriz
image = fc.convToMatriz(col, row, array_sobel)

#Transforma matriz em imagem novamente        
fc.convToImage2(col, row, array_sobel)

# =============================================================================#
#   Bloco G(x)^2, GxGy e G(y)^2
# =============================================================================#
#OBS: Gamma de x = 4, Gamma de y = 0.5
#Imagem array que esta sendo utiliozada: array_sobel

#Declaração/inicialização de arrays para os casos G(x)^2, GxGy e G(y)^2
#gx = np.zeros(len(array_sobel))
#gxy = np.zeros(len(array_sobel))
#gy = np.zeros(len(array_sobel))
#
##Extensão arrays
#gx_ext = fc.anexo(array_sobel, 12)
#gxy_ext = fc.anexo(array_sobel, 12)
#gy_ext = fc.anexo(array_sobel, 12)
#
##Curva gaussiana com gamma x
#Necessário alterar o valor da curva para o valor do gamma correto(gamma=4)
#curva_x = [1, 4, 7, 4, 1, 4, 16, 26, 16, 4, 7, 26, 41, 26, 7, 1, 4, 7, 4, 1, 4, 16, 26, 16, 4]
#
##Curva gaussiana com gamma y
#Necessário alterar o valor da curva para o valor do gamma correto(gamma=0.5)
#curva_y = [1, 4, 7, 4, 1, 4, 16, 26, 16, 4, 7, 26, 41, 26, 7, 1, 4, 7, 4, 1, 4, 16, 26, 16, 4]
#
#Aplicação das curvas nos arrays
#G(x)^2
#for i in range(len(array_result)):
#   array_analise = gx_ext[i:i+25]
#    pixel_gx = fc.gauss_5x5(array_analise,curva_x)
    #gx[i] = pixel_gx
    
#G(y)^2   
#for i in range(len(array_result)):
#    array_analise = gy_ext[i:i+25]
#    pixel_gy = fc.gauss_5x5(array_analise,curva_y)
#    gy[i] = pixel_gy
    
#Gx,Gy   
#for i in range(len(array_result)):
#    array_analise = gxy_ext[i:i+25]
#    pixel_gx = fc.gauss_5x5(array_analise,curva_x)
#    gxy[i] = pixel_gx
    
#gxy_ext = fc.anexo(gxy, 12)

#for i in range(len(array_result)):
#    array_analise = gxy_ext[i:i+25]
#    pixel_gy = fc.gauss_5x5(array_analise,curva_y)
#    gxy[i] = pixel_gy

# =============================================================================#
#   Aplicação gauss 5x5 (com gamma = 1) em G(x)^2, GxGy e G(y)^2
# =============================================================================#

#Extende a array do passo anterior
#array_gx_ext = fc.anexo(gy, 12)
#array_gxy_ext = fc.anexo(gxy, 12)
#array_gy_ext = fc.anexo(gy, 12)

#kernel para gaussiano 5x5
#kernel = [1, 4, 7, 4, 1, 4, 16, 26, 16, 4, 7, 26, 41, 26, 7, 1, 4, 7, 4, 1, 4, 16, 26, 16, 4]

#Aplicação do filtro gaussiano 5x5 (em vetor) sobre os vetores
#array_gauss_5x5 = np.zeros(len(array_result))

#Gx
#for i in range(len(array_result)):
#    array_analise = array_gx_ext[i:i+25]
#    pixel = fc.gauss_5x5(array_analise,kernel)
#    gx[i] = pixel
    
#Gy
#for i in range(len(array_result)):
#    array_analise = array_gxy_ext[i:i+25]
#    pixel = fc.gauss_5x5(array_analise,kernel)
#    gx[i] = pixel


#Gxy
#for i in range(len(array_result)):
#    array_analise = array_gy_ext[i:i+25]
#    pixel = fc.gauss_5x5(array_analise,kernel)
#    gx[i] = pixel

# =============================================================================#
#   
# =============================================================================#



