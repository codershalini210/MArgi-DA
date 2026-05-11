
person = {"name":"Raman","age":12,"city":"Vapi"}
print(person)
person.pop("age")      # Removes specific key
print(person)

del person["city"]     # Deletes key

print(person)
person.clear()         # Empties dictionary 
print(person)