import re
import xml.etree.ElementTree as ET


def init():
    text = open("./code.tpl","r").read()
    pattern = re.compile("<code>([\s\S]*?)</code>")
    match = pattern.findall(text)
    dic = {}
    # "String"->"@column @id private String $NAME; \n public String get$NAME { return this.$NAME;}\public void set$NAME (String $NAME) {this.$NAME = $NAME;}"
    for mat in match:
        pattern = re.compile("private[\s]+(\w+)")
        tpl_type = pattern.findall(mat)[0]
        dic[tpl_type]=mat

    tree = ET.parse("table.xml")
    root = tree.getroot()
    elem_code = ""
    #$TABLENAME = root.attrib['name']
    table_name = root.attrib['name']
    imports = root.findall("import/item") #import string list

    elems = root.findall("column")
    for elem in elems:
        code_temp = ""
        elem_type = elem.find("field/type").text
        elem_name = elem.find("field/name").text
        code_temp += dic[elem_type]
        elem_code += code_temp.replace('$NAME',elem_name)

    final_code= re.compile('<code>[\s\S]*<\/code>').sub(elem_code,text)
    final_code = final_code.replace('$TABLENAME',table_name)
    print final_code
    text.close()

if __name__ == "__main__":
    init()
        
        

