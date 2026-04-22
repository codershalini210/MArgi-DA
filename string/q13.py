sentence = "hello world this is dummyworddummy sentence , simultaneously we are working here"
wordslist=sentence.split(" ")
bword =""
for w in wordslist:
    if(bword.__len__() < w.__len__()):
        bword = w
print("biggest word in given sentence is ",bword)