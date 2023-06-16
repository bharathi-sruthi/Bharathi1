import pandas as pd
d=pd.read_csv('studentsurvey.csv')
print("Data before cleaning")
print(d.to_string())
d.drop("Timestamp",axis=1,inplace=True)
d.drop("Id Number",axis=1,inplace=True)
d.drop("Name::",axis=1,inplace=True)
print("Data after cleaning")
# df=d.apply(lambda x: x.astype(str).str.lower())
for i in d.columns:
    d[i]=d[i].str.lower()
df=d
print(df.to_string())
flavor3=list(df["Enter your third preference::"])
print(flavor3)
flavor1=list(df["Enter your first preference::"])
print(flavor1)
Third_preference=input("Enter the third preference:")
Third_preference=Third_preference.lower()
li=[]
def first_preference(Third_preference,flavor1,flavor3):
    for i in range(len(flavor3)):
        if Third_preference ==flavor3[i]:
            li.append(flavor1[i])
    print(li)       
first_preference(Third_preference,flavor1,flavor3)
c_count=0
b_count=0
s_count=0
d={}
def count(c_count,b_count,s_count):
    for i in li:
        if i=="butterscotch":
            b_count=b_count+1
        elif i=="chocolate":
            c_count=c_count+1
        else:
            s_count=s_count+1
    d["butterscotch"]=b_count
    d["chocolate"]=c_count
    d["strawberry"]=s_count
count(c_count,b_count,s_count)         #calling count function
print(d)
max=0
for k,v in d.items():
    if max<v:
        max=v
        key=k
    
print("most liked flavor is ",key,':',max)
            






