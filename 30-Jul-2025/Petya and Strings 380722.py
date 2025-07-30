# Problem: Petya and Strings - https://codeforces.com/problemset/problem/112/A

str1=input()
str2=input()
if str1.lower()==str2.lower():
    print("0")
for i in range(len(str1)):
    if ord(str1[i].lower()) < ord(str2[i].lower()):
        print("-1")
        break
    elif ord(str1[i].lower()) > ord(str2[i].lower()):
        print("1")
        break