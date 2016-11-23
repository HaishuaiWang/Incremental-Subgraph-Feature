function [ new_x ] = next_choosed_column( x, start, len)
%NEXT_CHOOSED_COLUMN Summary of this function goes here
%   Detailed explanation goes here
count=1;
for i = start:(len+start)
    new_x(:,count) = x(:,i); 
    count=count+1;
end

end

