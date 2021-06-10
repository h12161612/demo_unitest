# import demo_1
import unittest
import os


# # 构造测试套件
# suite = unittest.TestSuite()
# # 实例化TestLoader
# loader = unittest.TestLoader()
#
# # 加载demo_1下全部用例
# suite.addTest(loader.loadTestsFromTestCase(demo_1.UnittsetDemo))
#
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(suite)

def load_all_case():
    # os.path.join 将目录和文件名合成一个路径
    # os.getcwd(获取当前目录路径)
    path_case = os.path.join(os.getcwd(), 'unit_demo_1')
    discover = unittest.defaultTestLoader.discover(start_dir=path_case, pattern='demo*.py', top_level_dir=None)
    """
    TestLoader
    该类根据各种标准加载测试用例，并将它们返回给测试套件。正常情况下，不需要创建这个类的实例。
    unittest提供了可以共享的defaultTestLoader类，可以使用其子类和方法创建实例，discover()就是其中之一。

    discover(start_dir,pattern='test*.py',top_level_dir=None)
    找到指定目录下所有测试模块，并可递归查到子目录下的测试模块，只有匹配到文件名才能被加载。如果启动的不是顶层目录，那么顶层目录必须单独指定。
    start_dir：要测试的模块名或测试用例目录
    pattern='test*.py'：表示用例文件名的匹配原则。此处匹配文件名以“test”开头的“.py”类型的文件，幸好“*”表示任意多个字符
    top_level_dir=None：测试模块的顶层目录，如果没有顶层目录，默认为None
    """
    print(discover)
    return discover


if __name__ == '__main__':
    run = unittest.TextTestRunner()
    run.run(load_all_case())
