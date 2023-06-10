from collections import Counter
import string

def word_count(file_path, count_specific_word=None, most_frequent_words=None, exclude_stopwords=False):
    with open(file_path, 'r') as file:
        text = file.read()
        if exclude_stopwords:
            with open('stopwords.txt', 'r') as sw_file:
                stopwords = sw_file.read().split()
            words = [word for word in text.lower().split() if word not in stopwords]
        else:
            words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
        if count_specific_word:
            count = words.count(count_specific_word.lower())
            return count
        elif most_frequent_words:
            counter = Counter(words)
            return counter.most_common(most_frequent_words)
        else:
            return len(words)

file_path = input("Enter file path: ")
print("Total words:", word_count(file_path))
print("Occurrences of 'the':", word_count(file_path, count_specific_word='the'))
print("Top 10 most frequent words:", word_count(file_path, most_frequent_words=10))
print("Total words (excluding stopwords):", word_count(file_path, exclude_stopwords=True))