import unittest
import os


def run_all_testcase():
    case_path = os.path.join(os.getcwd(), '../case')  # 因为本工程与case的python包不在一个级别，所以必须加[../]
    discover = unittest.defaultTestLoader.discover(case_path, pattern='*Case.py', top_level_dir=None)
    return discover


if __name__ == '__main__':
    run = unittest.TextTestRunner(verbosity=2)
    run.run(run_all_testcase())
