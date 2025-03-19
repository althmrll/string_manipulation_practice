#Ask user to input sentence
sentence= str(input("Enter a sentence:"))

#count number of wordssentence.split()
word= sentence.split()
print("there are",word.count(sentence), "words in the sentence you inputted.")