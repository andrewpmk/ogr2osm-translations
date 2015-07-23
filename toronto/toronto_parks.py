"""
Translation rules for City of Toronto Open Data, Parks.
http://opendata.toronto.ca/gcc/city_green_space_wgs84.zip

Copyright 2015 Andrew MacKinnon, 2011 Paul Norman.

WORK IN PROGRESS - DO NOT USE

"""

def translateName(rawname):
	newName = rawname.title()
	return newName.strip()

def filterTags(attrs):
	if not attrs: return

	tags = {}
	
	#Add the source
	tags.update({'source':'City of Toronto Open Data'})
	#Add leisure=park
	tags.update({'leisure':'park'})
	#automagically convert names
	if attrs['NAME']:
		tags.update({'name':translateName(attrs['NAME'].strip(' '))})

	return tags
