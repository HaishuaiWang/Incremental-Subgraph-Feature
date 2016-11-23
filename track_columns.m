function [ location_index ] = track_columns( pointer, len, location_index, top_k_location )
%TRACK_COLUMNS Summary of this function goes here
%   Detailed explanation goes here

%temp = pointer - choosed_column - choosed_column;
last_top_k_location = location_index;
for i = 1:length(top_k_location)
        if top_k_location(i) <= len
            location_index(i) = pointer - 1 + top_k_location(i);
        else
            temp = top_k_location(i) - len;
            location_index(i) = last_top_k_location(temp);
        end
end
%location_index = location_x

end

