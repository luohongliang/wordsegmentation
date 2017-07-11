# -*- coding:UTF-8 -*-


import os
import os.path
import string
import sys
import csv
from hanziconv import HanziConv
reload(sys)
sys.setdefaultencoding( "utf-8" )


count = 0

a = '/home/hongliang/inpho/wordsegmentation/dicitonaries/ouyang_dictionary/Dictionary.txt'
f = open(a,'r')
fq = open('/home/hongliang/inpho/wordsegmentation/dicitonaries/ouyang_dictionary.dic','w')

for word in f.readlines():
    word = word.strip().replace(u'\ufeff','')
    word = word.replace('，','')
    word = word.replace(' ','')
    num = len(word)
    sim_word = HanziConv.toSimplified(word)
    sim_word = sim_word.encode('utf-8')
    if num != 1:
        content = str(num)+' '+sim_word+'\n'
        fq.write(content)




