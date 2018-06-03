import scrapy
import csv
from ..items import Museumspider1Item
import re

class MuseumSpider(scrapy.Spider):
    
    name="Spider"
    count=0

    def start_requests(self):
        with open("todo.csv", "rU") as f:
            reader = csv.DictReader(f)
            for line in reader:
                request = scrapy.Request(line.pop('url'))
                request.meta['fields'] = line
                yield request


    def parse(self,response):
        item = Museumspider1Item()
        for key, value in response.meta['fields'].items():
            value = value.strip()
            item[key]=" "
            if key == 'name':
                #如果是名字直接取出名字
                item['name'] = value
                self.count+=1
            elif not value:
                #如果xpath不存在则直接在输出中将其置控
                item[key] = ""
            elif key=='introduce':
                #如果对应的介绍则直接通过xpath将其输出 因为基本介绍的xpath是单一的
                if response.xpath(value).xpath('string(.)').extract_first():
                    item[key]=response.xpath(value).xpath('string(.)').extract_first().replace('\n',' ').replace('\r',' ').replace(' ','')
                else:
                    print("ERROR")
            elif key=='open_time':
                paths=value.split('$')
                if len(paths)>1:#表示开放时间由多个div块组成
                    for i in range(len(paths)):
                        if i < len(paths) - 1 and len(paths[i + 1].split('/')) == 1:#表示后面跟着一个数字的情况
                            p = paths[i].split('/')
                            length = int(paths[i + 1].strip())
                            len0 = int(re.findall(r'\d+', p[-1])[0])
                            content=""
                            for j in range(len0,length+1):
                                p[-1] = re.sub(r'\d+', str(j), p[-1], 1, flags=re.I)
                                if response.xpath('/'.join(p)).extract_first():
                                    content+=response.xpath('/'.join(p)).xpath('string(.)').extract_first().replace('\n',' ').replace('\r','').replace(' ','')
                            item[key]=content
                        else:
                            i+=1
                else:#开放时间由一个div块组成
                    item[key]=response.xpath(value).xpath('string(.)').extract_first().replace('\n','').replace(' ','').replace('\r','')
            elif key=="edu_activity":
                paths=value.split('$')
                if len(paths)>1:#表示教育活动由多个div块组成
                    for i in range(len(paths)):
                        if i < len(paths) - 1 and len(paths[i + 1].split('/')) == 1:
                            p = paths[i].split('/')
                            length = int(paths[i + 1].strip())
                            len0 = int(re.findall(r'\d+', p[-1])[0])
                            content = ""
                            for j in range(len0, length + 1):
                                p[-1] = re.sub(r'\d+', str(j), p[-1], 1, flags=re.I)
                                if response.xpath('/'.join(p)).extract_first():
                                    content += response.xpath('/'.join(p)).xpath('string(.)').extract_first().replace('\n', ' ').replace('\r', '').replace(' ', '')
                            item[key] = content
                        else:
                            i+=1
                else:#表示教育活动内容只由一个div块组成
                    if response.xpath(value).xpath('string(.)').extract_first():
                        item[key]=response.xpath(value).xpath('string(.)').extract_first().replace('\n',' ').replace('\r','').replace(' ','')
                    else:
                        item[key]="ERROR"
            elif key=='academic':#学术活动栏
                paths=value.split('$')
                item[key]=" "
                if len(paths)>1:#表示活动由多个div块组成
                    for i in range(len(paths)):
                        if i < len(paths) - 1 and len(paths[i + 1].split('/')) == 1:
                            #遇到路径后面跟着数字的情况
                            p = paths[i].split('/')
                            length = int(paths[i + 1].strip())
                            len0 = int(re.findall(r'\d+', p[-1])[0])
                            if p[-1][0]=='d':#学术内容在连续的div块里
                                content = ""
                                for j in range(len0, length + 1):
                                    p[-1] = re.sub(r'\d+', str(j), p[-1], 1, flags=re.I)
                                    if response.xpath('/'.join(p)).extract_first():
                                        content += response.xpath('/'.join(p)).xpath('string(.)').extract_first().replace('\n', ' ').replace('\r', '').replace(' ', '')
                                item[key] += content
                            elif p[-1][0]=='t':#学术内容在连续的table块里 遇到table情况 对table进行解析
                                content=""
                                for j in range(len0,length+1):
                                    p[-1] = re.sub(r'\d+', str(j), p[-1], 1, flags=re.I)
                                    t=response.xpath('/'.join(p)).xpath('string(.)')
                                    if t:
                                        content+=t.extract_first().replace('\n','').replace('\r','')
                                item[key]+=content
                        elif len(paths[i].split('/')) == 1:#数字跳过解析
                            i+=1
                        else:#内容在单独的table块里面
                            p=paths[i].split('/')
                            content=""
                            if response.xpath(paths[i]).xpath('string(.)'):
                                content=response.xpath(paths[i]).xpath('string(.)').extract()
                            content=''.join(content).replace('\n','').replace('\r','\t')
                            item[key]+=content
                else:#表示学术活动只有一个div块组成
                    if response.xpath(value).xpath('string(.)').extract_first():
                        item[key]=response.xpath(value).xpath('string(.)').extract_first().replace('\n',' ').replace('\r','').replace(' ','')
            elif key=='collection':
                paths = value.split('$')
                item[key] = " "
                if len(paths) > 1:  # 表示藏品由多个div块组成
                    for i in range(len(paths)):
                        if i < len(paths) - 1 and len(paths[i + 1].split('/')) == 1:
                            # 遇到路径后面跟着数字的情况
                            p = paths[i].split('/')
                            length = int(paths[i + 1].strip())
                            len0 = int(re.findall(r'\d+', p[-1])[0])
                            if p[-1][0] == 'd':  # 藏品内容在连续的div块里
                                content = ""
                                for j in range(len0, length + 1):
                                    p[-1] = re.sub(r'\d+', str(j), p[-1], 1, flags=re.I)
                                    if response.xpath('/'.join(p)).extract_first():
                                        content += response.xpath('/'.join(p)).xpath(
                                            'string(.)').extract_first().replace('\n', ' ').replace('\r', '').replace(
                                            ' ', '')
                                item[key] += content
                            elif p[-1][0] == 't':  # 藏品内容在连续的table块里 遇到table情况 对table进行解析
                                content = ""
                                for j in range(len0, length + 1):
                                    p[-1] = re.sub(r'\d+', str(j), p[-1], 1, flags=re.I)
                                    t = response.xpath('/'.join(p)).xpath('string(.)')
                                    if t:
                                        content += t.extract_first().replace('\n', '').replace('\r', '')
                                item[key] += content
                        elif len(paths[i].split('/')) == 1:  # 数字跳过解析
                            i += 1
                        else:  # 内容在单独的table块里面
                            p = paths[i].split('/')
                            content = ""
                            if response.xpath(paths[i]).xpath('string(.)'):
                                content = response.xpath(paths[i]).xpath('string(.)').extract()
                            content = ''.join(content).replace('\n', '').replace('\r', '\t')
                            item[key] += content
                else:  # 表示藏品活动只有一个div块组成
                    if response.xpath(value).xpath('string(.)').extract_first():
                        item[key] = response.xpath(value).xpath('string(.)').extract_first().replace('\n', ' ').replace(
                            '\r', '').replace(' ', '')
            else:
                item[key]=""
        yield item



