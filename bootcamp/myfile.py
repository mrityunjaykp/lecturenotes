import pandas as pd
import pymysql as p

df = pd.read_csv("movies.csv")
df.dropna(inplace=True)

def getconnect():
    return p.connect(host="localhost", user="root", password="", database="newbootcamp")


def insertrec(t):
    db = getconnect()
    cr = db.cursor()

    sql = "insert into movies values(%s, %s, %s, %s, %s, %s)"
    cr.execute(sql, t)

    db.commit()
    db.close()


table = []
for i, s, t, c, g, d, a in df.itertuples():
    table.append([i,s,t,c,g,d])


def senddata():
    for data in table:
        insertrec(data)
    print("Data transfered Successfully...!")
