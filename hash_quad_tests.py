import unittest
from hash_quad import *

class TestList(unittest.TestCase):

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

    def test_buggy(self):
        ht = HashTable(10)
        ht.insert("cat", 10)
        ht.insert("dog", 11)
        ht.insert("wildebeest", 12)

        self.assertEqual(ht.get_all_keys(), ["cat", "wildebeest", "dog"])
        self.assertEqual(ht.get_index("cat"), 2)
        self.assertEqual(ht.get_index("dog"), 4)
        self.assertEqual(ht.get_index("wildebeest"), 3)
        self.assertEqual(ht.get_num_items(), 3)
        self.assertEqual(ht.get_table_size(), 10)
        self.assertAlmostEqual(ht.get_load_factor(), 3/10)

        self.assertNotEqual(ht.get_index("cat"), 4)
        self.assertNotEqual(ht.get_index("dog"), 3)
        self.assertNotEqual(ht.get_index("wildebeest"), 2)

        self.assertIsNone(ht.get_index("crab"))

        self.assertTrue(ht.in_table("cat"))
        self.assertTrue(ht.in_table("dog"))
        self.assertTrue(ht.in_table("wildebeest"))
        self.assertFalse(ht.in_table("crab"))

        self.assertEqual(ht.get_value("cat"), [10])
        self.assertEqual(ht.get_value("dog"), [11])
        self.assertEqual(ht.get_value("wildebeest"), [12])

        ht.insert("cat", 25)
        ht.insert("cat", 90)
        ht.insert("walrus", 67)

        self.assertEqual(ht.get_value("cat"), [10, 25, 90])
        self.assertTrue(ht.in_table("walrus"))
        self.assertEqual(ht.get_index("walrus"), 0)
        self.assertEqual(ht.get_value("walrus"), [67])
        self.assertEqual(ht.get_table_size(), 10)
        self.assertAlmostEqual(ht.get_load_factor(), 4/10)
        self.assertEqual(ht.get_num_items(), 4)

        ht.insert("walrus", 99)
        self.assertEqual(ht.get_value("walrus"), [67, 99])
        self.assertEqual(ht.get_all_keys(), ["walrus", "cat", "wildebeest", "dog"])
        self.assertEqual(ht.get_table_size(), 10)
        self.assertEqual(ht.get_num_items(), 4)
        self.assertAlmostEqual(ht.get_load_factor(), 4/10)

        ht.insert("buffalo", 37)
        self.assertEqual(ht.get_value("buffalo"), [37])
        self.assertNotEqual(ht.get_value("buffalo"), 37)
        self.assertEqual(ht.get_index("buffalo"), 5)
        self.assertEqual(ht.get_table_size(), 10)
        self.assertEqual(ht.get_num_items(), 5)
        self.assertNotEqual(ht.get_table_size(), 21)
        self.assertEqual(ht.get_all_keys(), ["walrus", "cat", "wildebeest", "dog", "buffalo"])

        ht.insert("zebra", 190)
        self.assertEqual(ht.get_table_size(), 21)

        self.assertEqual(ht.get_index("zebra"), 7)
        self.assertEqual(ht.get_index("cat"), 3)
        self.assertEqual(ht.get_index("walrus"), 1)
        self.assertEqual(ht.get_index("wildebeest"), 11)
        self.assertEqual(ht.get_index("dog"), 20)
        self.assertEqual(ht.get_index("buffalo"), 15)
        self.assertNotEqual(ht.get_index("cat"), 2)
        self.assertTrue(ht.in_table("zebra"))
        self.assertTrue(ht.in_table("cat"))
        self.assertTrue(ht.in_table("walrus"))
        self.assertTrue(ht.in_table("wildebeest"))
        self.assertTrue(ht.in_table("dog"))
        self.assertTrue(ht.in_table("buffalo"))
        self.assertTrue(ht.in_table("cat"))
        self.assertFalse(ht.in_table("Cat"))
        self.assertNotEqual(ht.horner_hash("cat"), ht.horner_hash("Cat"))
        self.assertEqual(ht.get_value("cat"), [10, 25, 90])
        self.assertEqual(ht.get_value("zebra"), [190])
        self.assertIsNone(ht.get_index("Cat"))
        self.assertIsNone(ht.get_value("Zebra"))
        self.assertAlmostEqual(ht.get_load_factor(), 6/21)
        self.assertEqual(ht.get_all_keys(), ["walrus", "cat", "zebra", "wildebeest", "buffalo", "dog"])

        ht.insert("walrus", 900)
        ht.insert("walrus", 1000)

        self.assertEqual(ht.get_value("walrus"), [67, 99, 900, 1000])

        ht.insert("bird", 44)
        self.assertEqual(ht.get_index("bird"), 16)
        ht.insert("bird", 110)
        self.assertEqual(ht.get_value("bird"), [44 ,110])
        self.assertTrue(ht.in_table("bird"))
        self.assertEqual(ht.get_all_keys(), ["walrus", "cat", "zebra", "wildebeest", "buffalo", "bird", "dog"])
        self.assertEqual(ht.get_table_size(), 21)
        self.assertEqual(ht.get_num_items(), 7)
        self.assertAlmostEqual(ht.get_load_factor(), 7/21)

if __name__ == '__main__':
   unittest.main()
