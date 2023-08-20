from src.infrastructure.generator.print_generator import PrintGenerator
from src.infrastructure.file.struct_loader import load


class TestPrintGenerator:

    # 发送初始化 请求
    def test_print_function(self):

        generator = PrintGenerator()

        filepath = "resource/c/demo.cpp"
        source_code = load(filepath)
        print(source_code)
        print_func_define = generator.print_function(source_code)
        print(print_func_define)
        assert "printf" in print_func_define