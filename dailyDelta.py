import json
import requests

# url = 'https://api.covid19india.org/v4/min/data.min.json'
# r = requests.get(url, allow_redirects=True)
# open('data.min.json', 'wb').write(r.content)


file = open('data.min.json')
data = json.load(file)

# For TotaL cases Overview of india per day
# countryDelta = data['TT']['delta']
# print(countryDelta)
# print('*'*100)




confirmed = []
deceased = []
recovered = []
tested = []
vaccinated1 = []
vaccinated2 = []
# For State Wise Details per day
stateCode = ["AN","AP","AR","AS","BR","CH","CT","DN","DL","GA","GJ","HR","HP","JK","JH","KA","KL","LA","LD","MP","MH","MN","ML","MZ","NL","OR","PY","PB","RJ","SK","TN","TG","TR","UP","UT","WB"]

for i in stateCode:
    try:
        confirmed.append([i,data[i]['delta']['confirmed']])
    except:
        confirmed.append(0)
        pass
print(confirmed)
print('*'*100)

# District Wise details:
# distData = []
# for i in stateCode:
#     for j in data[i]['districts']:
#         try:
#             distData.append([j,data[i]['districts'][j]['delta']])
#         except:
#             pass
# print(distData)
# print('*'*100)


