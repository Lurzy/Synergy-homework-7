userWord = input().lower()
wordUser = userWord[::-1]

if userWord == wordUser:
    print("Yes")
else: 
    print("No")

