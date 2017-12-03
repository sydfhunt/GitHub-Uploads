fname = open("TheVictors.txt")
fname= fname.read()
word_list= fname.split()
word_dict= {}
for word in word_list:
    if word in word_dict.keys():
        word_dict[word]+=1
    else:
        word_dict[word]=1
popular_words=[]
for number in word_dict.items():
    popular_words.append(number)

popular_words= sorted(popular_words, key=lambda x:x[1], reverse=True)

print (popular_words[:15])
