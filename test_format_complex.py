# test_format_complex.py
# 问题：lambda表达式空格、条件表达式格式、字符串拼接、注释位置
import math

# lambda表达式空格缺失
calculate_square = lambda x: x**2
calculate_circle_area = lambda r: math.pi * r * r


# 条件表达式格式混乱
def get_discount(price):
    return price * 0.8 if price > 1000 else price * 0.9 if price > 500 else price


# 字符串拼接无空格
message = (
    "Hello," + "World!" + " This is a test string with no spaces around operators."
)


# 多行注释和代码混合格式问题
def process_data(data):
    # 处理数据
    # 1. 过滤空值
    filtered = [item for item in data if item is not None and item != ""]
    # 2. 转换为整数
    converted = [int(item) for item in filtered if item.isdigit()]
    # 3. 计算总和
    return sum(converted) if converted else 0


# 字典推导式格式问题
data_dict = {
    k: v for k, v in enumerate(["a", "b", "c", "d", "e"]) if v not in ["b", "d"]
}

# 超长import（模拟场景）
from typing import (
    List,
    Dict,
    Optional,
    Tuple,
    Set,
    Union,
    Callable,
    Iterable,
    Generator,
    Coroutine,
)
