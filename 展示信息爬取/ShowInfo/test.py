'''import nltk
# 分词
nltk.download('averaged_perceptron_tagger')
text = "我 是 王丽娟 你好"
sentence = nltk.word_tokenize(text)
print(sentence)
print(type(sentence))
# 词性标注
sentence_tag = nltk.pos_tag(sentence)
print(sentence_tag)
print(type(sentence_tag))
# 定义分块语法
# 这个规则是说一个NP块由一个可选的限定词后面跟着任何数目的形容词然后是一个名词组成
# NP(名词短语块) DT(限定词) JJ(形容词) NN(名词)
grammar = "NP: {<DT>?<JJ>*<NN>}"

# 进行分块
cp = nltk.RegexpParser(grammar)
tree = cp.parse(sentence_tag)
tree.draw()
'''

import jieba
import nltk
import jieba.posseg

def cut_sentences(sentence):
    puns = frozenset(u'。！？，,')
    tmp = []
    for ch in sentence:
        tmp.append(ch)
        if puns.__contains__(ch):
            yield ''.join(tmp)
            tmp = []
    yield ''.join(tmp)
s="计算机评价效果，需要给定参考摘要作为标准答案，通过制定一些规则来给生产的摘要打分。    目前使用最广泛的是ROUGH系统(Recall-Oriented Understudy for Gisting Evaluation),基本思想是将待审的摘要和参考摘要的n元组共现统计量作为评价作为评价依据，然后通过一系列标准进行打分。包括(ROUGH-N, ROUGH-L, ROUGH-W，ROUGH-S和ROUGH-SU)几个类型。  通俗地将就是通过一些定量化的指标来描述待审摘要和参考文摘之间的相似性，维度考虑比较多，在一定程度上可以很好地评价Extracive产生的摘要"
t=[]
for i in cut_sentences(s):
    t.append(i)
t=' '.join(t)
print(t)
seg_list=jieba.cut(t)
text=[]
for i in seg_list:
    text.append(i)
print(text)
text=' '.join(text)
sentence = nltk.word_tokenize(text)
# 词性标注
sentence_tag = nltk.pos_tag(sentence)

#正则提取
grammar = r"""
NP: {<DT|JJ|NN.*>+} 
PP: {<IN><NP>} 
VP: {<VB.*><NP|PP|CLAUSE>+$}
CLAUSE: {<NP><VP>}
t:{<VBD><CD>}
"""
cp = nltk.RegexpParser(grammar,loop=5)
tree = cp.parse(sentence_tag)

print(tree)
tree.draw()


'''seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))'''

'''
import nltk

sent = sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]

grammer = 'NP:{<DT>*<JJ>*<NN>+}'
cp = nltk.RegexpParser(grammer)
tree = cp.parse(sent)

print(tree)
tree.draw()
'''