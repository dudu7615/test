# test_format_basic.py
# 问题：缩进混乱、运算符空格缺失、行超长、逗号位置不规范
def calculate_sum(a,b,c):
    total = a +b*c - (a//b)  # 运算符周围无空格
    # 行超长（超过88字符）
    result = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    if total > 100:
        print("Total is greater than 100: " + str(total))
    else:
      print("Total is less than or equal to 100: " + str(total)) # 缩进不一致
    return total

class TestClass:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def get_info(self):
        return {
            "name":self.name,
            "age":self.age,
            "gender":self.gender
        } # 字典格式不规范

# 函数参数换行问题
def long_function_name(parameter_one, parameter_two, parameter_three, parameter_four, parameter_five, parameter_six):
    return parameter_one + parameter_two + parameter_three + parameter_four + parameter_five + parameter_six
