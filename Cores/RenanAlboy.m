%Primeiro teste:
%Compara��o entre diagrama rgb e cmyk. Sendo realizado sobre as imagens a soma e adivis�o.
%Devido ao tamanha das imagens n�o serem iguais� poss�vel notar regioes que
%n�o se encaixam, causando assim regi�es com cores diferentes.

I = imread('cores4.jpg');
I2 = imread('cores3.jpg');
K = imdivide(imadd(I,I2), 2); 
K2 = imlincomb(.5,I,.5,I2); 

%Plot das imagens
figure
subplot(2,2,1), imshow(I)
subplot(2,2,2), imshow(I2)
subplot(2,2,3), imshow(K)
subplot(2,2,4), imshow(K2)

%%
%Opera��o de soma. Devido a imagem n�o ser "pura", pois possui bordas, ao
%somar sobra resquicios de seus formatos.
K3 = imadd(I,I2);
figure
imshow(K3);

%%
%Opera��o de divis�o
K4 = imdivide(I,I2);
figure
imshow(K4);

%%
%Opera��o de subtra��o
K5 = imsubtract(I2,I);
figure
imshow(K5);

%%
%Opera��o de multiplica��o sobre a imagem I(cores3)
K6 = immultiply(I,1);
K7 = immultiply(I,0.75);
K8 = immultiply(I,0.5);
K9 = immultiply(I,0.25);

%Plot das imagens
figure
subplot(2,2,1), imshow(K6)
subplot(2,2,2), imshow(K7)
subplot(2,2,3), imshow(K8)
subplot(2,2,4), imshow(K9)


%%
%Segundo teste: Isolando canais de cores
%Utilizando o diagrama das cores cmyk
figure
RGB = imread('cores3.jpg');
subplot(2,2,1), imshow(RGB)
subplot(2,2,2), imshow(RGB(:,:,1))
subplot(2,2,3), imshow(RGB(:,:,2))
subplot(2,2,4), imshow(RGB(:,:,3))

% HSV

figure
HSV = rgb2hsv(RGB);
subplot(2,2,1), imshow(rgb2gray(RGB))
subplot(2,2,2), imshow(HSV(:,:,1))
subplot(2,2,3), imshow(HSV(:,:,2))
subplot(2,2,4), imshow(HSV(:,:,3))

%%
%Terceiro teste: Isolando canais de cores
%Utilizando o diagrama das cores rgb

RGB = imread('cores4.jpg');
figure
subplot(2,2,1), imshow(RGB)
subplot(2,2,2), imshow(RGB(:,:,1))
subplot(2,2,3), imshow(RGB(:,:,2))
subplot(2,2,4), imshow(RGB(:,:,3))

% HSV

figure
HSV = rgb2hsv(RGB);
subplot(2,2,1), imshow(rgb2gray(RGB))
subplot(2,2,2), imshow(HSV(:,:,1))
subplot(2,2,3), imshow(HSV(:,:,2))
subplot(2,2,4), imshow(HSV(:,:,3))
