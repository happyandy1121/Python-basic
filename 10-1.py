count = 0
for string in 'content':
    count+=1
    if string == 't':
        break
    print(string,end="")
print(f"\ncount:{count}")

print("------------")

count = 0
for string in 'content':
    count+=1
    if string == 't':
        continue
    print(string,end="")
print(f"\ncount:{count}")
