# -*- coding:utf-8 -*-
# 集成化

import unittest
from traditional import Traditional
from stream import Stream


if __name__ == "__main__":
    # 加载测试套件

    # 传统
    suit_traditional = unittest.TestLoader().loadTestsFromTestCase(Traditional)
    # 流式
    suit_stream = unittest.TestLoader().loadTestsFromTestCase(Stream)

    # 组织测试用例的实例
    suite = unittest.TestSuite([suit_stream])
    # 运行测试用例
    unittest.TextTestRunner(verbosity=2).run(suite)



