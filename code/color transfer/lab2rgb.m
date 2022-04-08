function rgb = lab2rgb(image)
LMS_matrix_1 = [1 1 1;
    1 1 -1;
    1 -2 0];
LMS_matrix_2 = [sqrt(3)/3 0 0;
    0 sqrt(6)/6 0;
    0 0 sqrt(2)/2];
LMS_matrix = LMS_matrix_1*LMS_matrix_2;
LMS = zeros(size(image));

for x = 1:size(image,1)
    for y = 1:size(image,2)
        LMS(x,y,:) = LMS_matrix*reshape(image(x,y,:),[3 1]);
    end
end

RGB_matrix = [4.4679 -3.5873 0.1193;
    -1.2186 2.3809 -0.1624;
    0.0497 -0.2439 1.2045];

for x = 1:size(image,1)
    for y = 1:size(image,2)
        for c = 1:3
            LMS(x,y,c) = 10^LMS(x,y,c);
        end
    end
end
rgb = zeros(size(image));

for x = 1:size(image,1)
    for y = 1:size(image,2)
        rgb(x,y,:) = RGB_matrix*reshape(LMS(x,y,:),[3 1]);
    end
end

end