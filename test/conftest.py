import os
import sys

import pytest

# 插入父级目录
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

sys.path.append("/code/10312862/test")

# 定义一个 fixture
@pytest.fixture
def my_fixture():
    # 在这里可以执行一些设置操作
    utils = "some_resource"
    print(sys.path)
    yield utils  # yield 后面的内容将作为被修饰函数的返回值
    # 在这里可以执行一些清理操作

    # clean up / reset resources here

# 测试methonds 无需启动 server
