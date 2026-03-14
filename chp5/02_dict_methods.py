a = {
    "Asad":"90",
    "Abdullah talib":"100",
    "Abu Bakar":"85",
    "talha":"23",
    "hafi":"80"
}

print(a.items()) #print all item and there values

print(a.keys()) #print left hand side values

a.update({"talha":233,"ahmed asif":99})
print(a)                                      #update the dict

b=a.get("Asad")  #print the righthand side value of the written name number etc
print(b)               #it will give none not error

print(a["Saim"]) #if the enter name is not in dict it will give error 