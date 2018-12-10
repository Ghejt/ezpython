def read_metar(file):
    lines = []
    with open(file, mode='r') as metar:
        for line in metar:
            line = line.split()
            lines.append(line)
    return lines
def parse_metar(metar):
    #TYPE
    if metar[0] == 'METAR':
        print("TYPE: Standard")
    elif metar[0] == 'SPECI':
        print('TYPE: Special')
    else:
        print("TYPE: Invalid")

    #ID (ezpz lol)
    print('ID: %s' %metar[1])

    #TIME
    time = metar[2]
    englishtime = int(time[2:6])
    if englishtime < 600:
        englishtime = str(englishtime + 1800).zfill(4)
    else:
        englishtime = str(englishtime - 600).zfill(4)
    print("TIME: %s UTC" %englishtime)

    #WIND
    windspeed = metar[3]
    windspeed = windspeed[3:5].strip("0")
    print("WIND: %s knots" %windspeed)
    
    #VIS
    miles = metar[4].strip('SM')
    print("VIS: %s miles" %miles)

    #WX
    intensity = {'-':'light','+':'heavy','VC':'vicinity'}
    descriptor = {'MI':'shallow','PR':'partial','BC':'patches','DR':'low drifting','BL':'blowing','SH':'showers','TS':'thunderstorm','FZ':'freezing'}
    precipitation = {'DZ':'Drizzle','RA':'Rain','SN':'Snow','SG':'Snow Grains','IC':'Ice Crystals','PL':'Ice Pellets','GR':'Hail','GS':'Small Hail and/or Snow Pellets','UP':'Unknown Precipitation'}
    obscuration = {'BR':'Mist','FG':'Fog','FU':'Smoke','VA':'Volcanic Ash','DU':'Widespread Dust','SA':'Sand','HZ':'Haze','PY':'Spray'}
    other = {'PO':'Well-Developed Dust/Sand Whirls','SQ':'Squalls','FC':'Funnel Cloud Tornado Waterspout','SS':'Sandstorm','SS':'Duststorm'}
    weather = ''
    if '0' in metar[5]:
        weather = 'None reported.'
    else:
        for key in intensity:
            if key in metar[5]:
                weather += intensity[key] + ' '
        for key in descriptor:
            if key in metar[5]:
                weather += descriptoy[key] + ' '
        for key in precipitation:
            if key in metar[5]:
                weather += precipitation[key] + ' '
        for key in obscuration:
            if key in metar[5]:
                weather += obscuration[key] + ' '
        for key in other:
            if key in metar[5]:
                weather += other[key] + ' '
    print('WX: %s' %weather)

    #SKY
    sky = {'FEW':'Few','SCT':'Scattered','BKN':'Broken','OVC':'Overcast','VV':'Clouds cannot be seen','NSC':'No significant cloud','CLR':'No Clouds','NCD':'Nil Cloud Detected','SKC':'No cloud/Sky clear'}
    significant_clouds = {'TCU':'Towering Cumulus','ACC':'Altocumulus Castellanus','CB':'Cumulonimbus or Shower/Thunderstorm'}
    conditions = ''
    for x in metar:
        feet = x[3:6].strip('0')
        feet = feet.ljust(4, '0')
        for key in sky:
            if key in x:
                conditions += ("%s at %s feet" %(sky[key], feet))
    print('SKY: %s' %conditions)
    
    #T/TD
    for x in metar:
        if '/' in x:
            temp = x[0:2]
            dew = x[3:5]
    print('T/TD: %sC, dew point %sC' %(temp, dew))
