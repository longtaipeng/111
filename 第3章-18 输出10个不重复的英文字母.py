a = input().replace(' ', '')
b = ''
c = 0
for i in a:
    if i.isalpha():
        h = i
        if ord(h) <= 90:
            h = chr(ord(h) + 32)
        else:
            h = chr(ord(h) - 32)
        if h not in b and i not in b:
                b += i
                c += 1
                if c == 10:
                    break
        else:
            continue
if c == 10:
    print(b)
else:
    print('not found')