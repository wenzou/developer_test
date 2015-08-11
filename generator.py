import xml.etree.cElementTree as ET

#this is a simply generator that generates large xml for testing
root = ET.Element("root")
root.set('xmlns:media', "http://search.yahoo.com/mrss/")
for i in range(1, 1000000):
    doc = ET.SubElement(root, "doc")
    id = "id_"
    id += `i`
    ET.SubElement(doc, "guid", name="blah").text = id
    for j in range(1, 5):
        string = id + "Some Name"
        string += `j`
        ET.SubElement(doc, "media:credit", name="asdfasd").text = string

tree = ET.ElementTree(root)
tree.write("filename1000000.xml")