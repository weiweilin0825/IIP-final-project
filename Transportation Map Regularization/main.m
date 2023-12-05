clear;
clc;
close all;

original_image = imread('ori.tiff');
transfer_image = imread('final_result.tiff');
%transfer_image = rgb2lab(transfer_image);

[M, N, C] = size(original_image);

neighbor_size = input('Enter the neighbor kernel size for non local mean filter : ');
search_size = input('Enter the search kernel size for non local mean filter : ');
%std = double(neighbor_size/3);
std = input('Enter the gaussian kernel variance for non local mean filter : ');

recover = TMR(transfer_image, original_image, neighbor_size, search_size, std);

imwrite(recover,'recover_lab_1.jpg');

subplot(3, 1, 1); imshow(original_image, []);
subplot(3, 1, 2); imshow(transfer_image, []);
subplot(3, 1, 3); imshow(recover, []);
%{

roi = [210,24,52,41];
patch = imcrop(transfer_image,roi);
patchSq = patch.^2;
edist = sqrt(sum(patchSq,3));
%}