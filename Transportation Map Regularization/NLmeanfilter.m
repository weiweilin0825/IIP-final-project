function [output] = NLmeanfilter(input, kernel, neighbor, search, x, y, ch, h, m, n);

x = x + neighbor;
y = y + neighbor;

w1 = input(x - neighbor : x + neighbor, y - neighbor : y + neighbor, ch);

rmin = max(x - search, neighbor + 1);
rmax = min(x + search, m + neighbor);
smin = max(y - search, neighbor + 1);
smax = min(y + search, n + neighbor);

%Compute local degree of smoothing
%{
patch = imcrop(input, [rmin, smin, (rmax - rmin + 1), (smax - smin + 1)]);
patch = input;
patchSq = patch.^2;
edist = sqrt(sum(patchSq,3));
patchSigma = sqrt(var(edist(:)));
h = 1.5*patchSigma;
%}

NL = 0;
cij = 0;

for r = rmin : rmax
    for s = smin : smax
        w2 = input(r - neighbor : r + neighbor, s - neighbor : s + neighbor, ch);
        d2 = sum(sum(kernel .* (w1 - w2) .* (w1 - w2)));
        wij = exp(-d2 / (h ^ 2));
        cij = cij + wij;
        NL = NL + (wij * input(r, s, ch));
    end
end

output = NL / cij;

end

