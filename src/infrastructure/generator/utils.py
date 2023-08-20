from pycparser import c_parser, c_ast

Format_MAP = {
            'int': '%d',
            'float': '%f',
            'double': '%f',
            'char': '%c',
            'char[]': '%s',
        }


class StructVisitor(c_ast.NodeVisitor):
    def __init__(self):
        self.struct_list = []

    def get_struct_list(self):
        return self.struct_list

    def visit_Struct(self, node):
        struct_name = node.name
        print(f"struct: {struct_name}")
        self.struct_list.append(f"struct: {struct_name}")
        for decl in node.decls:
            if isinstance(decl, c_ast.Decl) and isinstance(decl.type, c_ast.TypeDecl):
                member_name = decl.name
                member_type = decl.type.type.names[0]
                print(f"    Member: {member_type} {member_name}")
                self.struct_list.append(f"member: {member_type} {member_name}")
            # Decl 表示是一个声明 ， ArrayDecl 是一个 数组， TypeDecl 是一个类型
            if isinstance(decl, c_ast.Decl) and isinstance(decl.type, c_ast.ArrayDecl):
                member_name = decl.name
                member_type = decl.type.type.type.names[0]
                print(f"    Member: {member_type} {member_name}[]")
                self.struct_list.append(f"member: {member_type} {member_name}[]")

def get_struct_list(struct_code):
    parser = c_parser.CParser()
    ast = parser.parse(struct_code)
    struct_visitor = StructVisitor()
    struct_visitor.visit(ast)
    result_list = struct_visitor.get_struct_list()
    print(result_list)
    return result_list