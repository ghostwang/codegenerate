import re
import xml.etree.ElementTree as ET

def init():
    text = open("./html.tpl","r").read()
    pattern = re.compile(u"<code>([\s\S]*)</code>")
    match = pattern.findall(text)
    
    if len(match) > 1:
        print "label ERROR"
        return -1
    
    tree = ET.parse("table.xml")
    root = tree.getroot()
    elem_code = ""
    table_name = root.attrib['name']
    
    elems = root.findall("column")

    for elem in elems:
        code_temp = ""
        elem_name = elem.find("field/name").text
        elem_code += match[0].replace('$NAME',elem_name)

    final_code = pattern.sub(elem_code,text)
    final_code = final_code.replace('$TABLENAME',table_name)
    print final_code
    text.close()

if __name__ == "__main__":
    init()

