import pytest


def add_function(a, b):
    return a+b


@pytest.mark.parametrize("a,b,expected", [
    (3, 5, 8), (1000, 2000, 4000)], ids=["int", "longint"])
# 其中ids表示分别为测试数据起别名


def test_add(a, b, expected):
    assert add_function(a, b) == expected