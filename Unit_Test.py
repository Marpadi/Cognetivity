import unittest
import Test_For_Cognetivity


class MyTestCase(unittest.TestCase):
    def test_pass(self):
        result = Test_For_Cognetivity.str("This Summer is hot")
        self.assertEqual(result, "Summer", 6)


if __name__ == '__main__':
    unittest.main()
