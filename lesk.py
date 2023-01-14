import nltk as nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from pywsd.lesk import simple_lesk  
import time

# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

inp1='The artist left his sculptures to the British mueseum'
inp2='The man was told that an organ was not available for the choir'
a1= word_tokenize('The artist left his sculptures to the British mueseum')
start=time.time()
print(lesk(a1, 'organ', 'n'))
print(time.time()-start)

a2 =word_tokenize('The man was told that an organ was not available for the choir')
print(lesk(a2, 'organ', 'n'))


for ss in wn.synsets('organ'):
     print(ss, ss.definition())
print(lesk(a1, 'organ', 'n'))