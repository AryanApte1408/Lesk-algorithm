from nltk.wsd import lesk
from pywsd.lesk import simple_lesk
from nltk.tokenize import word_tokenize

con1=lesk(word_tokenize('I withdraw money from the bank.'),'bank')
con2=lesk(word_tokenize('Varanasi is loacated on the bank of river Ganges.'),'bank')
con3=lesk(word_tokenize('University jammed the network'),'jammed')
con4=lesk(word_tokenize('Please give me bread with jam.'),'jam')
scon1=simple_lesk('I withdraw money from the bank.','bank')
scon2=simple_lesk('Varanasi is loacated on the bank of river Ganges.','bank')
scon3=simple_lesk('University jammed the network','jammed')
scon4=simple_lesk('Please give me bread with jam.','jam')

print()
print("----------------Lesk algorithm-----------------")
print()
print(con1,con1.definition())
print(con2,con2.definition())
print(con3,con3.definition())
print(con3,con3.definition())
print()
print("----------------Simplified Lesk algorithm-----------------")
print()
print(scon1,scon1.definition())
print(scon2,scon2.definition())
print(scon3,scon4.definition())
print(scon4,scon4.definition())
