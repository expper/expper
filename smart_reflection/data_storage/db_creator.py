import sys
import sqlite3
import xml.etree.ElementTree as ET


def create_and_insert_to_db(c, xml_path):

	# Load XML data from file
	tree = ET.parse(xml_path)

	# Get root object
	root = tree.getroot()
	
	# Create table with name XML root object
	c.execute('''CREATE TABLE ''' + root.tag + ''' (xml_line text)''')

	if root.tag != 'speech':
		# Convert XML hierarchy to string
		x = ET.tostring(root, encoding='utf8', method='xml').decode(encoding='utf8').replace('\'', '\"')
		c.execute("INSERT INTO " + root.tag + " VALUES ('" + x + "')")
		return
	
	for i in root:
		x = ET.tostring(i, encoding='utf8', method='xml').decode(encoding='utf8').replace('\'', '\"')
    	# Insert into DB XML string
		c.execute("INSERT INTO " + root.tag + " VALUES ('" + x + "')")


db_path = sys.argv[1]

# Create new DB from given path
conn = sqlite3.connect(db_path)

# Get cursor
c = conn.cursor()

create_and_insert_to_db(c, "config.xml")
create_and_insert_to_db(c, "speech.xml")
create_and_insert_to_db(c, "tags.xml")
create_and_insert_to_db(c, "phrase.xml")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
