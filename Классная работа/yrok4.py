class StringIterator:
    def __init__(self, strings):
        self.strings = strings
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.strings):
            result = self.strings[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


strings_list = ["That", "feeling", "when", "knee", "surgery", "is", "tomorrow"]
iterator = StringIterator(strings_list)
for string in iterator:    print(string)
