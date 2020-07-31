import show_her_python.mysql_coupon, show_her_python.store, show_her_python.use_coupon

if __name__ == '__main__':
    print("1 --> 生产优惠券 2 --> 保存优惠券 3 --> 使用优惠券")
    a = input("请输入序号：")
    if a == '1':
        show_her_python.store.Game().start()
    elif a == '2':
        show_her_python.mysql_coupon.Coupon().star()
    elif a == '3':
        show_her_python.use_coupon.use().start()