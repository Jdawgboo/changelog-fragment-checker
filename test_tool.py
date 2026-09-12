import unittest
from tool import validate
class ChangelogTests(unittest.TestCase):
 def test_rules(self):self.assertEqual(validate('123.feature.md','Add a feature',['feature']),[]);self.assertIn('invalid filename category',validate('123.bad.md','x',['feature']));self.assertIn('empty description',validate('123.feature.md','',['feature']))
if __name__=='__main__':unittest.main()
