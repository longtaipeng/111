n = int(input())
str1 = {}
for i in range(n):
    s = input()
    str1[s] = len(s)
print('The longest is:',max(str1, key=str1.get))