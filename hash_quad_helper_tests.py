import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_duplicates(self):
        ht = HashTable(10)
        ht.insert("a", 10)
        ht.insert("a", 11)
        self.assertEqual(ht.get_value("a"), [10, 11])
        ht.insert("a", 10)
        self.assertEqual(ht.get_value("a"), [10, 11])
        ht.insert("a", 10)
        self.assertEqual(ht.get_value("a"), [10, 11])
        ht.insert("k", 11)
        ht.insert("k", 12)
        self.assertEqual(ht.get_value("k"), [11, 12])
        ht.insert("k", 11)
        self.assertEqual(ht.get_value("k"), [11, 12])
        ht.insert("k", 11)
        self.assertEqual(ht.get_value("k"), [11, 12])
        ht.insert("a", 12)
        self.assertEqual(ht.get_value("a"), [10, 11, 12])
        ht.insert("k", 12)
        ht.insert("a", 12)
        ht.insert("k", 12)
        self.assertEqual(ht.get_value("a"), [10, 11, 12])
        self.assertEqual(ht.get_value("k"), [11, 12])

    def test_01a(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_table_size(), 7)
        ht = HashTable(9)
        self.assertEqual(ht.get_table_size(), 9)
        self.assertNotEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_num_items(), 0)
        ht.insert("Item 1", 34)
        self.assertEqual(ht.get_num_items(), 1)
        ht.insert("Item 2", 35)
        ht.insert("Item 3", 36)
        self.assertEqual(ht.get_num_items(), 3)
        ht.insert("Item 1", 39)
        self.assertEqual(ht.get_num_items(), 3)
        ht.insert("Item 3", 40)
        self.assertEqual(ht.get_num_items(), 3)

    def test_01c(self):
        ht = HashTable(7)
        self.assertAlmostEqual(ht.get_load_factor(), 0)
        ht.insert("Item 1", 32)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)
        ht.insert("Item 2", 34)
        self.assertAlmostEqual(ht.get_load_factor(), 2/7)
        ht.insert("Item 1", 39)
        self.assertAlmostEqual(ht.get_load_factor(), 2/7)
        ht.insert("Item 3", 33)
        self.assertAlmostEqual(ht.get_load_factor(), 3/7)
        ht.insert("Item 4", 40)
        self.assertAlmostEqual(ht.get_load_factor(), 4/15)
        ht.insert("Item 1", 41)
        self.assertAlmostEqual(ht.get_load_factor(), 4/15)
        ht.insert("Item 7", 42)
        self.assertAlmostEqual(ht.get_load_factor(), 1/3)

    def test_01d(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_all_keys(), [])
        ht.insert("Item 1", 32)
        self.assertEqual(ht.get_all_keys(), ["Item 1"])
        ht.insert("Item 2", 34)
        ht.insert("Item 3", 37)
        self.assertEqual(ht.get_all_keys(), ["Item 2", "Item 3", "Item 1"])
        ht.insert("Item 1", 39)
        self.assertEqual(ht.get_all_keys(), ["Item 2", "Item 3", "Item 1"])
        self.assertNotEqual(ht.get_all_keys(), ["Item 3", "Item 1", "Item 1", "Item 2"])

    def test_01e(self):
        ht = HashTable(7)
        self.assertEqual(ht.in_table("cat"), False)
        ht.insert("Item 1", 2)
        self.assertEqual(ht.in_table("Item 1"), True)
        ht.insert("Item 2", 3)
        ht.insert("Item 3", 4)
        self.assertTrue(ht.in_table("Item 2"))
        self.assertTrue(ht.in_table("Item 3"))
        self.assertFalse(ht.in_table("Item 4"))

    def test_01f(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_value("cat"), None)
        ht.insert("Item 1", 34)
        ht.insert("Item 2", 35)
        self.assertEqual(ht.get_value("Item 1"), [34])
        self.assertEqual(ht.get_value("Item 2"), [35])
        self.assertEqual(ht.get_value("Item 3"), None)
        ht.insert("Item 1", 37)
        self.assertEqual(ht.get_value("Item 1"), [34, 37])

    def test_01g(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_index("cat"), None)
        ht.insert("Item 1", 34)
        ht.insert("Item 2", 35)
        ht.insert("Item 3", 36)
        self.assertEqual(ht.get_index("Item 1"), 6)
        self.assertEqual(ht.get_index("Item 2"), 0)
        self.assertEqual(ht.get_index("Item 3"), 1)
        self.assertEqual(ht.get_index("Item 4"), None)

    def test_01h(self):
        ht = HashTable(7)
        self.assertEqual(ht.horner_hash("cat"), 3)
        self.assertEqual(ht.horner_hash("Item 1"), 6)
        self.assertEqual(ht.horner_hash("Item 2"), 0)
        self.assertEqual(ht. horner_hash("Item 3"), 1)
        self.assertNotEqual(ht.horner_hash("item 1"), ht.horner_hash("Item 1"))
        self.assertNotEqual(ht.horner_hash("Item 4"), 5)


    def test_02a(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)
        ht.insert("dog", 7)
        ht.insert("crab", 8)
        ht.insert("turtle", 3)
        self.assertEqual(ht.get_table_size(), 15)

    def test_02b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_02c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_02d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_02e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)
        ht = HashTable(10)
        ht.insert("a", 1)
        ht.insert("u", 4)
        ht.insert("u", 5)
        self.assertTrue(ht.in_table("u"))
        ht = HashTable(4)
        ht.insert("a", 15)
        ht.insert("k", 17)
        self.assertEqual(ht.in_table("u"), False)

    def test_02f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), [5])

    def test_02g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

    def test_03(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert("cat", 17)
        self.assertEqual(ht.get_value("cat"), [5, 17])

    def test_04(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

        ht.insert("dog", 8)
        self.assertEqual(ht.get_num_items(), 2)
        self.assertEqual(ht.get_index("dog"), 6)
        self.assertAlmostEqual(ht.get_load_factor(), 2 / 7)

        ht.insert("mouse", 10)
        self.assertEqual(ht.get_num_items(), 3)
        self.assertEqual(ht.get_index("mouse"), 4)
        self.assertAlmostEqual(ht.get_load_factor(), 3 / 7)

        ht.insert("elephant", 12) # hash table should be resized
        self.assertEqual(ht.get_num_items(), 4)
        self.assertEqual(ht.get_table_size(), 15)
        self.assertAlmostEqual(ht.get_load_factor(), 4 / 15)
        self.assertEqual(ht.get_index("cat"), 12)
        self.assertEqual(ht.get_index("dog"), 14)
        self.assertEqual(ht.get_index("mouse"), 13)
        self.assertEqual(ht.get_index("elephant"), 9)
        keys = ht.get_all_keys()
        keys.sort()
        self.assertEqual(keys, ["cat", "dog", "elephant", "mouse"])

        ht.insert("god", 10)
        self.assertEqual(ht.get_num_items(), 5)
        self.assertEqual(ht.get_table_size(), 15)
        self.assertAlmostEqual(ht.get_load_factor(), 5 / 15)
        self.assertEqual(ht.get_index("god"), 0)

        ht.insert("gdo", 12)
        self.assertEqual(ht.get_index("gdo"), 3)

    def test_wrap(self):
        ht = HashTable(10)
        ht.insert("c", 1)
        ht.insert("m", 2)
        ht.insert("w", 3)
        self.assertEqual(ht.get_index("c"), 9)
        self.assertEqual(ht.get_index("m"), 0)
        self.assertEqual(ht.get_index("w"), 3)

        self.assertEqual(ht.in_table("c"), True)
        self.assertEqual(ht.in_table("m"), True)
        self.assertEqual(ht.in_table("w"), True)

        self.assertEqual(ht.get_value("c"), [1])
        self.assertEqual(ht.get_value("m"), [2])
        self.assertEqual(ht.get_value("w"), [3])

        ht.insert("d", 12)
        self.assertEqual(ht.get_index("d"), 1)

        ht.insert("n", 13)
        self.assertEqual(ht.get_index("n"), 4)

if __name__ == '__main__':
   unittest.main()
