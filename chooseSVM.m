function [ node_accuracy ] = nodeClassify( x,y, alg5_path, K )
%NODECLASSIFY Summary of this function goes here
%   Detailed explanation goes here

[no_row,no_column]=size(x);
fid = fopen(alg5_path, 'w+');
variance = 0;
[train_index] = crossvalind('Kfold',no_row,K);
temp_acc = 0;
bestID = 0;

for i=1:K
    Train_x=x(train_index~=i,:);
    Train_y=y(train_index~=i);
    
    Test_x=x(train_index==i,:);
    Test_y=y(train_index==i);
    %SVMStruct = svmtrain(Train_x,Train_y, 'kernel_function', 'linear', 'boxconstraint', 100);
    SVMStruct = svmtrain(Train_x,Train_y)
    %bestSVM(i) = SVMStruct;
    cp=svmclassify(SVMStruct,Test_x);
    Test_y;
    cp';
    if ~isempty(cp')
        err_rate(i) = sum(Test_y~= cp')/length(Test_y); % mis-classification rate
        acc_rate(i) = 1 - err_rate(i);
    end
    if acc_rate(i) > temp_acc
        temp_acc = acc_rate(i)
        bestID = i
    end
end

% BEST SVM ----------
Train_x=x(train_index~=bestID,:);
Train_y=y(train_index~=bestID);
bestSVM = svmtrain(Train_x,Train_y)

cp = svmclassify(bestSVM, Test_x);
%-----------------

node_accuracy = 1-sum(err_rate)/length(err_rate)
for i = 1:length(acc_rate)
    variance = variance + (acc_rate(i) - node_accuracy)^2;
end
variance = variance / (length(acc_rate)-1)
fprintf(fid, '%g\t', node_accuracy);
fprintf(fid, '%g\r\n', variance);
end

