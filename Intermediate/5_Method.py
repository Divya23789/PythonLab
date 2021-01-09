import unittest
import MyModule
class Testcap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = MyModule.cap_test(text)
        print(result)
        self.assertEqual(result,'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = MyModule.cap_test(text)
        print(result)
        self.assertEqual(result,'Monty python')

if __name__ == '__main__':
    unittest.main()
