raw_fruits=["Apple" , "apple" , "APPLE" , "Banana" , "banana"]
hootie_frutie= set(raw_fruits) #change the list raw_fruites into set as qs asked for
print(hootie_frutie) # all of the words going to get print out as the  case is diffrent so their has value is also diffrent and they becomes unique on their own

clean_fruits={item.strip().lower() for item in hootie_frutie}  #stripping out whitespaces and lowecasing the uppercases
print(clean_fruits)  #only banana, apple going to get printed as after lowercasing everything only this two becomes unique 