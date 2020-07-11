word_list = open("sowpods.txt", "r+")
words = []
for word in word_list.readlines():
    words.append(word)