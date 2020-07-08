#lambda expresssion
people = [
    {"name": "harry", "house": "GRYFFINDOR"},
    {"name": "cho", "house": "Ravenclaw"},
    {"name": "draco", "house": "Slytherin"}
    ]

people.append({"name": "hermione", "house": "Gryffindor"})
people.sort(key = lambda people: people["name"])

print(people)
