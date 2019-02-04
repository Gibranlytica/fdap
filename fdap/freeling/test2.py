from postagger import Postagger
from tokenizer import Tokenizer
from sentencespliting import SentenceSpliting
import logging 

analize = Postagger("Te espero el lunes. A las tres menos cuarto.")

try:
    
    k = analize.inicio()
    
except:
    logging.exception('')

print(k)