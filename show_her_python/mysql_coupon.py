import MySQLdb

class Coupon:
    def star(self):
        mysql = MySQLdb.connect(
            host='localhost',
            user='root',
            password='0216',
            db='long1'
        )

        cur = mysql.cursor()

        try:
            with open('优惠券', 'r', encoding='utf8') as c:
                str_coupon = c.read()
            for i in str_coupon.split(','):
                if len(i) == 10:
                    s = "'" + i + "'"
                    cur.execute("insert uid values({})".format(s))
                    mysql.commit()
            print("写入成功")
            with open('优惠券', 'w', encoding='utf8') as c:
                c.write("")

        except:
            print("写入失败")
