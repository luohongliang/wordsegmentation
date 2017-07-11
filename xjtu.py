# -*- coding:UTF-8 -*-
import os
import mmseg

dictionary = 'ancient words.dic'
file = raw_input("Please input filename [default is corpus/13classes/仪礼/丧服第十一.txt]:") or 'corpus/13classes/仪礼/丧服第十一.txt'
f = open(file)
data = f.read()



# reset_mmseg()
mmseg.Dictionary.load_words(dictionary)


tokenizer = mmseg.Algorithm(data)
tokens_xjtu = []
for token in tokenizer:
    token = token.text.decode('utf-8-sig', errors='replace').replace(u'\x00', '')
    if token:
        tokens_xjtu.append(token)
        
print 'using',dictionary,'has',len(tokens_xjtu),'words'
for a in tokens_xjtu:
    print a,
print 'using',dictionary,'has',len(tokens_xjtu),'words'
