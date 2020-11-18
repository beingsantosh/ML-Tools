import re
from bs4 import BeautifulSoup
import unicodedata
import spacy
from spacy.lang.en.stop_words import STOP_WORDS as stopwords
nlp = spacy.load('en_core_web_sm')


contraction_mapping = {"ain't": "is not", "aren't": "are not","can't": "cannot", "'cause": "because", "could've": "could have", "couldn't": "could not", "didn't": "did not",  "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hasn't": "has not", "haven't": "have not", "he'd": "he would","he'll": "he will", "he's": "he is", "how'd": "how did", "how'd'y": "how do you", "how'll": "how will", "how's": "how is",  "I'd": "I would", "I'd've": "I would have", "I'll": "I will", "I'll've": "I will have","I'm": "I am", "I've": "I have", "i'd": "i would", "i'd've": "i would have", "i'll": "i will",  "i'll've": "i will have","i'm": "i am", "i've": "i have", "isn't": "is not", "it'd": "it would", "it'd've": "it would have", "it'll": "it will", "it'll've": "it will have","it's": "it is", "let's": "let us", "ma'am": "madam", "mayn't": "may not", "might've": "might have","mightn't": "might not","mightn't've": "might not have", "must've": "must have", "mustn't": "must not", "mustn't've": "must not have", "needn't": "need not", "needn't've": "need not have","o'clock": "of the clock", "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not", "shan't've": "shall not have", "she'd": "she would", "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have", "she's": "she is", "should've": "should have", "shouldn't": "should not", "shouldn't've": "should not have", "so've": "so have","so's": "so as", "this's": "this is","that'd": "that would", "that'd've": "that would have", "that's": "that is", "there'd": "there would", "there'd've": "there would have", "there's": "there is", "here's": "here is","they'd": "they would", "they'd've": "they would have", "they'll": "they will", "they'll've": "they will have", "they're": "they are", "they've": "they have", "to've": "to have", "wasn't": "was not", "we'd": "we would", "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have", "we're": "we are", "we've": "we have", "weren't": "were not", "what'll": "what will", "what'll've": "what will have", "what're": "what are",  "what's": "what is", "what've": "what have", "when's": "when is", "when've": "when have", "where'd": "where did", "where's": "where is", "where've": "where have", "who'll": "who will", "who'll've": "who will have", "who's": "who is", "who've": "who have", "why's": "why is", "why've": "why have", "will've": "will have", "won't": "will not", "won't've": "will not have", "would've": "would have", "wouldn't": "would not", "wouldn't've": "would not have", "y'all": "you all", "y'all'd": "you all would","y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have","you'd": "you would", "you'd've": "you would have", "you'll": "you will", "you'll've": "you will have", "you're": "you are", "you've": "you have" }
def contraction_(x):
    for cont , exp in contraction_mapping.items():
        x = re.sub(cont,exp,x)
    return x


def _get_word_count(x):
    return len(str(x).split())

def _get_char_count(x):
    return len(''.join(str(x).split()))


def get_avg_word_length(x):
    return get_char_count(x)/get_word_count(x)


def remove_accented_chars(x):
    x = unicodedata.normalize('NFKD', x).encode('ascii','ignore').decode('utf-8','ignore')
    return x

#email
regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"


def convert_to_root(x):
    doc= nlp(x)
    x_list=[]
    for w in doc:
        root = w.lemma_
        x_list.append(root)
    return ' '.join(x_list)


#df['content']=df['content'].apply(lambda x: x.lower() )
#df['content']=df['content'].apply(lambda x: contraction_(x))
#df['content']=df['content'].apply(lambda x : re.sub('[a-zA-Z0-9_-]*@[a-zA-Z0-9_-]+\.com',' ', x))
#df['content']=df['content'].apply(lambda x : re.sub(regex, '', x))
#df['content']=df['content'].apply(lambda x : re.sub('[^\w ]+','',x))
#df['content']=df['content'].apply(lambda x : re.sub('\s{2,}',' ',x))
#df['content']=df['content'].apply(lambda x : BeautifulSoup(x,'html').get_text().strip())
#df['content']=df['content'].apply(lambda x : remove_accented_chars(x))
#df['content']=df['content'].apply(lambda x : ' '.join([w for w in x.split() if w not in stopwords]))
#df['content']=df['content'].apply(lambda x : convert_to_root(x))