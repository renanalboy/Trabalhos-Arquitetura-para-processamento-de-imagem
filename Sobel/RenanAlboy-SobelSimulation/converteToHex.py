import sys
import os
from PIL import Image
from numpy import *

#------ Funções ------#

#Converte a imagem passadda como parametro para tons de cinza
#Também já salva a versão PPM de da imagem em tons de cinza
def convToPpm(imagem):
    img_colorida = Image.open(imagem)
    img_cinza = img_colorida.convert('L')
    img_cinza.save('teste_cinza.jpg')
    img_cinza.save('teste_cinza.ppm')
    img_cinza.save('teste_cinza.pgm')



#Conversão da imagem pgm para hex, já sendo criado um arquivo com o formato de vetor
#para ser utilizado como entrada no testbench
def pgmToHexArray(file_in, file_out):
    im = Image.open(file_in)
    hex_file = ""
    for y in range(im.height):
        for x in range(im.width):
            pxl = im.getpixel((x, y))
            #print("pxl", pxl )
            pxl_hex = '{0:X}'.format(pxl)
            pxl_hex = "00" + pxl_hex
            pxl_hex = pxl_hex[-2:]
            if x == (im.width - 1):
                if y == (im.height - 1):
                    hex_file = hex_file + pxl_hex
                else:
                    hex_file = hex_file + pxl_hex + "\n"
            else:
                hex_file = hex_file + pxl_hex + "\n"
    f = open(file_out,'w+')
    f.write(hex_file)
    f.close()

#---------------------------------------------#

print('Convertendo a imagem para tons de cinza ...')
convToPpm('teste.jpg')
print('Conversão concluida.')
arq_in = 'teste_cinza.pgm'
arq_out = 'resultado.hex'
print('Gerando arquivo hexadecimal da imagem ...')
pgmToHexArray(arq_in, arq_out)
print('Arquivo gerado.')

