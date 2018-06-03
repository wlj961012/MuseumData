import re
from textrank4zh import TextRank4Sentence
import pymysql

def dbHandle():

    conn = pymysql.connect(
        host="39.106.168.133",
        user="museum",
        passwd='123456',
        charset='utf8',
        use_unicode=False
    )

    return conn

class Museumspider1Pipeline(object):
    
    def process_item(self, item, spider):
        if item['collection']:
            item['collection']=self.process_collection(item['collection'])
        if item['open_time']:
            item['open_time']=self.process_time(item['open_time'])
        if item['edu_activity']:
            item['edu_activity']=self.process_collection(item['edu_activity'])
        if item['introduce']:
            item['introduce']=self.process_time(item['introduce'])
        if item['academic']:
            item['academic']=self.process_collection(item['academic'])
        self.put_mysql(item)
        return item

    def process_collection(self,collection):
        collection=collection.replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\xa0','').replace('\u3000','')
        remove=re.findall('\[.*?\]',collection)
        for r in remove:
            collection=collection.replace(r,"")
        tr4s = TextRank4Sentence()
        tr4s.analyze(text=collection, lower=True, source='all_filters')
        l = len(tr4s.get_key_sentences())

        sentences = tr4s.get_key_sentences(num=3)
        sentences = sorted(sentences, key=lambda x: x.index, reverse=False)
        news = []
        if l>=3:
            for i in range(3):
                news.append(sentences[i].sentence)
        else:
            for i in range(l):
                news.append(sentences[i].sentence)
        return ''.join(news)

    def process_time(self,time):
        time=time.replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace('\xa0','').replace('\u3000','')
        remove = re.findall('\[.*?\]',time)
        for r in remove:
            time=time.replace(r,'')
        return time

    def put_mysql(self,item):
        try:
            dbObject = dbHandle()
            cursor = dbObject.cursor()
            sql = "insert into museumtest.museum(name,introduce,open_time,edu_activity,collection,academic) values (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (item['name'],item['introduce'],item['open_time'],item['edu_activity'],item['collection'],item['academic']))
            dbObject.commit()
        except Exception:
            print(Exception)
            print('error')
            dbObject.rollback()
        dbObject.close()

