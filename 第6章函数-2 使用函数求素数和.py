def prime(n):
    if n == 1:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True


def PrimeSum(num1, num2):
    sum1 = 0
    for i in range(num1, num2):
        if prime(i):
            sum1 += i
    return sum1

m,n=input().split()
m=int(m)
n=int(n)
print(PrimeSum(m,n))
