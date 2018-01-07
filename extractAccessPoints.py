import xml.etree.ElementTree as ET
from os import listdir
import sys
import csv

# The argument is a folder with EAD files
# It is recommended that the folder has the name of the CHI as part of it
# in order to identify after that the provenance of the tables of the output
folder = sys.argv[1]


filenames = listdir(folder)

# List of XML access point objects. It will be used to build after that the Python dictionaries.
subject_objects = []
place_objects = []
cb_objects = []
person_objects = []
creator_objects = []


# Python dictionaries for the different access point types (including creators as access point :/ )
subjectAPs = {}
placeAPs = {}
cbAPs = {}
personAPs = {}
creatorAPs = {}

# Parse the files and extract the access points as Element Tree objects. They will be stored in lists
# for each access point type.
for filename in filenames:
	print (filename)
	eadfile = folder + '/' + filename
	print (eadfile)
	tree = ET.parse(eadfile)
	root = tree.getroot()
	subjects = root.findall(".//{urn:isbn:1-931666-22-9}controlaccess/{urn:isbn:1-931666-22-9}subject")
	subject_objects = subject_objects + subjects
	places = root.findall(".//{urn:isbn:1-931666-22-9}geogname")
	place_objects = place_objects + places
	corporate_bodies = root.findall(".//{urn:isbn:1-931666-22-9}controlaccess/{urn:isbn:1-931666-22-9}corpname")
	cb_objects = cb_objects + corporate_bodies
	people = root.findall(".//{urn:isbn:1-931666-22-9}controlaccess/{urn:isbn:1-931666-22-9}persname")
	person_objects = person_objects + people
	creators = root.findall(".//{urn:isbn:1-931666-22-9}origination")
	creator_objects = creator_objects + creators



# Extraction of text and attributes of access points of type subject
for subject in subject_objects:
	if subject.text in subjectAPs:
		subjectAPs[subject.text]['counter'] += 1
		if 'source' in subject.attrib:
			if len(subjectAPs[subject.text]['source']) == 0:
				subjectAPs[subject.text]['source'] = subject.attrib['source']
				subjectAPs[subject.text]['authfilenumber'] = subject.attrib['authfilenumber']
	else:
		instance = {}
		instance['text'] = subject.text
		instance['counter'] = 1
		if 'source' in subject.attrib:
			instance['source'] = subject.attrib['source']
			instance['authfilenumber'] = subject.attrib['authfilenumber']
		else:
			instance['source'] = ''
			instance['authfilenumber'] = ''
		subjectAPs[subject.text] = instance


# Extraction of text and attributes of access points of type place
for place in place_objects:
	if place.text in placeAPs:
		placeAPs[place.text]['counter'] += 1
		if 'source' in place.attrib:
			if len(placeAPs[place.text]['source']) == 0:
				placeAPs[place.text]['source'] = place.attrib['source']
				placeAPs[place.text]['authfilenumber'] = place.attrib['authfilenumber']
	else:
		instance = {}
		instance['text'] = place.text
		instance['counter'] = 1
		if 'source' in place.attrib:
			instance['source'] = place.attrib['source']
			instance['authfilenumber'] = place.attrib['authfilenumber']
		else:
			instance['source'] = ''
			instance['authfilenumber'] = ''
		placeAPs[place.text] = instance


# Extraction of text and attributes of access points of type corporate body
for cb in cb_objects:
	if cb.text in cbAPs:
		cbAPs[cb.text]['counter'] += 1
		if 'source' in cb.attrib:
			if len(cbAPs[cb.text]['source']) == 0:
				cbAPs[cb.text]['source'] = cb.attrib['source']
				cbAPs[cb.text]['authfilenumber'] = cb.attrib['authfilenumber']
	else:
		instance = {}
		instance['text'] = cb.text
		instance['counter'] = 1
		if 'source' in cb.attrib:
			instance['source'] = cb.attrib['source']
			instance['authfilenumber'] = cb.attrib['authfilenumber']
		else:
			instance['source'] = ''
			instance['authfilenumber'] = ''
		cbAPs[cb.text] = instance


# Extraction of text and attributes of access points of type person
for person in person_objects:
	if person.text in personAPs:
		personAPs[person.text]['counter'] += 1
		if 'source' in person.attrib:
			if len(personAPs[person.text]['source']) == 0:
				personAPs[person.text]['source'] = person.attrib['source']
				personAPs[person.text]['authfilenumber'] = person.attrib['authfilenumber']
	else:
		instance = {}
		instance['text'] = person.text
		instance['counter'] = 1
		if 'source' in person.attrib:
			instance['source'] = person.attrib['source']
			instance['authfilenumber'] = person.attrib['authfilenumber']
		else:
			instance['source'] = ''
			instance['authfilenumber'] = ''
		personAPs[person.text] = instance

# Creators should be handle in a more sophisticate way, since they can be represented as text or as a deeper level in the
# XML tree, as text of other elements (persname, corpname, name and famname)
for creator in creator_objects:
	creator_pers = creator.findall('{urn:isbn:1-931666-22-9}persname')
	creator_cb = creator.findall('{urn:isbn:1-931666-22-9}corpname')
	creator_name = creator.findall('{urn:isbn:1-931666-22-9}name')
	creator_fam = creator.findall('{urn:isbn:1-931666-22-9}famname')
	# If the creator is tagged as <persname>
	if len(creator_pers) > 0:
		for pers in creator_pers:
			if pers.text in creatorAPs:
				creatorAPs[pers.text]['counter'] += 1
				if 'source' in pers.attrib:
					if len(creatorAPs[pers.text]['source']) == 0:
						creatorAPs[pers.text]['source'] = pers.attrib['source']
						creatorAPs[pers.text]['authfilenumber'] = pers.attrib['authfilenumber']
			else:
				instance = {}
				instance['text'] = pers.text
				instance['counter'] = 1
				if 'source' in pers.attrib:
					instance['source'] = pers.attrib['source']
					instance['authfilenumber'] = pers.attrib['authfilenumber']
				else:
					instance['source'] = ''
					instance['authfilenumber'] = ''
				creatorAPs[pers.text] = instance	
	# If the creator is tagged as <corpname>
	if len(creator_cb) > 0:
		for cb in creator_cb:
			if cb.text in creatorAPs:
				creatorAPs[cb.text]['counter'] += 1
				if 'source' in cb.attrib:
					if len(creatorAPs[cb.text]['source']) == 0:
						creatorAPs[cb.text]['source'] = cb.attrib['source']
						creatorAPs[cb.text]['authfilenumber'] = cb.attrib['authfilenumber']
			else:
				instance = {}
				instance['text'] = cb.text
				instance['counter'] = 1
				if 'source' in cb.attrib:
					instance['source'] = cb.attrib['source']
					instance['authfilenumber'] = cb.attrib['authfilenumber']
				else:
					instance['source'] = ''
					instance['authfilenumber'] = ''
				creatorAPs[cb.text] = instance	
	# If the creator is tagged as <name>
	if len(creator_name) > 0:
		for name in creator_name:
			if name.text in creatorAPs:
				creatorAPs[name.text]['counter'] += 1
				if 'source' in name.attrib:
					if len(creatorAPs[name.text]['source']) == 0:
						creatorAPs[name.text]['source'] = name.attrib['source']
						creatorAPs[name.text]['authfilenumber'] = name.attrib['authfilenumber']
			else:
				instance = {}
				instance['text'] = name.text
				instance['counter'] = 1
				if 'source' in name.attrib:
					instance['source'] = name.attrib['source']
					instance['authfilenumber'] = name.attrib['authfilenumber']
				else:
					instance['source'] = ''
					instance['authfilenumber'] = ''
				creatorAPs[name.text] = instance	
	# If the creator is tagged as <famname>
	if len(creator_fam) > 0:
		for family in creator_fam:
			if family.text in creatorAPs:
				creatorAPs[family.text]['counter'] += 1
				if 'source' in family.attrib:
					if len(creatorAPs[family.text]['source']) == 0:
						creatorAPs[family.text]['source'] = family.attrib['source']
						creatorAPs[family.text]['authfilenumber'] = family.attrib['authfilenumber']
			else:
				instance = {}
				instance['text'] = family.text
				instance['counter'] = 1
				if 'source' in family.attrib:
					instance['source'] = family.attrib['source']
					instance['authfilenumber'] = family.attrib['authfilenumber']
				else:
					instance['source'] = ''
					instance['authfilenumber'] = ''
				creatorAPs[family.text] = instance
	# If the creator is not tagged, we take the text
	if len(creator_pers) == 0 and len(creator_cb) == 0 and len(creator_name) == 0 and len(creator_fam) == 0:
		if creator.text in creatorAPs:
			creatorAPs[creator.text]['counter'] += 1
			if 'source' in creator.attrib:
				if len(creatorAPs[creator.text]['source']) == 0:
					creatorAPs[creator.text]['source'] = creator.attrib['source']
					creatorAPs[creator.text]['authfilenumber'] = creator.attrib['authfilenumber']
		else:
			instance = {}
			instance['text'] = creator.text
			instance['counter'] = 1
			if 'source' in creator.attrib:
				instance['source'] = creator.attrib['source']
				instance['authfilenumber'] = creator.attrib['authfilenumber']
			else:
				instance['source'] = ''
				instance['authfilenumber'] = ''
			creatorAPs[creator.text] = instance




# Finally we create a CSV table for each access point type
table_subjects = folder + '_subjects.csv'
table_places = folder + '_places.csv'
table_cbs = folder + '_cbs.csv'
table_person = folder + '_personalities.csv'
table_creators = folder + '_creators.csv'

with open (table_subjects, 'w') as csvtable:
	fields=['Text', 'Source', 'AuthFileNr', 'Frequency']
	writer = csv.DictWriter(csvtable, fieldnames=fields)
	writer.writeheader()
	for item in subjectAPs:
		writer.writerow({'Text':subjectAPs[item]['text'], 'Source':subjectAPs[item]['source'], 'AuthFileNr':subjectAPs[item]['authfilenumber'], 'Frequency':subjectAPs[item]['counter']})

with open (table_places, 'w') as csvtable:
	fields=['Text', 'Source', 'AuthFileNr', 'Frequency']
	writer = csv.DictWriter(csvtable, fieldnames=fields)
	writer.writeheader()
	for item in placeAPs:
		writer.writerow({'Text':placeAPs[item]['text'], 'Source':placeAPs[item]['source'], 'AuthFileNr':placeAPs[item]['authfilenumber'], 'Frequency':placeAPs[item]['counter']})

with open (table_cbs, 'w') as csvtable:
	fields=['Text', 'Source', 'AuthFileNr', 'Frequency']
	writer = csv.DictWriter(csvtable, fieldnames=fields)
	writer.writeheader()
	for item in cbAPs:
		writer.writerow({'Text':cbAPs[item]['text'], 'Source':cbAPs[item]['source'], 'AuthFileNr':cbAPs[item]['authfilenumber'], 'Frequency':cbAPs[item]['counter']})

with open (table_person, 'w') as csvtable:
	fields=['Text', 'Source', 'AuthFileNr', 'Frequency']
	writer = csv.DictWriter(csvtable, fieldnames=fields)
	writer.writeheader()
	for item in personAPs:
		writer.writerow({'Text':personAPs[item]['text'], 'Source':personAPs[item]['source'], 'AuthFileNr':personAPs[item]['authfilenumber'], 'Frequency':personAPs[item]['counter']})


with open (table_creators, 'w') as csvtable:
	fields=['Text', 'Source', 'AuthFileNr', 'Frequency']
	writer = csv.DictWriter(csvtable, fieldnames=fields)
	writer.writeheader()
	for item in creatorAPs:
		writer.writerow({'Text':creatorAPs[item]['text'], 'Source':creatorAPs[item]['source'], 'AuthFileNr':creatorAPs[item]['authfilenumber'], 'Frequency':creatorAPs[item]['counter']})































