item_list=["ipad","iphone","macbook","imac"]
item_price=[90000,45000,129000,299000]
product=input("Enter the product you want:")
for index,item in enumerate(item_list):
    if item==product:
        print(f"{index}. {item} is in stock and it costs {item_price[index]}.")
        break
else:
        print("Sorry, the item you searched for is not in inventory.")
        