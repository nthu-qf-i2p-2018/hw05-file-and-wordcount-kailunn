# -*- coding: utf-8 -*-
import csv
import json
import string

def main(filename):
    # read file into lines
    lines = open('i_have_a_dream.txt').readlines()
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
    word_counter = Counter(all_words)
    word_counter.most_common()

    


    # dump to a csv file named "wordcount.csv":
    # word,count
    # a,12345
    # I,23456
    # ...
    with open('word_count.csv','w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['word','count'])
        
    #
        writer.writerows(word_counter.most_common())


    # dump to a json file named "wordcount.json"
    import json
    json.dump(word_counter.most_common(),open('word_counter.json','w'))
    
    import pickle
    pickle.dump(word_counter,open('word_counter.pickle','wb'))
    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly


if __name__ == '__main__':
    main("i_have_a_dream.txt")

    
