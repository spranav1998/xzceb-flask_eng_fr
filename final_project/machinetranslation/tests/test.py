import unittest
import sys
sys.path.append( '/home/project/xzceb-flask_eng_fr/final_project/machinetranslation' )
from translator import englishtofrench, frenchtoenglish

class Testenglishtofrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtofrench(None),None)
        self.assertEqual(englishtofrench('Hello'),'Bonjour')

class Testfrenchtoenglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchtoenglish(None),None)
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello')

unittest.main()