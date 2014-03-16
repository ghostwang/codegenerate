import xml.etree.ElementTree as ET
class Elem:
    elem_sugar = []
    elem_type = ''
    elem_name = ''

    def __init__(self,su,ty,na):
        self.elem_sugar = su
        self.elem_type = ty
        self.elem_name = na

    def print_elem(self):
        for su in self.sugar:
            print su
        print "private "+self.elem_type +" "+self.elem_name + ";"
    def get_code(self):
        code = ""
        for su in self.elem_sugar:
            code += su;
            code += "\n"

        code += "private " + self.elem_type +" "+self.elem_name + ";\n"
        return code
    def get_get_fun(self):
        code = "public "+self.elem_type+" get"+self.elem_name+"(){\n\treturn this."+self.elem_name+";\n}\n"
        return code

    def get_set_fun(self):
        code = "public void set"+self.elem_name+" ("+self.elem_type+" "+self.elem_name+"){\n\tthis."+self.elem_name+"="+self.elem_name+";\n}\n"
        return code

class Table:
    table_name = ''
    table_import = []
    table_elem = []
    def __init__(self,tn):
        self.table_name=tn
    def add_import(self, import_name):
        self.table_import.append(import_name)

    def add_elem(self, elem_name):
        self.table_elem.append(elem_name)

    def get_entity_code(self):
        code = ""
        for imp in self.table_import:
            code += "import "+imp+";\n"
        code += "public class "+self.table_name+" {\n"
        for elem in self.table_elem:
            code += elem.get_code()
        
        for elem in self.table_elem:
            code += elem.get_get_fun()
            code += elem.get_set_fun()

        code += "}"

        return code

def init():
    tree = ET.parse("table.xml")
    root = tree.getroot()
    table = Table(root.attrib['name'])
    imports = root.findall("import/item")
    for im in imports:
        table.add_import(im.text)

    elems = root.findall("column")
    for elem in elems:
        su = []
        for su_elem in elem.findall("sugar/item"):
            su.append(su_elem.text)
        table.add_elem(Elem(su,elem.find("field/type").text,elem.find("field/name").text))

    print table.get_entity_code()

if __name__ == '__main__':
    init()
    

