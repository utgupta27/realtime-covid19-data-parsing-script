import firebase_admin
import json
import requests
from firebase_admin import credentials
from firebase_admin import firestore

url = 'https://api.covid19india.org/v4/min/data.min.json'
r = requests.get(url, allow_redirects=True)
open('data.min.json', 'wb').write(r.content)

file = open('data.min.json')
data = json.load(file)


url1 = 'https://api.covid19india.org/v4/min/timeseries.min.json'
r1 = requests.get(url1, allow_redirects=True)
open('timeseries.min.json', 'wb').write(r1.content)

file1 = open('timeseries.min.json')
data1 = json.load(file1)

cred = credentials.Certificate('learningfirebase-7cd69-firebase-adminsdk-fsg0o-75b0f8a9d5.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


# # For Total cases Overview of india
countryData = data['TT']['total']
data_ref = db.collection(u'countryWiseRecord').document(u'TT')
data_ref.set(countryData)

# # data_ref = db.collection(u'covidData').document(u'TT')
# # a = data_ref.get()
# # print(a.to_dict())


# # For State & district wise total cases
stateCode = ["AN","AP","AR","AS","BR","CH","CT","DN","DL","GA","GJ","HR","HP","JK","JH","KA","KL","LA","LD","MP","MH","MN","ML","MZ","NL","OR","PY","PB","RJ","SK","TN","TG","TR","UP","UT","WB"]
for i in stateCode:
    data_ref = db.collection(u'stateWiseRecord').document(i)
    data_ref.set(data[i]['total'])
    for j in data[i]['districts']:
        data_ref1 = db.collection(u'stateWiseRecord').document(i).collection('districts').document(j)
        data_ref1.set(data[i]['districts'][j]['total'])

# Country Time Series
TTconfirmed = []
TTdeceased = []
TTrecovered = []
TTtested = []
TTvaccinated1 = []
TTvaccinated2 = []
for i in data1['TT']['dates']:
    try:
        TTconfirmed.append(data1['TT']['dates'][i]['total']['confirmed'])
    except:
        TTconfirmed.append(0)
    try:
        TTdeceased.append(data1['TT']['dates'][i]['total']['deceased'])
    except:
        TTdeceased.append(0)
    try:
        TTrecovered.append(data1['TT']['dates'][i]['total']['recovered'])
    except:
        TTrecovered.append(0)
    try:
        TTtested.append(data1['TT']['dates'][i]['total']['tested'])
    except:
        TTtested.append(0)
    try:
        TTvaccinated1.append(data1['TT']['dates'][i]['total']['vaccinated1'])
    except:
        TTvaccinated1.append(0)
    try:
        TTvaccinated2.append(data1['TT']['dates'][i]['total']['vaccinated2'])
    except:
        TTvaccinated2.append(0)
data_ref = db.collection(u'countryTimeSeries').document(u'TT')
data_ref.set({
    "confirmed" : TTconfirmed,
    "deceased" : TTdeceased,
    "recovered" : TTrecovered,
    "tested" : TTtested,
    "vaccinated1" : TTvaccinated1,
    "vaccinated2" : TTvaccinated2
})



# State Time Sries
for i in stateCode:
    confirmed = []
    deceased = []
    recovered = []
    tested = []
    vaccinated1 = []
    vaccinated2 = []
    for j in data1[i]['dates']:
        try:
            confirmed.append(data1[i]['dates'][j]['total']['confirmed'])
        except:
            confirmed.append(0)
        try:
            deceased.append(data1[i]['dates'][j]['total']['deceased'])
        except:
            deceased.append(0)
        try:
            recovered.append(data1[i]['dates'][j]['total']['recovered'])
        except:
            recovered.append(0)
        try:
            tested.append(data1[i]['dates'][j]['total']['tested'])
        except:
            tested.append(0)
        try:
            vaccinated1.append(data1[i]['dates'][j]['total']['vaccinated1'])
        except:
            vaccinated1.append(0)
        try:
            vaccinated2.append(data1[i]['dates'][j]['total']['vaccinated2'])
        except:
            vaccinated2.append(0)
    data_ref = db.collection(u'stateTimeSeries').document(i)
    data_ref.set({
        "confirmed" : confirmed,
        "deceased" : deceased,
        "recovered" : recovered,
        "tested" : tested,
        "vaccinated1" : vaccinated1,
        "vaccinated2" : vaccinated2
    })
