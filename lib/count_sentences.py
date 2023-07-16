class MyString:
    def __init__(self, value=None):
        if isinstance(value, str):
            self.value = value
        else:
            print("The value must be a string.")
            self.value = ""
        self.punctuation = [".", "?", "!"]

    def is_sentence(self):
        return self.sentence_type() == "sentence"

    def is_question(self):
        return self.sentence_type() == "question"

    def is_exclamation(self):
        return self.sentence_type() == "exclamation"

    def sentence_type(self):
        if not self.value:
            return "unknown"

        last_char = self.value[-1]
        if last_char == ".":
            return "sentence"
        elif last_char == "?":
            return "question"
        elif last_char == "!":
            return "exclamation"
        else:
            return "unknown"

    def count_sentences(self):
        new_string = self.remove_repeated_punctuations()
        new_string = self.replace_punctuation(new_string)
        new_string = new_string[:-1]
        string_list = new_string.split('|')
        return len(string_list) if self.value else 0

    def remove_repeated_punctuations(self):
        if not self.value:
            return ""
        new_string = ""
        for i, char in enumerate(self.value):
            if i == 0 or char != self.value[i - 1] or char not in self.punctuation:
                new_string += char
        return new_string

    def replace_punctuation(self, mod_string):
        for punc in self.punctuation:
            mod_string = mod_string.replace(punc, "|")
        return mod_string
