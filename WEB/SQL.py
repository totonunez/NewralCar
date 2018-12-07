from configuraciones import *
import psycopg2

class SQLMAGIC:
  def __init__(self):
    self.conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
    print("dbname=%s user=%s password=%s"%(database,user,passwd))
    self.cur = self.conn.cursor()
    self.sql=""""""

  def setSql(self,m):
    self.cur.execute(m)
    self.conn.commit()
    self.post_id=self.cur.fetchone()[0]
    print(self.post_id)
    return
  
  
  def sql(self, command):
    self.sql=command
    self.setSql()
    return 
  
  def close(self):
    self.cur.close()
    self.conn.close()
