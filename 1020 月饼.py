n, m = map(int, input().split(' '))
number = list(map(int, input().split(' ')))
price = list(map(int, input().split(' ')))
price_sum = 0
number_sum = 0
price_number = {price[i]/number[i]:[price[i], number[i]] for i in range(n) }
price_number = sorted(price_number.items(), key=lambda item:item[0], reverse=True)
for i in price_number:
    if m >= i[1][1]:
        price_sum += i[1][0]
        m -= i[1][1]
    else:
        price_sum += i[0]*m
        break

print("{:.2f}".format(price_sum))




