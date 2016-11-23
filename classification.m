function state = classification( x_dat, y_dat, nodes_dat, top_k, para_C, len, K )
%CLASSIFICATION Summary of this function goes here
%   Detailed explanation goes here

%% Parameters;
x = load(x_dat);
y = load(y_dat);
nodes = load(nodes_dat);
pointer = 1;
b = [];

for i = 1:length(y)
    b(i) = -1;
end

%% Streaming subgraph feature selection method, calculate alpha first;
tic
ssf_path = 'SSF.dat';
ssf(x, y, b, top_k, para_C, len, pointer, ssf_path, K);  
toc

%% Calculate alpha later;
%alg2_path = 'algorithm_2.dat';
%algorithm2(x, y, b, top_k, para_C, len, pointer, alg2_path, K);

%% Long Pattern. Add long path as feature;
%longPattern_path = 'longPattern.dat';
%longPattern(x, y, b, top_k, para_C, len, pointer, longPattern_path, K);

%% Loads all features into memory at once and then selects top_k columns in each iteration;
tic
osf_path = 'OSF.dat';
osf(x, y, b, top_k, para_C, len, osf_path, K);
toc

%% Randomly selects meta subgraphs (nodes) as features;
msf_path = 'MSF.dat';
msf(nodes, y, msf_path ,K);

%% Randomly selects B features;
rsf_path = 'RSF.dat';
rsf(x, y, len, rsf_path, K);

%% End
state = '============= DONE! =============';


end

