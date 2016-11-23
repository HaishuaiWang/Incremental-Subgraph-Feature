function state_2 = allFeatures( x, y, b, top_k, para_C, len, alg2_path, K )

[x_row, x_column] = size(x);

%location_index = [];
%x_top_k = [];
alpha = 1/para_C*ones(x_row,1);
len = floor(len * x_column);
top_k = floor(top_k * len);
fid = fopen(alg2_path, 'w+');
unionSet = [];
temp = zeros(x_row,1);

while abs(alpha - temp) < 0.1
    [featureSet,top_k_loc] = find_top_k(x, y, alpha, top_k); % calculate score(W) and select top_k columns
    unionSet = [unionSet, featureSet];
    temp = alpha;
    [accuracy,Precision, Recall, F_score, variance] = getAccuracy(featureSet, y, K);    
    alpha = get_alpha(unionSet, y, b, para_C); %calculate \alpha
    fprintf(fid, '%g\t', accuracy);
    fprintf(fid, '%g\t', Precision);
    fprintf(fid, '%g\t', Recall);
    fprintf(fid, '%g\t', F_score);
    fprintf(fid, '%g\r\n', variance);
end

state_2 = '=================OSF DONE!================='

end
