function [ x_top_k, top_k_location ] = find_top_k(featureSet, y, alpha, top_k)
%FIND_TOP_K Summary of this function goes here
%   Detailed explanation goes here

[no_row, no_column] = size(featureSet);
w = zeros(no_column, 1);

for i = 1:no_column
    for j = 1:no_row
        w(i) = w(i) + alpha(j) * y(j) * featureSet(j,i);
    end
end

S_w = sort(w,'descend');
S_w(1:top_k);
top_k_location = zeros(1,top_k);
for index = 1:top_k
    location = find(w == S_w(index));
    if length(location) ~= 1
        for index_location = 1:length(location)
            if isempty(find(top_k_location == location(index_location)))
                top_k_location(index) = location(index_location);
                break;
            end
        end
    else
        top_k_location(index) = location;
    end
end
%l = [];

x_top_k = featureSet(:,top_k_location);
% temp = pointer - choosed_column - choosed_column;
% for i = 1:length(top_k_location)
%         if top_k_location(i) <= choosed_column
%             location_x(i) = temp + top_k_location(i);
%         else
%             tl = top_k_location(i) - len;
%             location_x(i) = l(tl);
%         end
% end
% l = location_x
end

