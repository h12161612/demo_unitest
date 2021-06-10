import unittest


class UnittsetDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('类开始执行')

    @classmethod
    def tearDownClass(cls):
        print('类执行结束')

    def setUp(self):
        print('Case开始')

    def tearDown(self):
        print('Case结束')

    def testCase1(self):
        print('demo_2 Case1')

    @unittest.skip('跳过这个case')
    def testCase2(self):
        print('demo_2 Case2')
        self.assertEqual(2, 2)

    def testCase3(self):
        print('demo_2 Case3')
