from postagger import Postagger
from tokenizer import Tokenizer
from sentencespliting import SentenceSpliting
import logging
import pyfreeling

import json

j = json.loads('{"1":"El", "2":"mundo", "3":"donde", "4":"vivimos"}')
analize = Postagger(j)

# try:
    
k = analize.inicio()
    
# except:
#     logging.exception('')


# k=[]
# #tokens = j[:]

# for i, tk in enumerate(j):
#     k.append(freeling.word(j[str(i+1)]))
#     #print (j[str(i+1)])

# #print (j['1'])
# sentencia = freeling.sentence(tuple(k))
# print(sentencia)
print(k)