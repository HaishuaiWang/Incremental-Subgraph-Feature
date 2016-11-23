clc;
clear;

%% parameters

% feature set file
% label set file
% top_k (percent of length)
% C
% length: column number, how many columns chose each iteration
% K-folder

classification('_trainingFeature.dat', '_trainingLable.dat', '_trainingFeatureAllNodes.dat', 0.8, 100 , 0.3, 10)
