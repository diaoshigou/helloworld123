import pymysql
import subprocess

# 连接数据库
db = pymysql.connect(host='192.168.7.202', user='moredian', password='moredian@1', charset='utf8')
cursor = db.cursor()

try:
    # 从account表中进行账号和密码的匹配
    cursor.execute('select * from hive.hive_org where tp_id = 1741578692972249088')

    # 如果找到，则登录成功
    if cursor.fetchall():
        print('登录成功')
    else:
        print('登录失败')

except Exception as e:
    print(e)

finally:


    result1 = subprocess.getoutput("pip --version")
    print(result1)
    cursor.close()
    db.close()