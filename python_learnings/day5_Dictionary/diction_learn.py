game_types={"tpp":"bgmi","fpp":"cod","racing":"race3d"}

print(game_types["fpp"])
print(game_types.get("tpp"))


game_types["fpp"]="valorant"  #to change values
print(game_types)    


for i in game_types:
    print(i,game_types[i])


for key,value in game_types.items():
    print(key,value)


if "tpp" in game_types:
    print(game_types["tpp"])


game_types["arcade"]="jungle mission"  #to add key-val in existing dictionary
print(game_types)

game_types.pop("fpp")   #to remove key:value 
print(game_types)


del game_types["arcade"]   #deletes reference from memory 
print(game_types)


copy_game_types=game_types
print(copy_game_types)


copy_game_types["new"]="fifa"
print(copy_game_types) #changing one cause change in other also
print(game_types)#cause both are reffering to same point


#so if you want to copy , copy like this
last_game_types=copy_game_types.copy()
last_game_types["ps4"]="Fifa"
print(last_game_types)  #only added on one place cause we used copy method
print(copy_game_types)  #that's why new referrence point created

mobile_shop={"android":{"samsung":"top","redmi":"bottom"},"IOS":{"16":"top","11":"bottom"}}

print(mobile_shop)
print(mobile_shop["android"])
print(mobile_shop["android"]["samsung"])  #nested dictionaries


squared_no={x:x**2 for x in range(6)}
print(squared_no)