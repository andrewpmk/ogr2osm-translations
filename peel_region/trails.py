"""
Translation rules for Peel Region Open Data - Roads.

Copyright 2015 Andrew MacKinnon, 2011 Paul Norman.

EPSG:26917

WORK IN PROGRESS - DO NOT USE
"""

def filterTags(attrs):
	if not attrs: return

	tags = {}
	
	#Add the source
	tags.update({'source':'Peel Open Data'})
	#automagically convert names
	if attrs['Name']:
		tags.update({'name':attrs['Name'].strip(' ')})
	if attrs['Class'] and attrs['Class'] == "Paved Multi-use Trail":
		tags.update({'highway':'path'})
	elif attrs['Class'] and attrs['Class'] == "Unpaved Multi-use Trail":
		tags.update({'highway':'path'})
	elif attrs['Class'] and attrs['Class'] == "Hiking Trail":
		tags.update({'highway':'footway'})
		tags.update({'sac_scale':'hiking'})
	elif attrs['Class'] and attrs['Class'] == "Unmarked Dirt Trail":
		tags.update({'highway':'footway'})
		tags.update({'surface':'dirt'})
	elif attrs['Class'] and attrs['Class'] == "Bicycle Lane":
		tags.update({'highway':'road'})
		tags.update({'cycleway':'lane'})
	elif attrs['Class'] and attrs['Class'] == "Marked On Road Bicycle Route":
		tags.update({'highway':'road'})
		tags.update({'lcn'='yes'})
	elif attrs['Class'] and attrs['Class'] == "On Road Connection":
		tags.update({'highway':'road'})
		tags.update({'bicycle'='yes'})
	else:
		tags.update({'highway':'road'})
	if 'ROAD_CLASS' in attrs:
		tags.update({'opendata:type': attrs['ROAD_CLASS'].strip(' ')})
  if attrs['BruceTrail']:
    tags.update({'bruce_trail': 'yes'})
  if attrs['TransCanTrail']:
    tags.update({'trans_canada_trail': 'yes'})

	return tags
