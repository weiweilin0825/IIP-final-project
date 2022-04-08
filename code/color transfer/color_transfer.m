%% convert
% clc;clear all;
source = imread('D:\清大\影像處理\term_project\fotojet-1606462750.jpg');
target = imread('D:\清大\影像處理\term_project\symmetric.tif');
source = double(source);
target = double(target);
lab_s = rgb2lab(source); lab_t = rgb2lab(target);
%% process
swatch1_s = lab_s(1:150,350:450,:);%sky
ls_1 = swatch1_s(:,:,1); ls_1 = ls_1(:);
as_1 = swatch1_s(:,:,2); as_1 = as_1(:);
bs_1 = swatch1_s(:,:,3); bs_1 = bs_1(:);

swatch2_s = lab_s(200:400,150:300,:);%roof
ls_2 = swatch2_s(:,:,1); ls_2 = ls_2(:);
as_2 = swatch2_s(:,:,2); as_2 = as_2(:);
bs_2 = swatch2_s(:,:,3); bs_2 = bs_2(:);

swatch3_s = lab_s(400:600,400:602,:);%floor
ls_3 = swatch3_s(:,:,1); ls_3 = ls_3(:);
as_3 = swatch3_s(:,:,2); as_3 = as_3(:);
bs_3 = swatch3_s(:,:,3); bs_3 = bs_3(:);

swatch1_t = lab_t(1:400,370:562,:);%sky
lt_1 = swatch1_t(:,:,1); lt_1 = lt_1(:);
at_1 = swatch1_t(:,:,2); at_1 = at_1(:);
bt_1 = swatch1_t(:,:,3); bt_1 = bt_1(:);

swatch2_t = lab_t(200:600,150:250,:);%tower
lt_2 = swatch2_t(:,:,1); lt_2 = lt_2(:);
at_2 = swatch2_t(:,:,2); at_2 = at_2(:);
bt_2 = swatch2_t(:,:,3); bt_2 = bt_2(:);

swatch3_t = lab_t(680:749,1:400,:);%grass
lt_3 = swatch3_t(:,:,1); lt_3 = lt_3(:);
at_3 = swatch3_t(:,:,2); at_3 = at_3(:);
bt_3 = swatch3_t(:,:,3); bt_3 = bt_3(:);

swatch4_t = lab_t(540:570,465:550,:);%floor
lt_4 = swatch4_t(:,:,1); lt_4 = lt_4(:);
at_4 = swatch4_t(:,:,2); at_4 = at_4(:);
bt_4 = swatch4_t(:,:,3); bt_4 = bt_4(:);

swatch5_t = lab_t(474:480,202:205,:);%tower2
lt_5 = swatch5_t(:,:,1); lt_5 = lt_5(:);
at_5 = swatch5_t(:,:,2); at_5 = at_5(:);
bt_5 = swatch5_t(:,:,3); bt_5 = bt_5(:);

mean_s = [mean(ls_1) mean(as_1) mean(bs_1);
    mean(ls_2) mean(as_2) mean(bs_2);
    mean(ls_3) mean(as_3) mean(bs_3)];
mean_t = [mean(lt_1) mean(at_1) mean(bt_1);
    mean(lt_2) mean(at_2) mean(bt_2);
    mean(lt_3) mean(at_3) mean(bt_3);
    mean(lt_4) mean(at_4) mean(bt_4);
    mean(lt_5) mean(at_5) mean(bt_5)];
std_s = [std(ls_1) std(as_1) std(bs_1);
    std(ls_2) std(as_2) std(bs_2);
    std(ls_3) std(as_3) std(bs_3)];
std_t = [std(lt_1) std(at_1) std(bt_1);
    std(lt_2) std(at_2) std(bt_2);
    std(lt_3) std(at_3) std(bt_3);
    std(lt_4) std(at_4) std(bt_4);
    std(lt_5) std(at_5) std(bt_5)];
mask = zeros([size(target,1),size(target,2)]);
for x = 1:size(target,1)
    for y = 1:size(target,2)
        D1 = sqrt((lab_t(x,y,1) - mean_t(1,1))^2+(lab_t(x,y,2) - mean_t(1,2))^2+(lab_t(x,y,3) - mean_t(1,3))^2);
        D2 = sqrt((lab_t(x,y,1) - mean_t(2,1))^2+(lab_t(x,y,2) - mean_t(2,2))^2+(lab_t(x,y,3) - mean_t(2,3))^2);
        D3 = sqrt((lab_t(x,y,1) - mean_t(3,1))^2+(lab_t(x,y,2) - mean_t(3,2))^2+(lab_t(x,y,3) - mean_t(3,3))^2);
        D4 = sqrt((lab_t(x,y,1) - mean_t(4,1))^2+(lab_t(x,y,2) - mean_t(4,2))^2+(lab_t(x,y,3) - mean_t(4,3))^2);
        D5 = sqrt((lab_t(x,y,1) - mean_t(5,1))^2+(lab_t(x,y,2) - mean_t(5,2))^2+(lab_t(x,y,3) - mean_t(5,3))^2);
        if min([D1 D2 D3 D4 D5]) == D1
            mask(x,y) = 0;
            lab_t(x,y,1) = (lab_t(x,y,1)-mean_t(1,1))*(std_s(1,1)/std_t(1,1))+mean_s(1,1);
            lab_t(x,y,2) = (lab_t(x,y,2)-mean_t(1,2))*(std_s(1,2)/std_t(1,2))+mean_s(1,2);
            lab_t(x,y,3) = (lab_t(x,y,3)-mean_t(1,3))*(std_s(1,3)/std_t(1,3))+mean_s(1,3);
        elseif min([D1 D2 D3 D4 D5]) == D2
            mask(x,y) = 0.3;
            lab_t(x,y,1) = (lab_t(x,y,1)-mean_t(2,1))*(std_s(2,1)/std_t(2,1))+mean_s(2,1);
            lab_t(x,y,2) = (lab_t(x,y,2)-mean_t(2,2))*(std_s(2,2)/std_t(2,2))+mean_s(2,2);
            lab_t(x,y,3) = (lab_t(x,y,3)-mean_t(2,3))*(std_s(2,3)/std_t(2,3))+mean_s(2,3);
        elseif min([D1 D2 D3 D4 D5]) == D3
            mask(x,y) = 0.6;
            %lab_t(x,y,1) = (lab_t(x,y,1)-mean_t(3,1))*(std_s(3,1)/std_t(3,1))+mean_s(3,1);
            %lab_t(x,y,2) = (lab_t(x,y,2)-mean_t(3,2))*(std_s(3,2)/std_t(3,2))+mean_s(3,2);
            %lab_t(x,y,3) = (lab_t(x,y,3)-mean_t(3,3))*(std_s(3,3)/std_t(3,3))+mean_s(3,3);
        elseif min([D1 D2 D3 D4 D5]) == D4
            mask(x,y) = 1;
            lab_t(x,y,1) = (lab_t(x,y,1)-mean_t(4,1))*(std_s(3,1)/std_t(4,1))+mean_s(3,1);
            lab_t(x,y,2) = (lab_t(x,y,2)-mean_t(4,2))*(std_s(3,2)/std_t(4,2))+mean_s(3,2);
            lab_t(x,y,3) = (lab_t(x,y,3)-mean_t(4,3))*(std_s(3,3)/std_t(4,3))+mean_s(3,3);
        elseif min([D1 D2 D3 D4 D5]) == D5
            mask(x,y) = 0.3;
            lab_t(x,y,1) = (lab_t(x,y,1)-mean_t(2,1))*(std_s(2,1)/std_t(2,1))+mean_s(2,1);
            lab_t(x,y,2) = (lab_t(x,y,2)-mean_t(2,2))*(std_s(2,2)/std_t(2,2))+mean_s(2,2);
            lab_t(x,y,3) = (lab_t(x,y,3)-mean_t(2,3))*(std_s(2,3)/std_t(2,3))+mean_s(2,3);
        end
    end
end

%% convert back
result = lab2rgb(lab_t);
result = uint8(result);
figure,imshow(result);
imwrite(result,'result.tif');