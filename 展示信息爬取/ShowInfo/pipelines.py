import codecs
from textrank4zh import TextRank4Keyword,TextRank4Sentence
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

class ShowinfoPipeline(object):
    def __init__(self):
        self.count=0
        self.file = codecs.open('out1.json', 'w')

    def process_item(self, item, spider):

        with open('out2.txt','a') as f:
            f.write(item['introduce'])
            f.write('\n')
            self.count+=1
        if item['time']:
            item['introduce']=item['introduce'].replace(item['time'],'')
        if item['introduce']:
            item['introduce']=item['introduce'].replace(item['address'],'')
        if item['time']:
            item['time']=self.process_time(item['time'])
        if item['name']:
            item['name'] = item['name'].replace('\n', '').replace('\r', '').replace(' ', '').replace('\t', '').replace('\u3000','')
        if item['address']:
            item['address']=self.process_address(item['address'])
        if item['introduce']:
            item['introduce']=self.process_introduce(item['introduce'])
        #print(item)
        '''
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        selectsql="select id from museumtest.museum where name='%s'"%item['museum']
        cursor.execute(selectsql)
        result1s = cursor.fetchall()
        if result1s:
            sql = "insert into museumtest.exhibition(museum_id,name,time,address,introduce) values (%s,%s,%s,%s,%s)"
            cursor.execute(sql, (result1s[0][0], item['name'], item['time'], item['address'], item['introduce']))
        selectsql="select name from museumtest.exhibition where museum_id=%s"%result1s[0][0]
        cursor.execute(selectsql)
        result2s = cursor.fetchall()
        ans=set()
        for i in result2s:
            ans.add(i[0].decode('utf-8'))
        if item['name'] not in ans:
            date=(item['name'],item['time'],item['address'],item['introduce'],result1s[0][0])
            updatesql='update museumtest.exhibition set name=%s,time=%s,address=%s,introduce=%s where id=%s '
            cursor.execute(updatesql,date)'''
        '''if results:
                    sql = "insert into museumtest.exhibition(museum_id,name,time,address,introduce) values (%s,%s,%s,%s,%s)"
                    cursor.execute(sql, (results[0][0],item['name'], item['time'], item['address'], item['introduce']))'''
        #dbObject.commit()
        '''except Exception:
            print(Exception)
            print('error')
            dbObject.rollback()'''
        #dbObject.close()

        with open('out2.txt','a') as f:
            f.write('\n')
            f.write(item['introduce'])
            f.write('\n')
        return item

    def close_spider(self, spider):
        self.file.close()

    def process_time(self,create_date):
        create_date=create_date.replace('\n','').replace('\r','').replace('\t','').replace('\xa0','').replace('\u3000','').replace(' ','')
        create_date=create_date.replace('展览','').replace('时间',"").replace('：','')
        return create_date

    def process_address(self,create_add):
        create_add =create_add.replace('\n', '').replace('\r', '').replace('\t', '').replace('\xa0', '').replace('\u3000', '').replace(' ', '')
        create_add=create_add.replace('展览','').replace('地点','').replace('：','')
        return create_add

    def process_introduce(self,introduce):

        introduce=introduce.replace('\n','').replace('\r','').replace('\t','').replace('\xa0','').replace('\u3000','').replace(' ','')
        tr4s = TextRank4Sentence()
        tr4s.analyze(text=introduce, lower=True, source='all_filters')
        l=len(tr4s.get_key_sentences())
        num_sentences=3
        sentences=tr4s.get_key_sentences(num=num_sentences)
        sentences = sorted(sentences, key=lambda x: x.index, reverse=False)
        news=[]
        if l>=num_sentences:
            for i in range(num_sentences):
                news.append(sentences[i].sentence)
        else:
            for i in range(l):
                news.append(sentences[i].sentence)
        return ''.join(news)

