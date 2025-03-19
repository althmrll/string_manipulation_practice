#Ask user to input sentence
sentence= (input("Enter a sentence:"))

#count number of wordssentence.split()
word= str(sentence.split())
print("there are",word.count(word), "words in the sentence you inputted.")