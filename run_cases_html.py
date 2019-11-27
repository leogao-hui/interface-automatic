# author:LEO GAO
# project Encoding:UTF-8


import unittest
import os
from Common import HTMLTestRunner


first = os.path.dirname((os.path.abspath(__file__)))
case_path = os.path.join(first, "Cases/Login")
report_path = os.path.join(first, "Common/Report")


def add_case(casepath=case_path, rule="test*.py"):

    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(casepath, pattern=rule,)

    return discover


def run_case(all_case, reportpath=report_path):

    #  执行所有的用例, 并把结果写入测试报告
    htmlreport = reportpath+r"/result.html"
    print("测试报告生成地址：%s" % htmlreport)
    fp = open(htmlreport, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="测试报告", description="用例执行情况")

    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()


if __name__ == "__main__":
    cases = add_case()
    run_case(cases)
