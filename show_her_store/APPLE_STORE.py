# 优惠券的长度是10个字符，由大字字母和数字随机组成
import random, string



count = int(input("需要多少个优惠券："))
if count < 1:
    print("输入错误！！！")
    exit()
Coupon = []
len_Coupon = 10

ALL_STR = string.ascii_uppercase + string.digits
for i in range(count):
    temporary_coupon = ''.join(random.choice(ALL_STR) for i in range(len_Coupon))
    if temporary_coupon not in Coupon:
        Coupon.append(temporary_coupon)

str_coupon = ','.join(Coupon)

with open('show_her_python\store优惠券\优惠券', 'a', encoding='utf8') as c:
        c.write(str_coupon)

print("优惠券生产并保存成功")


