function [ alpha ] = get_alpha(featureSet,y,b,para_C)
%GET_ALPHA Summary of this function goes here
%   Detailed explanation goes here

[no_row, no_column] = size(featureSet);
y_row = length(y);
C = para_C * ones(no_row,1);
bb = zeros(1,1);
lb = zeros(no_row, 1);
f = b';
H = [];
for i = 1:no_row
    for j = 1:y_row
        H(i,j) = y(i) * y(j) * featureSet(i,:) * featureSet(j,:)';
    end
end

alpha = quadprog(H, f, [], [], y, bb, lb, C);

end
