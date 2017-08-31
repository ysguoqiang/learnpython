from dbproxy import *
from gencdkey import *

keyfactory = cdkeygenerator()
allkey = keyfactory.gencdkey(5,20)
for key in allkey:
    print key

# dbconn=dbproxy()
# dbconn.connectdb('127.0.0.1','root','wgq840215','test')

# ret=dbconn.exesql("insert into test(first,value) values(1,2),(3,4)")
# print ret

