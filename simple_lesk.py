import nltk as nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from pywsd.lesk import simple_lesk  
import time

# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

from pywsd.lesk import simple_lesk  
sentences = ['The artist left his sculptures to the British mueseum',  
'The child, left by his parents, played table football']  
# calling the lesk function and printing results for both the sentences  
print ("Context-1:", sentences[0])  
answer = simple_lesk(sentences[0],'left')  
print ("Sense:", answer)  
print ("Definition : ", answer.definition())  
print ("Context-2:", sentences[1])  
answer = simple_lesk(sentences[1],'left')  
print ("Sense:", answer)  
print ("Definition : ", answer.definition())  
# calling the lesk function and printing results  
new_sentences = ['The workers at the plant were overworked', 'The plant was no longer bearing flowers', 'The workers at the industrial plant were overworked']
print ("Context-1:", new_sentences[0])  
answer = simple_lesk(new_sentences[0],'plant')  
print ("Sense:", answer)  
print ("Definition : ", answer.definition())
print ("Context-2:", new_sentences[1])  
answer = simple_lesk(new_sentences[1],'plant')  
print ("Sense:", answer)  
print ("Definition : ", answer.definition())  
print ("Context-3:", new_sentences[2])  
answer = simple_lesk(new_sentences[2],'plant')  
print ("Sense:", answer)  
print ("Definition : ", answer.definition())


