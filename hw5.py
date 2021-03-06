# -*- coding: utf-8 -*-
import csv
import json
import string
import pickle

def main(filename):
    # read file into lines
    lines = open(filename).readlines()
    # declare a word list
    all_words = []

    # extract all words from lines
    for line in lines:
        # split a line of text into a list words
        # "I have a dream." => ["I", "have", "a", "dream."]
        line=line.strip()
        words = line.split()

        # check the format of words and append it to "all_words" list
        for word in words:
            
            # then, remove (strip) unwanted punctuations from every word
            # "dream." => "dream"
            
            word = word.strip(string.punctuation)
            
            # check if word is not empty
            if word:
                # append the word to "all_words" list
                all_words.append(word)
     

    # compute word count from all_words
    
    from collections import Counter
    wordcount = Counter(all_words)
    wordcount.most_common()

    


    # dump to a csv file named "wordcount.csv":
    # word,count
    # a,12345
    # I,23456
    # ...
    with open('wordcount.csv','w',newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['word','count'])
        
    #
        writer.writerows(wordcount.most_common())


    # dump to a json file named "wordcount.json"
    import json
    json.dump(wordcount.most_common(),open('wordcount.json','w'))
    
    import pickle
    pickle.dump(wordcount,open('wordcount.pkl','wb'))
    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly


if __name__ == '__main__':
    main("i_have_a_dream.txt")
