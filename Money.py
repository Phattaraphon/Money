import pandas as pd

df = pd.read_csv('Money_20220827_140115.csv')

def getbytitle():
    title = str(input("หมวดหมู่ : "))
    date = str(input("ปี-เดือน-วัน : "))
    n = 0
    count = 1
    for i in range(len(df)):
        if df.iloc[i,0].find(title) != -1 and df.iloc[i,1].startswith(' '+date):
            n += df.iloc[i,3]
            print(count,df.iloc[i,0],df.iloc[i,1],df.iloc[i,2],df.iloc[i,3],df.iloc[i,4])
            count +=1
    print('รวม :', n,'บาท')
    print("")
def getbydescription():
    des = str(input("คำอธิบาย : "))
    date = str(input("ปี-เดือน-วัน : "))
    n = 0
    count = 1
    for i in range(len(df)):
        if df.iloc[i,4].find(des) != -1 and df.iloc[i,1].startswith(' '+date):
            n += df.iloc[i,3]
            print(count,df.iloc[i,0],df.iloc[i,1],df.iloc[i,2],df.iloc[i,3],df.iloc[i,4])
            count +=1
    print('รวม :', n,'บาท')
    print("")
def menu():
    print("ค้นหาด้วยหมวดหมู่ กด 1")
    print("ค้นหาด้วยคำอธิบาย กด 2")
    n = str(input("กรอกหมายเลข : "))
    print("")
    if n =='1':
        getbytitle()
    if n == '2':
        getbydescription()
    menu()
menu()
