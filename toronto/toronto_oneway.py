"""
Translation rules for City of Toronto Open Data, Oneway Streets.
http://opendata.toronto.ca/gcc/oneways_wgs84.zip

Copyright 2015 Andrew MacKinnon, 2011 Paul Norman.

WORK IN PROGRESS - DO NOT USE

"""

def translateName(rawname):
	suffixlookup = {}
	suffixlookup.update({'Ave':'Avenue'})
	suffixlookup.update({'Bdge':'Bridge'})
	suffixlookup.update({'Blvd':'Boulevard'})
	suffixlookup.update({'Crcl':'Circle'})
	suffixlookup.update({'Crt':'Court'})
	suffixlookup.update({'Crct':'Circuit'})
	suffixlookup.update({'Cres':'Crescent'})
	suffixlookup.update({'Cs':'Close'})
	suffixlookup.update({'Dr':'Drive'})
	suffixlookup.update({'Xwy':'Expressway'})
	suffixlookup.update({'Gdn':'Garden'})
	suffixlookup.update({'Gdns':'Gardens'})
	suffixlookup.update({'Gt':'Gate'})
	suffixlookup.update({'Grn':'Green'})
	suffixlookup.update({'Grv':'Grove'})
	suffixlookup.update({'Hts':'Heights'})
	suffixlookup.update({'Hwy':'Hwy'})
	suffixlookup.update({'Hill':'Hill'})
	suffixlookup.update({'Lane':'Lane'})
	suffixlookup.update({'Lwn':'Lawn'})
	suffixlookup.update({'Line':'Line'})
	suffixlookup.update({'Mews':'Mews'})
	suffixlookup.update({'Pk':'Park'})
	suffixlookup.update({'Pkwy':'Parkway'})
	suffixlookup.update({'Path':'Path'})
	suffixlookup.update({'Ptwy':'Pathway'})
	suffixlookup.update({'Pl':'Place'})
	suffixlookup.update({'Prom':'Promenade'})
	suffixlookup.update({'Ramp':'Ramp'})
	suffixlookup.update({'Rd':'Road'})
	suffixlookup.update({'Rdwy':'Roadway'})
	suffixlookup.update({'Sq':'Square'})
	suffixlookup.update({'St':'Street'})
	suffixlookup.update({'Ter':'Terrace'})
	suffixlookup.update({'Trl':'Trail'})
	suffixlookup.update({'View':'View'})
	suffixlookup.update({'Walk':'Walk'})
	suffixlookup.update({'Way':'Way'})
	suffixlookup.update({'Wds':'Woods'})

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

	if attrs['FCODE'] and attrs['FCODE'] == "201100":
		tags.update({'highway':'motorway'})
	elif attrs['FCODE'] and attrs['FCODE'] == "201101":
		tags.update({'highway':'motorway_link'})
	elif attrs['FCODE'] and attrs['FCODE'] == "201200":
		tags.update({'highway':'secondary'})
	elif attrs['FCODE'] and attrs['FCODE'] == "201201":
		tags.update({'highway':'secondary_link'})
	elif attrs['FCODE'] and attrs['FCODE'] == "201300":
		tags.update({'highway':'tertiary'})
	elif attrs['FCODE'] and attrs['FCODE'] == "201301":
		tags.update({'highway':'tertiary_link'})
	elif attrs['FCODE'] and attrs['FCODE'] == "201400":
		tags.update({'highway':'tertiary'})
	elif attrs['FCODE'] and attrs['FCODE'] == "201401":
		tags.update({'highway':'tertiary_link'})
	elif attrs['FCODE'] and attrs['FCODE'] == "201500":
		tags.update({'highway':'residential'})
	elif attrs['FCODE'] and attrs['FCODE'] == "201600":
		tags.update({'highway':'unclassified'})
	elif attrs['FCODE'] and attrs['FCODE'] == "201601":
		tags.update({'highway':'unclassified'})
	elif attrs['FCODE'] and attrs['FCODE'] == "202001":
		tags.update({'railway':'rail'})
	elif attrs['FCODE'] and attrs['FCODE'] == "202002":
		tags.update({'railway':'rail'})
		tags.update({'service':'spur'})
	elif attrs['FCODE'] and attrs['FCODE'] == "202003":
		tags.update({'railway':'construction'})
	elif attrs['FCODE'] and attrs['FCODE'] == "203001":
		tags.update({'waterway':'river'})
	elif attrs['FCODE'] and attrs['FCODE'] == "203002":
		tags.update({'waterway':'stream'})
	elif attrs['FCODE'] and attrs['FCODE'] == "204001":
		tags.update({'highway':'path'})
	elif attrs['FCODE'] and attrs['FCODE'] == "204002":
		tags.update({'highway':'footway'})
	elif attrs['FCODE'] and attrs['FCODE'] == "205001":
		tags.update({'power':'line'})
	elif attrs['FCODE'] and attrs['FCODE'] == "206001":
		tags.update({'natural':'coastline'})
	elif attrs['FCODE'] and attrs['FCODE'] == "206002":
		tags.update({'natural':'coastline'})
	else:
		tags.update({'highway':'road'})
	if 'FCODE' in attrs:
		tags.update({'opendata:type': attrs['FCODE'].strip(' ')})
	if 'ONE_WAY_DI' in attrs:
		tags.update({'oneway': attrs['ONE_WAY_DI'.strip(' ')})

	return tags
