"""
Translation rules for City of Toronto Open Data, Oneway Streets.
http://opendata.toronto.ca/gcc/oneways_wgs84.zip

Copyright 2015 Andrew MacKinnon, 2011 Paul Norman. 

"""

def translateName(rawname):
	suffixlookup = {}
	suffixlookup.update({'Ave':'Avenue'})
	suffixlookup.update({'Rd':'Road'})
	suffixlookup.update({'St':'Street'})
	suffixlookup.update({'Pl':'Place'})
	suffixlookup.update({'Cr':'Crescent'})
	suffixlookup.update({'Blvd':'Boulevard'})
	suffixlookup.update({'Dr':'Drive'})
	suffixlookup.update({'Lane':'Lane'})
	suffixlookup.update({'Crt':'Court'})
	suffixlookup.update({'Gr':'Grove'})
	suffixlookup.update({'Cl':'Close'})
	suffixlookup.update({'Rwy':'Railway'})
	suffixlookup.update({'Div':'Diversion'})
	suffixlookup.update({'Hwy':'Highway'})
	suffixlookup.update({'Hwy':'Highway'})

	suffixlookup.update({'E':'East'})
	suffixlookup.update({'S':'South'})
	suffixlookup.update({'N':'North'})
	suffixlookup.update({'W':'West'})
	
	newName = ''
	for partName in rawname.split():
		newName = newName + ' ' + suffixlookup.get(partName,partName)
	
	return newName.strip()



def filterTags(attrs):
	if not attrs: return

	tags = {}
	
	#Add the source
	tags.update({'source':'City of Toronto Open Data'})
	#automagically convert names
	if attrs['LF_NAME']:
		tags.update({'name':translateName(attrs['LF_NAME'].strip(' '))})

	if 'RC_TYPE2' in attrs:
		if attrs['RC_TYPE2'] == "Road" or attrs['RC_TYPE2'] == "Frontage Road":  #TYPE=0 or 1
			#some form of road	
			if attrs['STATUS'] and attrs['STATUS'] == "Unconstructed":
				tags.update({'highway':'proposed'})
			else:
				#a road that's been completed
				if attrs['STATUS'] and attrs['STATUS'] == "Closed to Traffic":
					tags.update({'access':'no'})
				if attrs['RD_CLASS'] and attrs['RD_CLASS'] == "Provincial Highway":
					tags.update({'highway':'primary'})
				elif attrs['RD_CLASS'] and attrs['RD_CLASS'] == "Arterial":
					tags.update({'highway':'secondary'})
				elif attrs['RD_CLASS'] and attrs['RD_CLASS'] == "Major Collector":
					tags.update({'highway':'tertiary'})
				elif attrs['RD_CLASS'] and attrs['RD_CLASS'] == "Local":
					tags.update({'highway':'residential'})
				elif attrs['RD_CLASS'] and attrs['RD_CLASS'] == "Translink":
					tags.update({'highway':'road'})
				else:
					tags.update({'highway':'road'})
		elif attrs['RC_TYPE2'] == "Highway Interchange": #type=1
			tags.update({'highway':'primary_link'})
		elif attrs['RC_TYPE2'] == "Street Lane" or attrs['RC_TYPE2'] == "Access Lane": #TYPE=3 or 4
			tags.update({'highway':'service'})
			tags.update({'service':'alley'})
		elif attrs['RC_TYPE2'] == "Railway": #type 5
			tags.update({'railway':'rail'})
		
	# Truck route information
	if 'ROUTE' in attrs:
		if attrs['ROUTE'] == "Dangerous Goods Routes":
			tags.update({'hazmat':'designated'})
			tags.update({'hgv':'designated'})
		if attrs['ROUTE'] == "Truck Routes":
			tags.update({'hgv':'designated'})				
		if attrs['ROUTE'] == "Truck Routes Restrictions":
			tags.update({'hgv':'no'})

	if 'GEODB_OID' in attrs:
		tags.update({'surrey:geodb_oid': attrs['GEODB_OID'].strip(' ')})
	
	

	return tags

