#Before using NLTK's tokenizers, you must install the library and download the punkt data package, which contains the pre-trained unsupervised machine learning models used to detect sentence boundaries and abbreviations

# sent_tokenize for sentence based tokenization
# word_tokenize : splits a sentence into specific sentences and punctuations

import nltk
nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize, word_tokenize
import pandas as pd

text = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi quam illum est iusto quibusdam, aliquid perspiciatis quo dolores vero quisquam! Sint necessitatibus ratione laudantium mollitia harum ipsum quia vero. Suscipit! Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus corporis distinctio sapiente eveniet, fugiat rerum maiores tenetur asperiores tempora magnam, cupiditate incidunt excepturi. Blanditiis impedit adipisci, vitae qui molestias iste!"
sentences = sent_tokenize(text)
word = word_tokenize(text)
print("sentence :",sentences)

print("\n\nwords", word)


# removing punctuation
import string
exclude = string.punctuation
df = pd.read_csv('data/twitter-hate-train.csv')
print(df.sample(5))

df['tweet'] = df['tweet'].astype(str)

def remove_punc(text):
    return text.translate(str.maketrans('','',exclude))

print("\n\n\n\n\n\n",df['tweet'].apply(remove_punc).head())



# spelling correction
from textblob import TextBlob

incorrect_text = (
    "certaaiin conditionas duriing seveal ggenerations aree moodified in the"
    " samme maner"
)
textBlb = TextBlob(incorrect_text)

# Using str() extracts the corrected text reliably
print("Corrected text:", str(textBlb.correct()))


# stop word removal
from nltk.corpus import stopwords

nltk.download('stopwords')
def remove_stop_words(text):
    new_text =[]
    for word in text.split():
        if word in stopwords.words('english'):
            new_text.append('')
        else: 
            new_text.append(word)

    return new_text

print(remove_stop_words("Hi my name is Abhinav Patra, how are are you doing today, if everything is fine, can you stfu and go back to working and not simply bitching and shouting"))


# Tokenization
pre_tokenized_string = "Hi! My name is Abhinav and i am very new to the city, New Delhi."

 