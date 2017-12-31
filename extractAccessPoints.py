import xml.etree.ElementTree as ET
from os import listdir
import sys

# Here iterate through the list of XML files

folder = sys.argv[1]

filenames = listdir(folder)
subjectAPs = {}
placeAPs = {}
cbAPs = {}
personAPs = {}

subject_objects = []
place_objects = []
cb_objects = []
person_objects = []


for filename in filenames:
	eadfile = folder + '/' + filename
	tree = ET.parse(eadfile)
	root = tree.getroot()
	subjects = root.findall(".//{urn:isbn:1-931666-22-9}subject")
	subject_objects = subject_objects + subjects
	places = root.findall(".//{urn:isbn:1-931666-22-9}geogname")
	place_objects = place_objects + places
	corporate_bodies = root.findall(".//{urn:isbn:1-931666-22-9}corpname")
	cb_objects = cb_objects + corporate_bodies
	people = root.findall(".//{urn:isbn:1-931666-22-9}persname")
	person_objects = person_objects + people


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

print (personAPs)

