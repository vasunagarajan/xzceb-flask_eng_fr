# Test cases
import sys
import copy
import os
import unittest

curr_filename = os.path.abspath(__file__)
curr_dir = os.path.dirname(curr_filename)
script_path = os.path.join(curr_dir, "../script")
sys.path.append(script_path)

class TestTranslator(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestTranslator, self).__init__(*args, **kwargs)
    
    def test_youdao(self):
        t = IBMWatson Translator()
        r = t.translate("auto", "zh", "naive")
        self.assertTrue(len(r['paraphrase']) != 0 or len(r['explains']))


if __name__ == "__main__":
    unittest.main()
