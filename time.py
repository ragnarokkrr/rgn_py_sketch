import time

import datetime


tt = time.time()
ttt = int(tt )


print tt, ttt
#print ttt, time.strftime(" %d %b %Y %H:%M:%S ", time.localtime() )

st = datetime.datetime.fromtimestamp(ttt).strftime('%Y-%m-%d %H:%M:%S')


print tt, ttt, st