marketplace = {
        "Zudio":
              {"top":
                  { 
                      "price":"200",
                    "stock":"In Stock"
                   },
                "jeans":
                   {
                       "price":"799",
                        "stock":"Out of Stock"
                        },
                },
        "Trends":
        { "Croptop":
                 {
                     "price":"599",
                     "stock":"In Stock"
                     },
            "Skirt":
                {
                    "price":"899",
                     "stock":"In stock"
                     }}

}

user_store = input("Enter the store name:")
store = marketplace.get(user_store)
if store == None:
    print("Sorry the store you entered is not found.")
else:
    print(f"The store{user_store} is found and here are the inventory: {store}")
    user_update = input("Enter what you want to update (price/stock): ")
    product = input("Enter the product you want to update:")
    if user_update == "price":
        marketplace[user_store][product]["price"]= int(input("Enter the price:"))
    else:
        marketplace[user_store][product]["stock"]= input("Enter stock:")
    for  store, inventory in marketplace.items():
        print(f"store:{store}")
        print(f"Inventory:{inventory}")