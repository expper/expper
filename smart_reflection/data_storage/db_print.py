import sys
import sqlite3
import xml.etree.ElementTree as ET

def print_all(r):
    if len(r) == 0:
        return
    i = 0
    for child in r:
        s = ""
        if r[i].text != None:
            s = r[i].text
        print(child.tag, child.attrib, s)
        i += 1
        print_all(child)

db_path = sys.argv[1]
conn = sqlite3.connect(db_path)
c = conn.cursor()
for i in c.execute('SELECT * FROM config'):
    root = ET.fromstring(i[0])
    print(root.tag, root.text)
    print_all(root)
    print("--------------")
print("===========")
for i in c.execute('SELECT * FROM speech'):
    root = ET.fromstring(i[0])
    print(root.tag, root.text)
    print_all(root)
    print("--------------")

for i in c.execute('SELECT * FROM tags'):
    root = ET.fromstring(i[0])
    print(root.tag, root.text)
    print_all(root)
    print("--------------")


for i in c.execute('SELECT * FROM phrase'):
    root = ET.fromstring(i[0])
    print(root.tag, root.text)
    print_all(root)
    print("--------------")

conn.close()
