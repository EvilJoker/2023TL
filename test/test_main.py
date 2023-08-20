from src.main import hello
import sys
from utilstest import UtoolsTest


def test_hello():
    str1 = "a"
    str2 = "b"
    assert UtoolsTest.append_str(str1, str2) == hello(str1, str2), "比较错误"