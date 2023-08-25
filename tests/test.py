import unittest
import helper
class TestHelperFunctions(unittest.TestCase):

    def test_add(self):
        str = "Test Item"
        helper.add("Test Item")
        self.assertEqual(helper.items[-1].text, str)

    def test_update(self):
        helper.items.append(helper.Item("Sample Item"))
        helper.update(0)
        self.assertTrue(helper.items[0].isCompleted)

    def test_bbb(self):
        helper.add("b")
        self.assertEqual(helper.items[-1].text, "bbb")
        
if __name__ == '__main__':
    unittest.main()