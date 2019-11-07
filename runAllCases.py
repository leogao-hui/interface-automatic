# author:LEO GAO
# project Encoding:UTF-8


import os
import sys
import unittest

sys.dont_write_bytecode = True

first = os.path.dirname((os.path.abspath(__file__)))
case_path = os.path.join(first, "Cases/Register/")
sys.path.append(case_path)

discover = unittest.defaultTestLoader.discover(start_dir=case_path,
                                               pattern='test*.py')
runner = unittest.TextTestRunner()
runner.run(discover)

