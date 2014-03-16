import xml.etree.ElementTree as ET
from string import Template
code_temp = Template('$SUGAR private $TYPE $NAME ;\n')
get_temp = Template('public $TYPE get$NAME \b(){\n\treturn this.$NAME \b;\n}\n')
set_temp = Template('public void set$NAME \b($TYPE $NAME){\n\tthis.$NAME = $NAME;\n}\n')
import_temp = Template("import $IMPORTNAME ;\n")
class_temp = Template("public class $TABLENAME {\n $DECLARE $GETSETFUN \n}")
class Elem:
    elem_dic = {}

    def __init__(self,su,ty,na):
        sugar_temp = ""
        for sugar in su:
            sugar_temp+=sugar;
            sugar_temp+="\n";

        self.elem_dic=dict(SUGAR=sugar_temp,TYPE=ty,NAME=na)

    def set_code_template(self,code_template):
        code_temp = Template(code_template)

    def set_set_fun_template(self,set_fun_template):
        set_temp = Template(set_fun_template)

    def set_get_fun_template(self,get_fun_template):
        get_temp =Template(get_fun_template)


    def get_code(self):
        return code_temp.substitute(self.elem_dic)
    def get_get_fun(self):
        return get_temp.substitute(self.elem_dic)

    def get_set_fun(self):
        return set_temp.substitute(self.elem_dic)

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


    def set_import_template(self,template):
        import_temp = Template(template)
    
    def set_class_template(self,template):
        class_temp = Template(template)

    def get_entity_code(self):
        code = ""
        for imp in self.table_import:
            code += import_temp.substitute(IMPORTNAME=imp)
        declare_code=""
        for elem in self.table_elem:
            declare_code += elem.get_code()

        getset_code =""
        
        for elem in self.table_elem:
            getset_code += elem.get_get_fun()
            getset_code += elem.get_set_fun()

        code +=class_temp.substitute(TABLENAME=self.table_name,DECLARE=declare_code, GETSETFUN=getset_code)

        return code

def init():
    set_template("code.tmp")
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

def set_template(filename):
    settings = open(filename,'r').readlines()
    for line in settings:
        if line.split():
            k,v = line.split(":")
            k=k.strip()
            v=v.strip()
            exec(k+" = Template("+v+")")


if __name__ == '__main__':
    init()
    

