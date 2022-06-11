"""
a=10
print(type(a))
"""

# d= {}
# print(type(d))

#kon kya khata hai??
d2 ={"Harry" :"Burger", "Sneha":"Fish", "Tarun":"Ghee-roti", "Sachin":"egg-roll" ,
     "Subham": {"B":"milk", "L":"Dahi", "D":"Sabji"}}
print(d2)
print(d2["Harry"])
print(d2["Subham"])
print(d2["Subham"]["L"])
d2["Ankit"]="Junk Food"
print(d2)
del(d2["Ankit"]) # or write it like- del d2["Ankit"]
print(d2)

d3= d2.copy() # separate copy will be assigned to d3
del d3["Harry"]
print(d2)
print(d3)

"""
d3 = d2
del d3["Harry"] # it will also delete Harry from d2
"""

print(d2.get("Harry"))
(d2.update({"Leena" : "Toffee"}))
print(d2)
print(d2.keys())
print(d2.items())