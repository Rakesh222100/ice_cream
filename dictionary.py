person = {"name": "Rosan","age": 30,"city": "Jagatsinghpur"}
print(person["name"]) 

person["email"] = "rakeshrosanpradhan1@gmail.com"

person["age"] = 35

del person["city"]

for key, value in person.items():
    print(f"{key}: {value}")
