file=open("book1.txt","r")
lines = book.readlines()


for line in lines:
	words=line.split("")
	for word in words:
		wordlist.append(word)



