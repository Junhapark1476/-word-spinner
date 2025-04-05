import random

class Spinner:
    def __init__(self, filename):
        self.synonyms = {}
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                word, synonym_str = line.split(":")
                synonym_list = synonym_str.split(",")
                self.synonyms[word] = synonym_list  # Store word and its synonyms in a dictionary

    def spin(self, text, threshold=50):
        words = text.split()
        new_words = []

        for word in words:
            if word in self.synonyms:
                chance = random.randint(1, 100)
                if chance > threshold:
                    # Replace the word with a random synonym
                    synonym = random.choice(self.synonyms[word])
                    new_words.append(synonym)
                else:
                    # Keep the original word
                    new_words.append(word)
            else:
                # Word has no synonym in the dictionary
                new_words.append(word)

        return ' '.join(new_words)

