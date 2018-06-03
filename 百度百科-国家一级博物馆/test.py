'''import json
with open('/home/wlj/PycharmProjects/MuseumSpider1/out2.json', 'r') as f:
    data = json.load(f)
mset1=set()
for d in data:
    mset1.add(d['name'])
#print(mset1)
with open('/home/wlj/PycharmProjects/MuseumSpider1/out.json', 'r') as f:
    data1=json.load(f)
mset2=set()
for d in data1:
    mset2.add(d['name'])
for d in data1:
    mset2.add(d['name'])
#print(mset2)
l=[]
print(len(mset1),len(mset2))
print(mset2-mset1)'''
import json
with open('/home/wlj/PycharmProjects/MuseumSpider1/out2.json', 'r') as f:
    data = json.load(f)
mset1=set()
for d in data:
    t=d['collection'].strip()
    if t:
        print(t)
        mset1.add(d['name'])
with open('/home/wlj/PycharmProjects/MuseumSpider1/out.json', 'r') as f:
    data1=json.load(f)
mset2=set()
for d in data1:
    mset2.add(d['name'])
print(len(mset1),len(mset2))
print(mset2-mset1)

