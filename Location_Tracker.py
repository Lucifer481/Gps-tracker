import phonenumbers
import opencage
import folium
import pyfiglet


text = pyfiglet.figlet_format("Location Tracker")
print(text)
number = input("Enter the number with country code:")
print("Number details", number)


from phonenumbers import geocoder
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print (location)


from phonenumbers import carrier
service_number = phonenumbers.parse(number)
print(carrier.name_for_number(service_number, "en"))


from opencage.geocoder import OpenCageGeocode
key ='4b2b06c81da5475d9229d1528d8ebb6d'
geocoder = OpenCageGeocode(key)
query =str(location)
results = geocoder.geocode(query)
#print (results)

lat = results[0]['geometry']['lat']
lng =results[0]['geometry']['lng']
print (lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start= 9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("mylocation.html")
