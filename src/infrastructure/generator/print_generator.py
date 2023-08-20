
from src.infrastructure.generator.utils import Format_MAP, StructVisitor, get_struct_list

class PrintGenerator:

    def print_function(self, struct_code):
        struct_list = get_struct_list(struct_code)
        # 解析
        struct_name = struct_list[0].split(":")[1].strip()
        function_name = "Print" + struct_name.lower().replace("t_", "", 1).capitalize()
        point_name = "pt" + struct_name.lower().replace("t_", "", 1).capitalize()

        mebs = struct_list[1:]
        name_mebs =[]
        type_mebs = []
        format_mebs = []
        for member in mebs:
            arr = member.replace('member:', "").strip().split(" ")
            type_m = arr[0]
            if type_m == "char":
                if '[' in member and ']' in member:
                    type_m = "char[]"

            name_m = arr[1]
            if '[' in arr[1]:
                name_m = arr[1].split("[")[0]

            format_char = Format_MAP[type_m]

            format_mebs.append(format_char)
            type_mebs.append(type_m)
            name_mebs.append(name_m)
        

        left, right="", ""

        for name , format in zip(name_mebs, format_mebs):
            left += "{}: {}\\n".format(name, format)
            right += "ptStudent->{}, ".format(name)
        value_str = "\"{}\", {}".format(left, right[:-2])




        template = """INT {}({} *{})
        {{
            if (NULL == {} )
            {{
                return -1;
            }}
            
            return printf({});
        }}
        """.format(function_name, struct_name, point_name, point_name, value_str)


        return template
    
