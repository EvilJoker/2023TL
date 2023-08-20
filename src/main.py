
# 独立运行时，需要去掉 src
from src.infrastructure.generator.print_generator import PrintGenerator
from src.infrastructure.file.struct_loader import load

# demo
def hello(str1, str2):
    return str1 + str2
# 函数生成
def generate_print_function(filepath) :
    generator = PrintGenerator()
    source_code = load(filepath)
    print("[sourcecode]:\n {}".format(source_code))
    print_func_define = generator.print_function(source_code)
    print("[ouputcode ]:\n {}".format(print_func_define))

if __name__ == '__main__':
    print("start !!! ")

    generate_print_function("resource/c/demo.cpp")


