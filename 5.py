list1 = ["lion", "monkey", "dog", "fish"]
tuple1 = ("lion", "monkey", "dog", "fish")
set1 = {"lion", "monkey", "dog", "fish"}
dict1 = {"lion": 4, "monkey": 2, "dog": 4, "fish": 2}

print("Length of list1:", len(list1))
print("Length of tuple1:", len(tuple1))
print("Length of set1:", len(set1))
print("Length of dict1:", len(dict1))

print("First element of list1:", list1[0])
print("First element of tuple1:", tuple1[0])

print("Value of 'lion' key in dict1:", dict1["lion"])

list1[1] = "rabbit"
print("Modified list1:", list1)

list1.append("monkey")
print("Modified list1:", list1)

list1.remove("rabbit")
print("Modified list1:", list1)

dict1["fish"] = 0
print("Modified dict1:", dict1)
