
contents = []

categories=['WARRANTS',
 'GAMBLING',
 'LARCENY/THEFT',
 'VANDALISM',
 'BURGLARY',
 'TRESPASS',
 'STOLEN PROPERTY',
 'FRAUD',
 'FAMILY OFFENSES',
 'BRIBERY',
 'RUNAWAY',
 'VEHICLE THEFT',
 'DRIVING UNDER THE INFLUENCE',
 'RECOVERED VEHICLE',
 'SEX OFFENSES FORCIBLE',
 'SEX OFFENSES NON FORCIBLE',
 'PORNOGRAPHY/OBSCENE MAT',
 'PROSTITUTION',
 'ROBBERY',
 'ASSAULT',
 'TREA',
 'EMBEZZLEMENT'
 'ARSON',
 'KIDNAPPING',
 'FORGERY/COUNTERFEITING',
 'DRUG/NARCOTIC',
 'EXTORTION',
 'SECONDARY CODES',
 'MISSING PERSON',
 'DISORDERLY CONDUCT',
 'LIQUOR LAWS',
 'SUICIDE',
 'LOITERING',
 'SUSPICIOUS OCC',
 'BAD CHECKS',
 'DRUNKENNESS',
 'WEAPON LAWS',
 'OTHER OFFENSES',
 'NON-CRIMINAL']

major_cats=['Minor Crimes','Major Crimes',"Vehicle Infractions",'Sex Offenses','Others']
major_cat_ar=[0,0,0,0]

for x in contents:
	if x in categories[0:11]:
		major_cat_ar[0]+=1
	if x in categories[11:14]:
		major_cat_ar[1]+=1
	if x in categories[14:18]:
		major_cat_ar[2]+=1
	if x in categories[18:27]:
		major_cat_ar[3]+=1
	if x in categories[27:39]:
		major_cat_ar[4]+=1


###Set category score###
major_cat_score=[5,10,7,9,3]

obtained score=[a*b for a,b in zip(major_cat_ar,major_cat_score)]

