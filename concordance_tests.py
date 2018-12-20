import unittest
import filecmp
from concordance import *

class TestList(unittest.TestCase):

    def test_01(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_con.txt")
        self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))

    def test_02(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))

    def test_03(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_con.txt")
        self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))

    def test_fake_file(self):
        conc = Concordance()
        with self.assertRaises(FileNotFoundError):
           conc.load_stop_table("fake_file.txt")
        with self.assertRaises(FileNotFoundError):
           conc.load_concordance_table("fake_file.txt")

    def test_empty_file(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("empty.txt")
        conc.write_concordance("empty_con.txt")
        self.assertTrue(filecmp.cmp("empty_con.txt", "empty_sol.txt"))

    def test_stop_file(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("stop_words.txt")
        conc.write_concordance("empty_con.txt")
        self.assertTrue(filecmp.cmp("empty_con.txt", "empty_sol.txt"))

    def test_no_stop_file(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("no_stop.txt")
        conc.write_concordance("no_stop_con.txt")
        self.assertTrue(filecmp.cmp("no_stop_con.txt", "no_stop_sol.txt"))

    def test_only_punc(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("only_punc.txt")
        conc.write_concordance("only_punc_con.txt")
        self.assertTrue(filecmp.cmp("only_punc_con.txt", "only_punc_soln.txt"))

    def test_only_dig(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("only_dig.txt")
        conc.write_concordance("only_dig_con.txt")
        self.assertTrue(filecmp.cmp("only_dig_con.txt", "only_dig_sol.txt"))

    # def test_long_boi(self):
    #     conc = Concordance()
    #     conc.load_stop_table("stop_words.txt")
    #     conc.load_concordance_table()

if __name__ == '__main__':
   unittest.main()
