"""
Translation rules for City of Toronto Open Data, 3D Buildings.
http://opendata.toronto.ca/gcc/ContextMassing_wgs84.zip

Copyright 2015 Andrew MacKinnon, 2011 Paul Norman.

WORK IN PROGRESS - DO NOT USE

"""

def filterTags(attrs):
	if not attrs: return

	tags = {}
	
	#Add the source
	tags.update({'source':'City of Toronto Open Data'})
	#Add building=yes
	tags.update({'leisure':'park'})
	#Add building height
	if attrs['EleZ']:
	  tags.update(attrs['EleZ'].strip(' '))

	return tags
