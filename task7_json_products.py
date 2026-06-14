import json

product = {

    "name" : "Laptop",
    "price" : 70000,
    "quantity" : 5

}

with open("products.json","w") as file:

    json.dump(product,file,indent=4)

with open("products.json","r") as file:

    data = json.load(file)

print("\nProduct Details")
print("-----------------------------")
print("Name\t\tPrice\t\tQuantity")
print("-----------------------------")
print(data["name"],"\t",data["price"],"\t\t",data["quantity"])