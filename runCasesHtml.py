# author:LEO GAO
# project Encoding:UTF-8


import unittest
import os


first = os.path.dirname((os.path.abspath(__file__)))
case_path = os.path.join(first, "Cases")
print(case_path)

discover = unittest.defaultTestLoader.discover(start_dir=case_path, pattern='test*.py')
print(discover)
