class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punc = [',', '.', '=', '!', '?', ';', ':', '-', '(', ')']
        for file_n in self.file_names:
            with open(file_n, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    for pun in punc:
                        line = line.replace(pun, '')
                    line = line.replace(' - ', ' ')
                    words.extend(line.split())
                all_words[file_n] = words
        return all_words

    def find(self, word):
        dict_ = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                dict_[key] = value.index(word.lower()) + 1
        return dict_

    def count(self, word):
        word_count = {}
        for value, key in self.get_all_words().items():
            count = key.count(word.lower())
            word_count[value] = count
        return word_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('СЛОВО'))
print(finder2.count('слОво'))
