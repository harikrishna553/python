def wordCount(str):
    dict = {}

    for word in str.split():
        count = dict.setdefault(word, 0)
        dict[word] = count+1

    return dict

str = '''Word Count Program
Welcome to the Word Count Program! This program will analyze the text you provide and count the number of words in it
'''

print(wordCount(str))