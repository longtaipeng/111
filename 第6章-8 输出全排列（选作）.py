

def there(n):
    return (str(x)+str(y)+str(z) for x in range(1, n+1) for y in range(1, n+1) if x != y for z in range(1, n+1) if y != z and x != z)

def four(n):
    return (str(x) + str(y) + str(z) + str(i) for x in range(1, n+1) for y in range(1, n+1) if y != x for z in range(1, n+1) if z != y and z != x for i in range(1, n+1) if i != z and i != y and i != x)

def five(n):
    return (str(x)+str(y)+str(z)+str(a)+str(b)
            for x in range(1, n+1) for y in range(1, n+1) if y != x for z in range(1, n+1) if z != y and z != x
            for a in range(1, n+1) if a != z and a != x and a != y
            for b in range(1, n+1) if b != a and b != z and b != x and b != y)

def six(n):
    return (str(x)+str(y)+str(z)+str(a)+str(b)+str(c)
            for x in range(1, n+1) for y in range(1, n+1) if y != x for z in range(1, n+1) if z != y and z != x
            for a in range(1, n+1) if a != z and a != x and a != y
            for b in range(1, n+1) if b != a and b != z and b != x and b != y
            for c in range(1, n+1) if c != b and c != a and c != z and c != y and c != x)

def seven(n):
    return (str(x) + str(y) + str(z) + str(a) + str(b) + str(c)+str(d)
            for x in range(1, n+1) for y in range(1, n+1) if y != x for z in range(1, n+1) if z != y and z != x
            for a in range(1, n+1) if a != z and a != x and a != y
            for b in range(1, n+1) if b != a and b != z and b != x and b != y
            for c in range(1, n+1) if c != b and c != a and c != z and c != y and c != x
            for d in range(1, n+1) if d != c and d != b and d != a and d != z and d != y and d != x)

n = int(input())
if n == 3:
    print('\n'.join(list(there(n))))
elif n == 4:
    print('\n'.join(list(four(n))))
elif n == 5:
    print('\n'.join(list(four(n))))
elif n == 6:
    print('\n'.join(list(four(n))))
elif n == 7:
    print('\n'.join(list(four(n))))