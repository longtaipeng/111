import MySQLdb
class use():
    def __init__(self):
        self.sql = "select name from uid"
        self.a = []
        self.b = {}
    def start(self):
        mysql = MySQLdb.connect(
            host='localhost',
            user='root',
            password='0216',
            db='long1'
        )

        cur = mysql.cursor()
        cur.execute(self.sql)

        results = cur.fetchall()
        for i in results:
            i = str(i)
            self.a.append(i.split("'")[1])
        self.sql = "select * from suid"
        cur.execute(self.sql)

        results1 = cur.fetchall()
        for i in results1:
            self.b[i[0]] = i[1]
        s = input("请输入优惠券码：")
        if s in self.a and s not in self.b.values():
            id = input("请输入你的账号：")
            s = "'"+s+"'"
            id = "'"+id+"'"
            self.sql = "insert suid values({},{})"
            cur.execute(self.sql.format(id, s))
            mysql.commit()
            print("使用成功")
        else:
            print('使用错误，优惠券码输入错误')

