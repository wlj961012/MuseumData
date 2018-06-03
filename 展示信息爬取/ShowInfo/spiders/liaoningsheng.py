import scrapy
from ..items import ShowinfoItem

class LiaoNingSpider(scrapy.Spider):

    name="liaoningSpider"
    start_urls=['http://www.nmgbwy.com/zldt/1356.jhtml']

    def parse(self, response):
        item=ShowinfoItem()

        museum="辽宁省博物馆"


        item['name'] = "明清瓷器展"
        item['museum'] = museum
        item['time']=""
        item['address']=""
        item['introduce']="瓷器是中国人民的伟大发明，千百年来一直浓缩和传承着中华民族的杰出智慧和创新精神。瓷器滥觞于东汉时期，历经魏晋、隋唐、宋元瓷业的发展后，于明清时期达到鼎盛。明代起，江西景德镇跃升为“天下窑器所集”之瓷都，所烧瓷器的品种、产量、销路均超过以往任何一个时期。青花瓷器经元代短暂的繁荣后，在明代得以创新和推广，成为全国瓷器生产的主流；以成化斗彩为代表的彩瓷、永乐宣德时期的铜红釉和其他颜色釉瓷器，技术高妙、气韵雅静，是我国制瓷史上的空前杰作。清代，特别是康熙、雍正、乾隆三朝，制瓷业达到了历史最高峰，所制瓷器以精妙严谨著称，且“行于九域，施及外洋”。除沿袭前代的制瓷工艺外，新创的珐琅彩、粉彩等瓷器，美轮美奂，为中国瓷器艺术增添了异彩。明清瓷器，集中国古代工艺之大成，忠实地记录了瓷工们的不朽功绩，也折射出了创造它们的时代的特有光辉。"

        yield item
