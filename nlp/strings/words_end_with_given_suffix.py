def print_words_with_given_suffix(file, suffix, separator=' '):
    for line in open(file):
        for word in line.split(separator):
            if word.endswith(suffix):
                print(word)

print_words_with_given_suffix('test.txt', 'ing')