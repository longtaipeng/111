import random, string

class Game:
    def __init__(self):
        self.Coupon = []
        self.len_coupon = 10
        self.count = int(input("请输入需要多少优惠券："))
        self.ALL_STR = string.ascii_uppercase + string.digits
    def panduan(self):
        if self.count < 1:
            print("输入错误")
            exit()
    try:
        def game(self):
            for i in range(self.count):
                str = ''.join(random.choice(self.ALL_STR) for i in range(self.len_coupon))
                if str not in self.Coupon:
                    self.Coupon.append((str))
            str1 = ','.join(self.Coupon)
            with open('优惠券', 'w', encoding='utf8') as c:
                c.write(str1)
                print("写入成功")
    except:
        print("写入失败")
    def start(self):
        self.panduan()
        self.game()