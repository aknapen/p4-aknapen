from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = HashTable(191)          # hash table for stop words
        self.concordance_table = HashTable(191)   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            file = open(filename, "r")
            for word in file:
                self.stop_table.insert(word.rstrip(), None)
            file.close()
        except FileNotFoundError:
            raise FileNotFoundError("File does not exist")

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table,
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            file = open(filename, "r")
            stop_words = self.stop_table.get_all_keys()
            count = 1
            for line in file:
                if line == "\n":
                    count += 1
                    continue
                frm = '''!"#$%&()*+,-./:;<=>?@[\]^_`{|}~''' + string.digits
                to = " " * len(frm)
                table = str.maketrans(frm, to)
                translation = line.translate(table)
                frm = "'"
                table = str.maketrans({key: None for key in frm})
                translation = translation.translate(table)
                translation = translation.rstrip("\n")
                translation = set(translation.split())
                for word in translation:
                    word = word.lower()
                    if not self.stop_table.in_table(word):
                        self.concordance_table.insert(word, count)
                count += 1
            file.close()

        except FileNotFoundError:
            raise FileNotFoundError("File does not exist")

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        file = open(filename, "w")
        vals = ""
        strings = []
        for slot in self.concordance_table.hash_table:
            if slot != None:
                for num in slot.get_value():
                    vals += str(num) + " "
                vals = vals[:-1]
                vals += "\n"
                lower = slot.get_key().lower()
                strings += [lower + ": " + vals]
                vals = ""
        strings.sort()
        for i in range(len(strings)):
            if i == len(strings)-1:
                strings[i] = strings[i].rstrip()
            file.write(strings[i])
        file.close()

conc = Concordance()
conc.load_stop_table("stop_words_the.txt")
conc.load_concordance_table("file_the.txt")
conc.write_concordance("test.txt")
