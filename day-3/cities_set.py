raw_cities =["Naihati","Durgapur","Kolkata","Naihati","Durgapur","Shiliguri"]
cities_set =set(raw_cities)
print(cities_set)  # the city list has transfered to set and the duplicte cities are gone too
print(len(cities_set))    # gonna show the length of the set; and it supoose to be 4
cities_set.add("Asansole")  #it will add Asansole to the set
cities_set.discard("Kolkata") # it will remove kolkata from the set
cities_set.discard("Pune") #as we dont have any pune in  our set it will simply just ignore it without showing any error
print(cities_set)