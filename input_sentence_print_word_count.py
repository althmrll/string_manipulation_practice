#Ask user to input sentence
sentence= input("Enter a sentence:")

#count number of words
word_count=sentence.split()
print("there are", word_count.count(word_count), "words in the sentence you inputted.")