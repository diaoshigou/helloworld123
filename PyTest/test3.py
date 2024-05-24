import subprocess
from time import sleep
import random

# process = subprocess.Popen('adb shell am start com.alibaba.android.rimet/com.alibaba.android.rimet.biz.LaunchHomeActivity')


# for i in range(1,11):
#     random_float = float(random.randrange(3, 6))
#     print(random_float + round(random.random(), 3))

Time_reco = 1715152660712
for i in range(9140,10140):

    print("INSERT INTO" + ' "RecogRecord" ' + "(" + '"id"' + ", " + '"trackId"' + ", " + '"rect"' +", "+ '"personId"' +", "+ '"recognizeUserType"' +", "+ '"recognizeType"' +", "+ '"onlineFlag"'
          +", "+ '"recognizeTime"' +", "+ '"score"' +", "+ '"recognizeThreshold"' +", "+ '"timeTake"' +", "+ '"matchResult"' +", "+ '"inGroup"' +") " + "VALUES " +
          "('" + str(i) + "', '" +str(i)+"', "+"'126,84,100,136', '1798280962858024960'" +", "+ "'1'"+", "+"'20'"+", "+"'0', '"+str(Time_reco)+"', '84.553566', '60.000004' "+", "+"'718'"+", "+"'0'"+", "+"'0')"+";")
    Time_reco += 1000
