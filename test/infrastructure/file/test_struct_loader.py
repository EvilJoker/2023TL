from src.infrastructure.file.struct_loader import load
import sys
def test_load():
    filepath = "resource/c/demo.cpp"
    source_code = load(filepath)
    print(source_code)
    assert "struct" in source_code