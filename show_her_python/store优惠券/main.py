import APPLE_STORE, mysql_coupon

print("1 --> 生成优惠券  2 --> 保存优惠券")
a = input("请输出序号: ")
if a == '1':
    APPLE_STORE.game()
elif  a == '2':
    mysql_coupon.Coupon()