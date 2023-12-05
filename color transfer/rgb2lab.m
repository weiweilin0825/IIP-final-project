function lab = rgb2lab(image)
LMS_matrix = [0.3811 0.5783 0.0402;
    0.1967 0.7244 0.0782;
    0.0241 0.1288 0.8444];
LMS = zeros(size(image));
for x = 1:size(image,1)
    for y = 1:size(image,2)
        LMS(x,y,:) = LMS_matrix*reshape(image(x,y,:),[3 1]);
    end
end
LMS(find(LMS==0)) = 1;
LMS = log10(LMS);

lab_matrix_1 = [1/sqrt(3) 0 0;
     0 1/sqrt(6) 0;
      0 0 1/sqrt(2)];
lab_matrix_2 = [1 1 1;
    1 1 -2;
    1 -1 0];
lab = zeros(size(image));

for x = 1:size(image,1)
    for y = 1:size(image,2)
        lab(x,y,:) = lab_matrix_1*lab_matrix_2*reshape(LMS(x,y,:),[3 1]);
    end
end

end