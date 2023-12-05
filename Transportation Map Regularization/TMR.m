function [output] = TMR(transfer_image, original_image, neighbor_size, search_size, std);

[M, N, C] = size(original_image);

original_image = rgb2lab(original_image);
transfer_image = rgb2lab(transfer_image);

half_neighbor = floor(neighbor_size / 2);
half_search = floor(search_size / 2);

gkernel = Gaussian_kernel(neighbor_size, std);

padded_original = padarray(original_image, [half_neighbor, half_neighbor], 'replicate', 'both');
padded_transfer = padarray(transfer_image, [half_neighbor, half_neighbor], 'replicate', 'both');

output = zeros(M, N, C);

%Compute global degree of smoothing of original image
patch1 = original_image;
patchSq1 = patch1.^2;
edist1 = sqrt(sum(patchSq1,3));
patchSigma1 = sqrt(var(edist1(:)));
h1 = 1.5*patchSigma1;

%Compute global degree of smoothing of transfer image
patch2 = transfer_image;
patchSq2 = patch2.^2;
edist2 = sqrt(sum(patchSq2,3));
patchSigma2 = sqrt(var(edist2(:)));
h2 = 1.5*patchSigma2;


for ch = 1 : C 
    for x = 1 : M
        for y = 1 : N
            %output(x, y, ch) = NLmeanfilter(padded_transfer, gkernel, half_neighbor, half_search, x, y, ch, h, M, N);  
            old_m = transfer_image(x, y, ch) - original_image(x, y, ch);
            filtered_original = NLmeanfilter(padded_original, gkernel, half_neighbor, half_search, x, y, ch, h1, M, N);
            filtered_transfer = NLmeanfilter(padded_transfer, gkernel, half_neighbor, half_search, x, y, ch, h2, M, N);
            new_m = filtered_transfer - filtered_original;
            while abs(new_m - old_m) >= 1
                old_m = new_m;
                filtered_original = NLmeanfilter(padded_original, gkernel, half_neighbor, half_search, x, y, ch, h1, M, N);
                filtered_transfer = NLmeanfilter(padded_transfer, gkernel, half_neighbor, half_search, x, y, ch, h2, M, N);
                new_m = filtered_transfer - filtered_original;
            end
            output(x, y, ch) = new_m + original_image(x, y, ch);    
        end
    end
end

output = lab2rgb(output, 'OutputType', 'uint8');
%output = uint8(output);

end

