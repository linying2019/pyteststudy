import pytest
def setup_module():
    print("setup:整个test_setup_teardown模块开始只执行一次")

def teardown_module():
    print("teardown:整个test_setup_teardown模块结束只执行一次")

def setup_function():
    print("setup:不在类中的测试用例开始的时候都会执行")


def teardown_function():
    print("teardown:不在类中的测试用例结束的时候都会执行")


# 不在类中的方法（）里没有self,只有在类中的方法才有
def test_3():
    print("test_3")


def test_4():
    print("test_4")


class TestClass():
    # 作用于class上
    def setup_class(self):
        print("在class前执行")

    def teardown_class(self):
        print("在class后执行")

    # 作用于方法上的，在每个方法执行前后执行
    def setup_method(self):
        print("setup每个用例开始时执行")

    def teardown_method(self):
        print("teardown每个用例结束执行")

    def test_1(self):
        print("test-1")

    def test_2(self):
        print("test-2")
