"""
Translation rules for York Region Open Data, Roads.

Copyright 2015 Andrew MacKinnon, 2011 Paul Norman.

Projection is EPSG:26917

TODO:
Remove Unopened Road Allowance
Remove Proposed Road (maybe)

WORK IN PROGRESS - DO NOT USE

"""

def filterTags(attrs):
	if not attrs: return

	tags = {}
	
	#Add the source
	tags.update({'source':'York Region Open Data'})
	#automagically convert names
	if attrs['FULL_NAME']:
		tags.update({'name':attrs['FULL_NAME'].strip(' ')})
	if attrs['ROAD_CLASS'] and attrs['ROAD_CLASS'] == "Freeway":
		tags.update({'highway':'motorway'})
	elif attrs['ROAD_CLASS'] and attrs['ROAD_CLASS'] == "Interchange-Freeway":
		tags.update({'highway':'motorway_link'})
	elif attrs['ROAD_CLASS'] and attrs['ROAD_CLASS'] == "Provincial Highway":
		tags.update({'highway':'primary'})
	elif attrs['ROAD_CLASS'] and attrs['ROAD_CLASS'] == "Urban Road":
		tags.update({'highway':'residential'})
	elif attrs['ROAD_CLASS'] and attrs['ROAD_CLASS'] == "Regional Road":
		tags.update({'highway':'secondary'})
	elif attrs['ROAD_CLASS'] and attrs['ROAD_CLASS'] == "Arterial Road":
		tags.update({'highway':'secondary'})
	elif attrs['ROAD_CLASS'] and attrs['ROAD_CLASS'] == "Interchange-Regional Road":
		tags.update({'highway':'secondary'})
	elif attrs['ROAD_CLASS'] and attrs['ROAD_CLASS'] == "Interchange-Urban Road":
		tags.update({'highway':'residential'})
	elif attrs['ROAD_CLASS'] and attrs['ROAD_CLASS'] == "Interchange-Prov Highway":
		tags.update({'highway':'secondary_link'})
	elif attrs['ROAD_CLASS'] and attrs['ROAD_CLASS'] == "Rural Road":
		tags.update({'highway':'unclassified'})
	elif attrs['ROAD_CLASS'] and attrs['ROAD_CLASS'] == "Proposed Road":
		tags.update({'highway':'proposed'})
	elif attrs['ROAD_CLASS'] and attrs['ROAD_CLASS'] == "Accessway":
		tags.update({'highway':'service'})
		tags.update({'service':'driveway'})
	elif attrs['ROAD_CLASS'] and attrs['ROAD_CLASS'] == "Laneway":
		tags.update({'highway':'service'})
		tags.update({'service':'alley'})
	elif attrs['ROAD_CLASS'] and attrs['ROAD_CLASS'] == "Private Road":
		tags.update({'highway':'service'})
		tags.update({'access':'private'})
	else:
		tags.update({'highway':'road'})
	if 'ROAD_NUMBE' in attrs:
		if attrs['ROAD_NUMBE']!='':
			tags.update({'ref': attrs['ROAD_NUMBE'].strip(' ')})
	if 'ROAD_CLASS' in attrs:
		tags.update({'opendata:type': attrs['ROAD_CLASS'].strip(' ')})
	if 'FLOW' in attrs:
		if attrs['FLOW'] == "OneWay":
			tags.update({'oneway': 'yes'})

	return tags
