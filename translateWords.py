import csv
import re
file = open('t8.shakespeare.txt','r')
result = open('result.txt','w')
word = open('find_words.txt','r')
dic = open('french_dictionary.csv','r')
rep = csv.reader(dic)
engfr = {r[0]:r[1] for r in rep}
temp = file.read()
for i in word:
    i = i.strip()
    k=re.compile(i)
    # to replace all words irrespective of case comment above line(12 th line) and uncomment below line(14 th line)
    # k=re.compile(i, re.IGNORECASE)
    if re.search(k,temp):
        temp= re.sub(k,engfr[i.strip()],temp)
result.write(temp)
result.close()
word.close()
dic.close()
file.close()
