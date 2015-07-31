import urllib.request, json
url = 'http://www.citibikenyc.com/stations/json'
response = urllib.request.urlopen(url)
str_response = response.readall().decode('utf-8')
citibike_json = json.loads(str_response)

def heatmap_data():
    data = []
    for station in citibike_json["stationBeanList"]:
        if station["totalDocks"] != 0:
            #print("-----------STATION DATA-----------")
            #print("%d docks at station %d (%s)" % (station["availableDocks"], station["id"], station["stationName"]))
            density = (1-station["availableDocks"]/station["totalDocks"])
            #print("Station density: %.2f" % (density))

            #print("Saving to heatmap_data...")
            data.append({
                'latitude' : station['latitude'],
                'longitude' : station['longitude'],
                'density' : density
            })
            #print("...done")
            #print("\n")

    return json.dumps(data)
