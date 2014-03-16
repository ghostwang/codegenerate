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

class Table:
    table_name = ''
    def __init__(self,tn):
        self.table_name=tn

def init():
    tree = ET.parse("~/Storage/src/python/xml/table.xml")
    root = tree.getroot()
    
tree = ET.parse('./Stroage/src/python/xml/table.xml')

