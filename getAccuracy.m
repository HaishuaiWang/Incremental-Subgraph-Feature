function [ accuracy, Precision, Recall, F_score, variance ] = getAccuracy( featureSet, y, K )
%GETACCURACY Summary of this function goes here
%   Detailed explanation goes here

[nof,nod]=size(featureSet);
variance = 0;
positive = 0;
negative = 0;
true_positive = 0;
false_positive = 0;
true_negative = 0;
false_negative = 0;
[train_index] = crossvalind('Kfold',nof,K);

for i=1:K
    Train_x = featureSet(train_index~=i,:);
    Train_y = y(train_index~=i);
    
    Test_x = featureSet(train_index==i,:);
    Test_y = y(train_index==i);
    SVMStruct = svmtrain(Train_x,Train_y);
    cp = svmclassify(SVMStruct,Test_x);
    if ~isempty(cp')
        err_rate(i) = sum(Test_y ~= cp')/length(Test_y); % mis-classification rate
        acc_rate(i) = 1 - err_rate(i);
        for j = 1:length(Test_y)
            if Test_y(j) == 1 
                positive = positive + 1;
                if Test_y(j) == cp(j)
                    true_positive = true_positive + 1;
                else
                    false_positive = false_positive + 1;
                end
            elseif Test_y(j) == -1 
                negative = negative + 1;
                if Test_y(j) == cp(j)
                    true_negative = true_negative + 1;
                else
                    false_negative = false_negative + 1;
                end
            end
        end
    end
end
Precision = true_positive / (true_positive + false_positive)
Recall = true_positive / (true_positive + false_negative)
F_score = 2 * Precision * Recall / (Precision + Recall)
accuracy = 1-sum(err_rate)/length(err_rate)
for i = 1:length(acc_rate)
    variance = variance + (acc_rate(i) - accuracy)^2;
end
variance = variance / (length(acc_rate)-1)
end

