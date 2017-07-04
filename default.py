# -*- coding:UTF-8 -*-

import os
import mmseg

dictionary = 'modern words.dic'
file = raw_input("Please input filename [default is 13classes/仪礼/丧服第十一.txt]:") or '13classes/仪礼/丧服第十一.txt'
f = open(file)
data = f.read()


# reset_mmseg()
mmseg.Dictionary.load_words(dictionary)


tokenizer = mmseg.Algorithm(data)
tokens = []
for token in tokenizer:
    token = token.text.decode('utf-8-sig', errors='replace').replace(u'\x00', '')
    if token:
        tokens.append(token)
print 'using',dictionary,'has',len(tokens),'words'
for a in tokens:
    print a,
print 'using',dictionary,'has',len(tokens),'words'
