import json
import requests

url = 'https://api.covid19india.org/v4/min/timeseries.min.json'
r = requests.get(url, allow_redirects=True)
open('timeseries.min.json', 'wb').write(r.content)

file = open('timeseries.min.json')
data = json.load(file)


TTconfirmed = []
TTdeceased = []
TTrecovered = []
TTtested = []
TTvaccinated1 = []
TTvaccinated2 = []
for i in data['TT']['dates']:
    try:
        TTconfirmed.append(data['TT']['dates'][i]['total']['confirmed'])
    except:
        TTconfirmed.append(0)
    try:
        TTdeceased.append(data['TT']['dates'][i]['total']['deceased'])
    except:
        TTdeceased.append(0)
    try:
        TTrecovered.append(data['TT']['dates'][i]['total']['recovered'])
    except:
        TTrecovered.append(0)
    try:
        TTtested.append(data['TT']['dates'][i]['total']['tested'])
    except:
        TTtested.append(0)
    try:
        TTvaccinated1.append(data['TT']['dates'][i]['total']['vaccinated1'])
    except:
        TTvaccinated1.append(0)
    try:
        TTvaccinated2.append(data['TT']['dates'][i]['total']['vaccinated2'])
    except:
        TTvaccinated2.append(0)
countryTimeSeries = [TTconfirmed,TTdeceased,TTrecovered,TTtested,TTvaccinated1,TTvaccinated2]
print(countryTimeSeries)


stateCode = ["AN","AP","AR","AS","BR","CH","CT","DN","DL","GA","GJ","HR","HP","JK","JH","KA","KL","LA","LD","MP","MH","MN","ML","MZ","NL","OR","PY","PB","RJ","SK","TN","TG","TR","UP","UT","WB"]

allStateTimeSeries = []
for i in stateCode:
    confirmed = []
    deceased = []
    recovered = []
    tested = []
    vaccinated1 = []
    vaccinated2 = []
    for j in data[i]['dates']:
        try:
            confirmed.append(data[i]['dates'][j]['total']['confirmed'])
        except:
            confirmed.append(0)
        try:
            deceased.append(data[i]['dates'][j]['total']['deceased'])
        except:
            deceased.append(0)
        try:
            recovered.append(data[i]['dates'][j]['total']['recovered'])
        except:
            recovered.append(0)
        try:
            tested.append(data[i]['dates'][j]['total']['tested'])
        except:
            tested.append(0)
        try:
            vaccinated1.append(data[i]['dates'][j]['total']['vaccinated1'])
        except:
            vaccinated1.append(0)
        try:
            vaccinated2.append(data[i]['dates'][j]['total']['vaccinated2'])
        except:
            vaccinated2.append(0)
    allStateTimeSeries.append([confirmed,deceased,recovered,tested,vaccinated1,vaccinated2])

print(allStateTimeSeries)

