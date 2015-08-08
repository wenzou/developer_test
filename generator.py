import xml.etree.cElementTree as ET

root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, "guid", name="blah").text = "123"
ET.SubElement(doc, "media:credit", name="asdfasd").text = "Some Name"

tree = ET.ElementTree(root)
tree.write("filename.xml")