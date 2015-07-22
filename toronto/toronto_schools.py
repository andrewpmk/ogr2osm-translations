"""
Translation rules for City of Toronto Open Data, Schools.
http://opendata.toronto.ca/gcc/school_tdsb_wgs84.zip
Copyright 2015 Andrew MacKinnon, 2011 Paul Norman.
WORK IN PROGRESS - DO NOT USE
"""

def filterTags(attrs):
	if not attrs: return

	tags = {}
	
	#Add the source
	tags.update({'source':'City of Toronto Open Data'})
	#Add operator
	#tags.update({'operator':'Toronto District School Board'})
	#Add amenity=school
	tags.update({'amenity':'school'})
	#Add addr:province and addr:country
	tags.update({'addr:province':'ON'})
	tags.update({'addr:country':'CA'})
	#automagically convert names
	if attrs['SCHNAME']:
		tags.update({'name':attrs['SCHNAME'].strip(' ')})
	if attrs['ADDRESS']:
		address=attrs['ADDRESS'].split()
		housenumber=address.pop(0)
		street=" ".join(address)
  		tags.update({'addr:housenumber':housenumber.strip(' ')})
  		tags.update({'addr:street':street.strip(' ')})
	if attrs['MUN']:
		tags.update({'addr:city':attrs['MUN'].strip(' ')})
	if attrs['POSTALCODE']:
		tags.update({'addr:postcode':attrs['POSTALCODE'].strip(' ')})
	return tags
