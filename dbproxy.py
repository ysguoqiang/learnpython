# -*- coding: UTF-8 -*-


import MySQLdb


class dbproxy:

    def __init__(self):
        pass

    def connectdb(self,ip,user,passwd,database):
        self.db=MySQLdb.connect(ip,user,passwd,database)
        self.cursor=self.db.cursor()

    def selectdata(self,sql):        
        self.cursor.execute(sql)
        retdata=self.cursor.fetchall()
        self.cursor.close()
        return retdata
        
    def exesql(self,sql):
        self.cursor.execute(sql)
        self.db.commit()
        self.cursor.close()

    def close(self):
        self.conn.close()




