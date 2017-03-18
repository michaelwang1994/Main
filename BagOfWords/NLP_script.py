import pandas as pd
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import datetime

train = pd.read_csv("labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)

def review_to_words(raw_review):
    remove_text_html = BeautifulSoup(raw_review, 'html.parser').get_text()
    remove_punctuation = re.sub("[^a-zA-Z]", " ", remove_text_html)
    review_split = remove_punctuation.lower().split()
    nltk_stopwords = set(stopwords.words("english"))
    meaningful_words = [w for w in review_split if not w in nltk_stopwords]
    return( " ".join( meaningful_words ))

train['review_clean'] = train['review'].apply(lambda x: review_to_words(x))
clean_train_reviews = train['review_clean'].tolist()

vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 5000)

train_data_features = vectorizer.fit_transform(clean_train_reviews)
train_data_features = train_data_features.toarray()
vocab = vectorizer.get_feature_names()
print vocab

forest = RandomForestClassifier(n_estimators = 100)
forest = forest.fit( train_data_features, train["sentiment"] )

test = pd.read_csv("testData.tsv", header=0, delimiter="\t", \
                   quoting=3 )

test['review_clean'] = test['review'].apply(lambda x: review_to_words(x))
clean_test_reviews = test['review_clean'].tolist()

test_data_features = vectorizer.transform(clean_test_reviews)
test_data_features = test_data_features.toarray()

result = forest.predict(test_data_features)

output = pd.DataFrame( data={"id":test["id"], "sentiment":result} )
output.to_csv( "Bag_of_Words_model.csv", index=False, quoting=3 )
