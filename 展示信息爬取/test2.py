'''
import jieba
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer


def cut_sentence(sentence):
    """
    分句
    :param sentence:
    :return:
    """
    #if not isinstance(sentence,unicode):
        #sentence = sentence.decode('utf-8')
    delimiters = frozenset(u'。！？')
    buf = []
    for ch in sentence:
        buf.append(ch)
        if delimiters.__contains__(ch):
            yield ''.join(buf)
            buf = []
    if buf:
        yield ''.join(buf)


def load_stopwords(path='/home/fhqplzj/data/orion/stopwords.txt'):
    """
    加载停用词
    :param path:
    :return:
    """
    with open(path) as f:
        stopwords = filter(lambda x: x, map(lambda x: x.strip().decode('utf-8'), f.readlines()))
    stopwords.extend([' ', '\t', '\n'])
    return frozenset(stopwords)


def cut_words(sentence):
    """
    分词
    :param sentence:
    :return:
    """
    stopwords = load_stopwords()
    return filter(lambda x: not stopwords.__contains__(x), jieba.cut(sentence))


def get_abstract(content, size=3):
    """
    利用textrank提取摘要
    :param content:
    :param size:
    :return:
    """
    docs = list(cut_sentence(content))
    tfidf_model = TfidfVectorizer(tokenizer=jieba.cut, stop_words=load_stopwords())
    tfidf_matrix = tfidf_model.fit_transform(docs)
    normalized_matrix = TfidfTransformer().fit_transform(tfidf_matrix)
    similarity = nx.from_scipy_sparse_matrix(normalized_matrix * normalized_matrix.T)
    scores = nx.pagerank(similarity)
    tops = sorted(scores.iteritems(), key=lambda x: x[1], reverse=True)
    size = min(size, len(docs))
    indices = map(lambda x: x[0], tops)[:size]
    return map(lambda idx: docs[idx], indices)


s = u'要说现在当红的90后男星，那就不得不提鹿晗、吴亦凡、杨洋、张艺兴、黄子韬、陈学冬、刘昊然，2016年他们带来不少人气爆棚的影视剧。这些90后男星不仅有颜值、有才华，还够努力，2017年他们又有哪些傲娇的作品呢？到底谁会成为2017霸屏男神，让我们拭目以待吧。鹿晗2016年参演《盗墓笔记》、《长城》、《摆渡人》等多部电影，2017年他将重心转到了电视剧。他和古力娜扎主演的古装奇幻电视剧《择天记》将在湖南卫视暑期档播出，这是鹿晗个人的首部电视剧，也是其第一次出演古装题材。该剧改编自猫腻的同名网络小说，讲述在人妖魔共存的架空世界里，陈长生(鹿晗饰演)为了逆天改命，带着一纸婚书来到神都，结识了一群志同道合的小伙伴，在国教学院打开一片新天地。吴亦凡在2017年有更多的作品推出。周星驰监制、徐克执导的春节档《西游伏魔篇》，吴亦凡扮演“有史以来最帅的”唐僧。师徒四人在取经的路上，由互相对抗到同心合力，成为无坚不摧的驱魔团队。吴亦凡还和梁朝伟、唐嫣合作动作片《欧洲攻略》，该片讲述江湖排名第一、第二的林先生(梁朝伟饰)和王小姐(唐嫣饰)亦敌亦友，二人与助手乐奇(吴亦凡饰)分别追踪盗走“上帝之手”地震飞弹的苏菲，不想却引出了欧洲黑帮、美国CIA、欧盟打击犯罪联盟特工们的全力搜捕的故事。吴亦凡2017年在电影方面有更大突破，他加盟好莱坞大片《极限特工3：终极回归》，与范·迪塞尔、甄子丹、妮娜·杜波夫等一众大明星搭档，为电影献唱主题曲《JUICE》。此外，他还参演吕克·贝松执导的科幻电影《星际特工：千星之城》，该片讲述一个发生在未来28世纪星际警察穿越时空的故事，影片有望2017年上映。'
for i in get_abstract(s):
    print(i)
'''
'''
from snownlp import SnowNLP

text = '自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。自然语言处理是一门融语言学、计算机科学、数学于一体的科学。因此，这一领域的研究将涉及自然语言，即人们日常使用的语言，所以它与语言学的研究有着密切的联系，但又有重要的区别。自然语言处理并不是一般地研究自然语言，而在于研制能有效地实现自然语言通信的计算机系统，特别是其中的软件系统。因而它是计算机科学的一部分。'

s = SnowNLP(text)


l=s.summary(3)
'''
import codecs
from textrank4zh import TextRank4Keyword,TextRank4Sentence

text ='自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。自然语言处理是一门融语言学、计算机科学、数学于一体的科学。因此，这一领域的研究将涉及自然语言，即人们日常使用的语言，所以它与语言学的研究有着密切的联系，但又有重要的区别。自然语言处理并不是一般地研究自然语言，而在于研制能有效地实现自然语言通信的计算机系统，特别是其中的软件系统。因而它是计算机科学的一部分。'

tr4w = TextRank4Keyword()

tr4w.analyze(text=text, lower=True, window=2)

print('关键词：')
for item in tr4w.get_keywords(10, word_min_len=1):
    print("{} 出现的频率为:{:.6f}".format(item.word, item.weight))

print('关键短语：')
for phrase in tr4w.get_keyphrases(keywords_num=10, min_occur_num=5):
    print(phrase)

tr4s = TextRank4Sentence()
tr4s.analyze(text=text, lower=True, source='all_filters')

print()
print('摘要：')
print(len(tr4s.get_key_sentences()))
for item in tr4s.get_key_sentences(num=3):
    print("第{}句出现的频率为:{:.6f},内容为:{}".format(item.index, item.weight, item.sentence))