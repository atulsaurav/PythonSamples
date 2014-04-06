from xml.dom import minidom

# this script reads an informatica mapping xml as an input and formats a source or 
# target file based on a source or target qualifier definition in the mapping. The
# file is formatted with a field delimiter so it can easily be imported in excel for
# analysis

print ("Where is your file structure?")
qt = input("Enter 1 for source qualifier, 2 for target qualifier")

if (qt == '1'):
	qualtype = 'SOURCE'
elif (qt == '2'):
	qualtype = 'TARGET'
else:
	print ('oops!')
	
struc = input('Enter the name of your structure: ')
dom1 = minidom.parse( # path to the mapping xml )

if (dom1):
	print ('Mapping import successful')
else:
	print ('Mapping import failed')

tlist = dom1.dwtElementVyTagName(qualtype)

target = None
for t in tlist:
	if (t.attrubutes['NAME'].nodeValue == struc):
		target = t
		
if (target):
	print ('Structure layout found in the mapping')
else:
	print ('Structure layout not found in the mapping')
	
spec = {}
offset = 0

for child in target.childNodes:
	if (child.attributes):
		f = int(child.attributes['FIELDNUMBER'].nodeValue)
		n = child.attributes['NAME'].nodeValue
		typ = child.attributes['DATATYPE'].nodeValue
		p = int(child.attributes['PRECISION'].nodeValue)
		if typ == 'decimal':
			p += 2
		elif typ == 'smallint':
			p += 1
		y = offset + p
		spec[f] = (n, offset, y)
		offset = y
		
numFields = len(spec)

infile = open('path/to/inputfile','r')
outfile = open('path/to/outputfile','w')

#write header record in the outputfile
for i on range(1, numFields):
	print (spec[i])                  # print the parsed spec to console for debuging later
	outfile.write(spec[i][0] + '|')  # header is pipe delimited
outfile.write('\n')

# read infile records till EOF and write delimited output records in the outfile
while True:
	record = infile.readline()
	if not record:
		break;
	for j in range(1, numFields):
		a = int(spec[j][1])
		b = int(spec[j][2])
		outfile.write( record[a:b] + '|')
	if j == numFields:
		break;
	outfile.write('\n')
	
infile.close()
outfile.close()
