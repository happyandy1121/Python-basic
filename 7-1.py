# 設計一個猜數字遊戲

# a = input("Guess number") 這是錯誤用法，input進來的型態是str，所以要轉成int才能比大小
a = int(input("Guess number"))
number = 66

if a<number:
    print("Too small")
elif a>number:
    print("Too big")
else:
    print("Correct")