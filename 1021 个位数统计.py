a = input()
k = {}

for i in a:
    if i not in k.keys():
        k[i] = 1
    else:
        k[i] += 1

for key in sorted(k.keys()):
    print("{}:{}".format(key, k[key]))
