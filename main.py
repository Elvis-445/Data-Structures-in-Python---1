cars=["BMW","Audi","Ferarri","Lamborghini","Porsche","Maserati","Toyota"]
#length of list
print("The length is: ",len(cars))
#accessing the first element
print("The first element is: ",cars[0])
#sort
cars.sort()
print("Sorted list is: ",cars)
#reverse
cars.reverse()
print("Reversed list is ",cars)
#slice
cars=cars[:5]
print("Sliced list: ",cars)
#clearlist
cars.clear()
print("Cleared List: ",cars)
cars.append("Subaru")
print("Append: ",cars)