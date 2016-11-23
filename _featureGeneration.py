#/usr/bin/env python
import sys, os, string
import subprocess
import random
#--------------------------------------------------------------------------------------------------------------------

def usage():
	print u'''
	help: _featureGeneration.py <upperbound | lowerbound | lable_threshold | t | support>
	
	[upperbound]: Option, select cascades whose length is more than upperbound
	[lowerbound]: Option, select cascades whose length is less than lowerbound
	[lable_threshold]: Option, classification bound, the lable of cascade whose length is more than lable_threshold is "1", otherwise is "-1"
	[t]: Option, select part cascade whose time delay is less than t in each cascade
	[support]: Option, support threshold for sequetial pattern mining

	Example: python _featureGeneration.py 35 15 36 5 12
	'''

#--------------------------------------------------------------------------------------------------------------------
def global_variance():
	global dic
	global upperbound
	global lowerbound
	global lable_threshold
	global t
	global support
	global trainingFile
	global testingFile
	global testingSet
	global trainingSet
	global trainingLable
	global testingLable
	global trainingFeature
	global testingFeature
	global _trainingSet
	global _testingSet
	global _trainingLable
	global _testingLable
	global patternFile
	global _trainingFeature
	global _testingFeature
	global nodesFile
	global _trainingFeatureAllNodes
	global _testingFeatureAllNodes
	dic = os.getcwd()
	upperbound = int(sys.argv[1])
	lowerbound = int(sys.argv[2])
	lable_threshold = int(sys.argv[3])
	t = float(sys.argv[4])
	support = int(sys.argv[5])
	trainingFile = dic + "/" + sys.argv[1] + "_" + sys.argv[2] + "_training.dat"
	testingFile = dic + "/" + sys.argv[1] + "_" + sys.argv[2] + "_testing.dat"
	testingSet = dic + "/" + sys.argv[1] + "_" + sys.argv[2] + "_testingSet.dat"
	trainingSet = dic + "/" + sys.argv[1] + "_" + sys.argv[2] + "_trainingSet.dat"
	trainingLable = dic + "/training_lable.dat"
	testingLable = dic + "/testing_lable.dat"
	trainingFeature = dic + "/trainingFeature.dat"
	testingFeature = dic + "/testingFeature.dat"
	_trainingSet = dic + "/_traingSet.dat"
	_testingSet = dic + "/_testingSet.dat"
	_trainingLable = dic + "/_trainingLable.dat"
	_testingLable = dic + "/_testingLable.dat"
	patternFile = dic + "/patterns.dat"
	_trainingFeature = dic + "/_trainingFeature.dat"
	_testingFeature = dic + "/_testingFeature.dat"
	nodesFile = dic + "/nodes.dat"
	_trainingFeatureAllNodes = dic + "/_trainingFeatureAllNodes.dat"
	_testingFeatureAllNodes = dic + "/_testingFeatureAllNodes.dat"
	
def init():
	fr = open(dic + '/exampleData.dat')       
	fw = open(dic + '/original_no_time.dat','w')
	l1 = fr.readlines()  

	for x in range(0, len(l1)):
		l2 = l1[x].index(';')
		remaindstring = l1[x][l2+1:len(l1[x])]
		splitstring = remaindstring.split(',')
		print len(splitstring)
		print '-------'
		fw.writelines(l1[x][0:l2])
		if len(splitstring) > 2:
			for xx in range(0, len(splitstring)-2, 2):
				newstring = splitstring[xx]
				print newstring
				fw.writelines(" "+newstring)
		else:
			print splitstring[0]
		fw.writelines(" ")
		fw.writelines(splitstring[len(splitstring)-2]+'\n')
	fr.close()
	fw.close()

#--------------------------------------------------------------------------------------------------------------------

def count():
	fr = open(dic + '/original_no_time.dat')       
	l1 = fr.readlines()  
	fw = open(dic + '/count.dat','w')

	for x in range(0, len(l1)):
		splintedstring = l1[x].split(" ")
		count = len(splintedstring)
		fw.writelines(str(count)+'\n')

	fr.close()

#--------------------------------------------------------------------------------------------------------------------

def selectCascades():
	f_read_count = open(dic + "/count.dat")
	f_read_original = open(dic + "/exampleData.dat")
	f_write_cascade = open(trainingFile, 'w')
	f_write_testing = open(testingFile, 'w')
	list_upper = []
	list_lower = []
	random_lower = []
	count = 0
	#randomNo = []

	count_lines = f_read_count.readlines()
	original_lines = f_read_original.readlines()

	for count_lines_index in range(0, len(count_lines)):
		if int(count_lines[count_lines_index]) > upperbound:
			count = count + 1
			list_upper.append(count_lines_index)
		elif int(count_lines[count_lines_index]) < lowerbound:
			list_lower.append(count_lines_index)
	randomNo = random.sample(range(len(list_lower)),count)
	print count
	for randomNo_list in range(0, len(randomNo)):
		print randomNo[randomNo_list],
		print list_lower[randomNo[randomNo_list]]
		random_lower.append(list_lower[randomNo[randomNo_list]])

	for list_index in range(0, count):
		f_write_cascade.writelines(original_lines[list_upper[list_index]])
		f_write_cascade.writelines(original_lines[random_lower[list_index]])
		f_write_testing.writelines(original_lines[list_upper[list_index]])
		print original_lines[list_upper[list_index]]
		print original_lines[random_lower[list_index]]
	
	for lower_index in range(0, len(list_lower)):	
		f_write_testing.writelines(original_lines[list_lower[lower_index]])
	f_read_count.close()
	f_read_original.close()
	f_write_cascade.close()
	f_write_testing.close()

#--------------------------------------------------------------------------------------------------------------------

def removeTime(file,fileNoTime):
	fr = open(file)
	fw = open(fileNoTime,'w')
        l1 = fr.readlines()

        for x in range(0, len(l1)):
                l2 = l1[x].index(';')
                remaindstring = l1[x][l2+1:len(l1[x])]
                splitstring = remaindstring.split(',')
                print len(splitstring)
                print '-------'
                fw.writelines(l1[x][0:l2])
                if len(splitstring) > 2:
                        for xx in range(0, len(splitstring)-2, 2):
                                newstring = splitstring[xx]
                                print newstring
                                fw.writelines(" "+newstring)
                else:
                        print splitstring[0]
                fw.writelines(" ")
                fw.writelines(splitstring[len(splitstring)-2]+'\n')
        fr.close()
        fw.close()

#--------------------------------------------------------------------------------------------------------------------

def lable(inputFile,outputFile):
        fr = open(inputFile)
	fw = open(outputFile,'w')

	l = fr.readlines()
	count = 0
	for i in range(0, len(l)):
        	li = l[i].split(' ')
	        if len(li) > lable_threshold:
        	        fw.write("1"+",")
                	count = count + 1
	        else:
        	        fw.write("-1"+",")
                	count = count + 1
	print count
	fr.close()
	fw.close()

#--------------------------------------------------------------------------------------------------------------------

def cascade_in_t(inputCascades, inputLable, outputCascades, outputLable):
	f_read_original_cascade = open(inputCascades)
	f_read_original_lable = open(inputLable)
	f_w_cascade = open(outputCascades, 'w')
	f_w_lable = open(outputLable, 'w')
	#t = int(sys.argv[5])
	line = f_read_original_cascade.readlines()
	lable_line = f_read_original_lable.readlines()
	splited_lable_line = lable_line[0].split(',')
	print splited_lable_line[5]
	for line_index in range(0, len(line)):
		source_index = line[line_index].index(';')
		remaindstring = line[line_index][source_index+1:len(line[line_index])]
		splitstring = remaindstring.split(',')
		print splitstring[1] + "============",
		if string.atof(splitstring[1]) < t:
			print str(line_index) + "~~~~~~~~~~~~"
			f_w_lable.writelines(splited_lable_line[line_index]+",")
			f_w_cascade.writelines(line[line_index][0:source_index]+" ")	
		for splitstring_index in range(0, len(splitstring)-1,2):
		#if splitstring_index < len(splitstring) - 4:
			#print splitstring[splitstring_index]
			print float(splitstring[splitstring_index+1])
			if string.atof(splitstring[splitstring_index+1]) < t:
				#print float(splitstring[splitstring_index+1])
				print "************!!*************"
				f_w_cascade.writelines(splitstring[splitstring_index]+" ")
		
		if string.atof(splitstring[1]) < t: 
			f_w_cascade.writelines('\n')	

	f_read_original_cascade.close()
	f_read_original_lable.close()
	f_w_cascade.close()
	f_w_lable.close()

#--------------------------------------------------------------------------------------------------------------------

def frequentPatternMining():
	subprocess.call(['java', '-jar', 'subgraphMining.jar', str(support), _trainingSet])

#--------------------------------------------------------------------------------------------------------------------

def feature(patterns, cascades, features):
	f_read_frequentpatterns = open(patterns)
	f_read_originalCascade = open(cascades)
	f_w_feature = open(features, 'w')
	#path_length_threshold = arg[1]
	count = 1
	pattern_lines = f_read_frequentpatterns.readlines()
	cascade_lines = f_read_originalCascade.readlines()
	for cascade_lines_index in range(0, len(cascade_lines)):
		for pattern_lines_index in range(0, len(pattern_lines)):
			splitedPatternLines = pattern_lines[pattern_lines_index].split(" ")
			flag = "true"
			list_location = []
			for splitedPatternLines_index in range(0, len(splitedPatternLines)):
				if splitedPatternLines[splitedPatternLines_index] in cascade_lines[cascade_lines_index]:
					list_location.append(cascade_lines[cascade_lines_index].find(splitedPatternLines[splitedPatternLines_index]))
				else:
					flag = "false"
			for list_index in range(0, len(list_location)):
				for ll in range(list_index, len(list_location)):
					if list_location[list_index] > list_location[ll]:
						flag = "false"
			if pattern_lines_index != len(pattern_lines)-1:
				if flag is "true":
					f_w_feature.writelines("1" + ",")
					print "1",
				else:
					f_w_feature.writelines("0" + ",")
					print "0",
			else:
				#print "--------------"
				if flag is "true":	
					f_w_feature.writelines("1")
					print "1"
				else:
        	                        f_w_feature.writelines("0")
					print "0"
		f_w_feature.writelines('\n')
		print count 
		count = count + 1

	f_read_frequentpatterns.close()
	f_read_originalCascade.close()
	f_w_feature.close()

#--------------------------------------------------------------------------------------------------------------------

def allnodes(inputFile, outputFile):
	read = open(inputFile)
	write = open(outputFile,'w')

	lines = read.readlines()
	list = []
	for i in range(0, len(lines)):
		l = lines[i].split(" ")
		for ii in range(0, len(l)):
			if l[ii].strip() not in list:	
				list.append(l[ii].strip())
				write.writelines(l[ii].strip()+'\n')
				print l[ii] + " ",
		print str(i)+"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	#list = map(int, list)
	print "----------------"
	#print str(list.index(min(list))) + "    " +  str(min(list))
	print "###################"
	#print str(list.index(max(list))) + "    " + str(max(list))
	list = []
	write.close()
	read.close()

#--------------------------------------------------------------------------------------------------------------------

def feature_nodes(cascade, nodes, outputFile):
	read_cascade = open(cascade)
	read_nodes = open(nodes)
	write = open(outputFile,'w')

	cascade_lines = read_cascade.readlines()
	nodes_lines = read_nodes.readlines()
	list = []

	for c_index in range(0, len(cascade_lines)):
		cascade = cascade_lines[c_index].split(" ")
		for i in range(0, len(cascade)):
			list.append(cascade[i].strip())
		print list
		for n_index in range(0, len(nodes_lines)):
			if nodes_lines[n_index].strip() in list:
				#print nodes_lines[n_index].strip()+"======="
				#print list
				write.writelines("1"+" ")
				print "1",
			else:
				write.writelines("0"+" ")	
				print "0",
		write.writelines('\n')
		list = []
	read_cascade.close()
	read_nodes.close()
	write.close()

#--------------------------------------------------------------------------------------------------------------------

#def classification():
#	---

#--------------------------------------------------------------------------------------------------------------------

def main():
	#print len(sys.argv)
	if len(sys.argv) < 6:
		usage()
		sys.exit(1)
	else:
		global_variance()
		#dic = os.getcwd()
		
	init()
	count()
	print "==================== select cascades by length s.t. upperbound and lowerbound =======================" 
	selectCascades()
	print "#################### generate trainingFile and testingFile #############################"
	print "==================== remove time delay from trainFile and testingFile ========================"
	removeTime(trainingFile, trainingSet)
	removeTime(testingFile, testingSet)
	print "#################### generate trainingSet and testingSet which are not include time delay ##################"
	print "==================== get lable from trainingSet and testingSet s.t. lable_threshold ===================="
	lable(trainingSet, trainingLable)
	lable(testingSet, testingLable)
	print "#################### generate trainingLable and testingLable which are before spliting by t ###################"
	print "==================== split and select part cascades s.t. time delay t ====================="
	cascade_in_t(trainingFile, trainingLable, _trainingSet, _trainingLable)
	cascade_in_t(testingFile, testingLable, _testingSet, _testingLable)
	print "#################### generate _trainingSet, _trainingLable, _testingSet and _testingLable which time delay is less than t ##############"
	print "==================== call frequent pattern mining algorithm by java using _trainingSet ==================="
	frequentPatternMining()
	print "#################### generate frequent patterns ######################"
	print "==================== get features ================="
	feature(patternFile, _trainingSet, _trainingFeature)
	feature(patternFile, _testingSet, _testingFeature)
	print "#################### features for training set and testing set ######################"
	print "==================== get all nodes ================="
	allnodes(_trainingSet, nodesFile)
	print "#################### generate all nodes file #################"
	print "==================== get features for all nodes algorithm ================="
	feature_nodes(_trainingSet, nodesFile, _trainingFeatureAllNodes)
	feature_nodes(_testingSet, nodesFile, _testingFeatureAllNodes)
	print "#################### generate _traingingFeatureAllNodes and _testingFeatureAllNodes ##################"
	print "--------Done!---------"
#--------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
	main()

#--------------------------------------------------------------------------------------------------------------------



