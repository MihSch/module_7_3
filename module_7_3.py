class WordsFinder:

    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punc = [',', '.', '=', '!', '?', ';', ':', '-', '(', ')']
        with open(self.file_names, encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                for i in line:
                    if i in punc:
                        line = line.replace(i, '')
            all_words.update({self.file_names: line.split()})
        return all_words

    def find(self, word):
        dict_ = {}
        word_key = self.get_all_words()[self.file_names]
        for i in range(len(word_key)):
            if word.lower() == word_key[i]:
                dict_.update({self.file_names: i + 1})
                return dict_

    def count(self, word):
        word_count = {}
        word_key = self.get_all_words()[self.file_names]
        word_count.update({self.file_names: word_key.count(word.lower())})
        return word_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('СЛОВО'))
print(finder2.count('слОво'))
