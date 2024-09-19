names = ["Peter", "Brain", "Leo"]
print("name:",end="")
for name in names:
    print(name,end=" ")

dic = {0: "Andy",
       1: "Ben",
       2: "Charly"}
print("\nkey:",end="")
for key in dic.keys():
    print(key,end=" ")

print("\nvalue:",end="")
for value in dic.values():
    print(value,end=" ")

print("\nitem:",end="")
for key, value in dic.items():
    print(f"{key}: {value}",end=" ")