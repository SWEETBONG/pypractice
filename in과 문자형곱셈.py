sentence=input('write any word:')
numberofletters=0

for oneletter in sentence:
    if oneletter !=' ':
        numberofletters +=1
print(sentence * numberofletters)       
