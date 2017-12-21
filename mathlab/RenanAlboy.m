% Renan aleane Alboy

%Parte 1

%Atribui a I a imagem que será utilizada. O nome sem extensão da imagem é
%atribuidsa a uma variável FILENAME.
FILENAME = 'forest';
I = imread([FILENAME,'.tif']);

%Mostra as informações referentes a imagem I
%whos I;

% Utiliza a fução histeq para realizar a equalização da imagem e armazena o
% resultado em I2
I2 = histeq(I);

%Faz o plot da imagem composta em um ajanela. Esta imagem é composta por uma 
%versão inicial da foto acompanhada de seu histograma, logo abaixo, a foto 
%$equalizada e seu histograffo. 
figure
subplot(2,2,1), imshow(I)
subplot(2,2,2), imhist(I)
subplot(2,2,3), imshow(I2)
subplot(2,2,4), imhist(I2)
%%
%Parte 2

%Foi feita por etapas seguindo o script do arroz

%% 
I = imread('coins.png');
imshow(I)
%%
background = imopen(I,strel('disk',30));
%% 
figure
surf(double(background(1:8:end,1:8:end))),zlim([0 255]);
set(gca,'ydir','reverse');
%% 
I2 = I - background;
imshow(I2)
%% 
I3 = imadjust(I2);
imshow(I3);
%% 
level = graythresh(I3)
bw = im2bw(I3,level);
bw = bwareaopen(bw, 50);
imshow(bw)
%%
cc = bwconncomp(bw)
cc.NumObjects
%% 
% View the rice grain that is labeled 50 in the image. 
coin = false(size(bw));
grain(cc.PixelIdxList{30}) = true;
imshow(grain);
%% 
labeled = labelmatrix(cc);
RGB_label = label2rgb(labeled, @spring, 'c', 'shuffle');
imshow(RGB_label)  
%% 
coindata = regionprops(cc, 'basic')
%%
coindata(50).Area
%% 
coin_areas = [coindata.Area];
%%
[max_area, idx] = max(coin_areas) 
coin = false(size(bw));
coin(cc.PixelIdxList{idx}) = true;
imshow(grain);
%%
figure
histogram(coin_areas)
title('Área da moeda');