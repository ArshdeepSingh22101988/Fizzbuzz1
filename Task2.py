os.dictdir(path="target directory")

def get_dict_of_files(target):
	#creates a dictionary of folders and files
	dictoffiles=os.dictdir(targetdirectory)
	totalfiles= dict()
	#iterate through all the entries 
	for entry in dictoffiles:
		#a full path is created
		full path= os.path.join(target diectory,entry)
		if os.path.isdir("full path to the diretory"):
			totalfiles= totalfiles +getdictoffiles(full path)
		else:
			totalfiles.append(full path)
	return totalfiles

def main():
	dirname= "enter the name where you want to get the directories from"
	#to get the list of all the files in the directory tree at the path mentioned
		dictoffiles=getdictoffiles(target dict)

	#to print these files
	for elem in dictoflifes:
		print(elem)
	print("*****************")

#to get the list of all the files from the directory"
dictoffiles=dict{}
for (dirpath,dirnames,filenames) in os.walk("target directory"):
	dictoffiles+={"os.path.join(dirpath,file ) for file in filenames]

#printing the files
 for elem in dictoffiles
	print(elem)


f __name__ == '__main__':
    main()
