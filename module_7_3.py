class WordsFinder:
    def __init__(self, *files):
        self.file_names = list(files)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        line = line.replace(char, '')
                    words += line.split()
                all_words[file_name] = words
        return all_words
    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            word = word.lower()
            if word in words:
                result[file_name] = words.index(word) + 1
            else:
                result[file_name] = -1
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            word = word.lower()
            count = words.count(word)
            result[file_name] = count
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего