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
major_cat_ar=[0,0,0,0,0]

###Set category score###
major_cat_score=[5,10,7,9,3]

def total_score(crime_committed):
    for x in categories:
        if crime_committed.lower() == x.lower():
            if x in categories[0:11]:
                return 5
            elif x in categories[11:14]:
                return 10
            elif x in categories[14:18]:
                return 7
            elif x in categories[18:27]:
                return 9
            elif x in categories[27:39]:
                return 3


def minor_crimes_score(crime_committed):
    for x in categories:
        if crime_committed.lower() == x.lower():
            if x in categories[0:11]:
                return 5
            else:
                return 0

def major_crimes_score(crime_committed):
    for x in categories:
        if crime_committed.lower() == x.lower():
            if x in categories[11:14]:
                return 10
            else:
                return 0

def vehicle_infractions_score(crime_committed):
    for x in categories:
        if crime_committed.lower() == x.lower():
            if x in categories[14:18]:
                return 7
            else:
                return 0

def sex_offenses_score(crime_committed):
    for x in categories:
        if crime_committed.lower() == x.lower():
            if x in categories[18:27]:
                return 9
            else:
                return 0

def other_crimes_score(crime_committed):
    for x in categories:
        if crime_committed.lower() == x.lower():
            if x in categories[27:39]:
                return 3
            else:
                return 0

