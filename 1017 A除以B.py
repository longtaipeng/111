'''
本题要求计算 A/B，其中 A 是不超过 1000 位的正整数，B 是 1 位正整数。
你需要输出商数 Q 和余数 R，使得 A=B×Q+R 成立。
'''
a, b = input().split(' ')
m = [int(x) for x in a]
if len(m) > 20:
    b = int(b)
    s = []
    i = 0
    while True:
        if m[i] != 0:
            if m[i] // b:
                if i != len(m) - 1:
                    s.append(m[i] // b)
                    m[i + 1] += (m[i]) % b * 10
                    i += 1
                else:
                    s.append(m[i] // b)
                    x = m[i] % b
                    break

            else:
                if i != len(m) - 1:
                    if i != 0:
                        s.append(0)
                        s.append((m[i]*10 + m[i+1]) // b)
                        m[i+2] +=(m[i]*10 + m[i+1]) % b * 10
                        i += 2
                    else:
                        s.append((m[i] * 10 + m[i + 1]) // b)
                        m[i + 2] += (m[i] * 10 + m[i + 1]) % b * 10
                        i += 2
                else:
                    s.append((m[i]*10 + m[i+1]) // b)
                    x = (m[i]*10 + m[i+1]) % b
                    break
        else:
            if i != len(m) - 1:
                s.append(0)
                i += 1
            else:
                s.append(0)
                x = 0
                break

    s1 = [str(i) for i in s]
    print(''.join(s1), x)
else:
    print(int(a)//int(b), int(a) % int(b))

# n=input().split()
# a=n[0]
# b=int(n[1])
# s=''
# r='0'
# for i in range(len(a)):
#     q=int(r+a[i])//b
#     r=str(int(r+a[i])%b)
#     s+=str(q)
# print(int(s),r)

a = input().split()
q = int(a[0])//int(a[1])
r = int(a[0])%int(a[1])
print(q,r)