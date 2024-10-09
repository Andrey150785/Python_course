

class WordsFinder:
    file_names = []
    all_words = {}
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                self.all_words[file_name] = [i.strip(',.=!?;:-') for i in file.read().lower().split()]
        return self.all_words

    def find(self, word):
        for key, value in self.get_all_words().items():
            if word in value:
                return {key: value.index(word)+1}

    def count(self, word):
        for key, value in self.get_all_words().items():
            if word in value:
                return {key: value.count(word)}


finder2 = WordsFinder('test.txt', 'test2.txt', 'test1.txt')

print(finder2.get_all_words())
print(finder2.find('text'))
print(finder2.count('text'))
