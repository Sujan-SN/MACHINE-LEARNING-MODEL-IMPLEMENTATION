!pip install pandas numpy scikit-learn

import pandas as pd

url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"

df = pd.read_csv(url, sep="\t", names=["label", "message"])
df.head()

df["label"] = df["label"].map({"ham": 0, "spam": 1})

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["message"])

y = df["label"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score

predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))

def check_spam(message):
    msg_vector = vectorizer.transform([message])
    result = model.predict(msg_vector)
    
    if result[0] == 1:
        return "Spam"
    else:
        return "Not Spam"

print(check_spam("Congratulations! You have won a free iPhone"))
print(check_spam("Hey, are we meeting today?"))

print(check_spam("Congratulations! You have won a $500 gift card. Call now!"))
print(check_spam("URGENT! You have been selected for a prize reward"))
print(check_spam("Free entry in a weekly competition to win tickets"))
