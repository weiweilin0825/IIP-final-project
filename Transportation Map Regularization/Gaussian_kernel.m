function [output] = Gaussian_kernel(neighbor_size, std_gaussian)

kernel_sum = 0;
output = zeros(neighbor_size, neighbor_size);
half_neighbor_size = floor(neighbor_size / 2); 

for x = 1 : neighbor_size
    for y = 1 : neighbor_size
        horizon_dis = x - half_neighbor_size - 1;
        vertical_dis = y - half_neighbor_size -1;
        output(x, y) = exp((horizon_dis ^ 2 + vertical_dis ^ 2) / (-2 * (std_gaussian ^ 2)));
        kernel_sum = kernel_sum + output(x, y);
    end
end

output = output ./ half_neighbor_size;
output = output / kernel_sum;

end

