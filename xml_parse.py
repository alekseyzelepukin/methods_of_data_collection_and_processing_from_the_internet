from pprint import pprint
import xml.etree.ElementTree as etree
tree = etree.parse('lesson_5.xml')
root = tree.getroot()
# for child in root:             #Разбираем дерево по уровням
#     print("first level")
#     print(f"Tag: {child.tag}")
#     print(f"Text: {child.text}")
#     print(f"Attributes: {child.attrib}\n")
#     for result in root.findall('SpellResult'):
#         print("second level")
#         print(f"Tag: {result.tag}")
#         print(f"Text: {result.text}")
#         print(f"Attributes: {result.attrib}\n")
#
#         errors = result.findall('error')
#         for err in errors:
#             print("third level")
#             print(f"Tag: {err.tag}")
#             print(f"Text: {err.text}")
#             print(f"Attributes: {err.attrib}\n")
#             for el in err:
#                 print("fourth level")
#                 print(f"Tag: {el.tag}")
#                 print(f"Text: {el.text}")
#                 print(f"Attributes: {el.attrib}\n")
sr = root.findall('SpellResult')
for er in sr[0]:
    pprint(er)


