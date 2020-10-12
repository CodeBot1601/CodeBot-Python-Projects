import requests

def corona_cases(name):
 url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"
 name = name.lower()
 name = name.capitalize()
 querystring = {"country":"{}".format(name)}

 headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "1c110f3091msha3f81899852d215p1e90c3jsn8f5e0e42572e"
    }

 response = requests.request("GET", url, headers=headers, params=querystring)
 x = str(response.content).replace("false",'2')
 x = eval(x[2:len(x)-1])
 x = eval(str(x["data"]))
 total = x['confirmed']
 recovered = x['recovered']
 death = x['deaths']
 return total,recovered,death
