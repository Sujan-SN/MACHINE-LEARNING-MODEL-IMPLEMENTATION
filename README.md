# MACHINE-LEARNING-MODEL-IMPLEMENTATION

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: SUJAN S N

*INTERN ID*: CTIS6847

*DOMAIN*: Python Programming

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

## DESCRIPTION OF THE TASK

This project aims to develop a predictive model for detecting spam messages using techniques from Machine Learning. Spam detection is an important real-world application, as unwanted messages can lead to security risks, fraud, and reduced productivity. The objective of this project is to classify messages into two categories: spam and non-spam (ham), based on their textual content.

A publicly available SMS dataset containing thousands of labeled messages was used for this task. Each message in the dataset is tagged as either “spam” or “ham.” The first step involved data preprocessing, where the text data was cleaned and prepared for analysis. Since machine learning models cannot directly understand text, the messages were transformed into numerical features using the TF-IDF method. This technique assigns importance to words based on their frequency and relevance, allowing the model to better understand patterns in the data.

After preprocessing, the dataset was split into training and testing sets. The training set was used to teach the model to recognize patterns associated with spam messages, while the testing set was used to evaluate its performance on unseen data. For classification, the Naive Bayes classifier was implemented using the scikit-learn library. This algorithm is widely used for text classification problems due to its simplicity and efficiency.

The trained model achieved an accuracy of approximately 96%, indicating a high level of performance in distinguishing between spam and legitimate messages. The model was further tested using custom input messages to verify its predictive capability in real-time scenarios. Results showed that the model performs well when identifying messages containing common spam-related keywords such as “win,” “free,” “urgent,” and “prize.”

Despite its high accuracy, the model has certain limitations. It may struggle with very short or ambiguous messages and depends heavily on patterns seen during training. Improving the dataset size, using advanced algorithms, or incorporating deep learning techniques could further enhance performance.

In conclusion, this project successfully demonstrates how machine learning can be applied to solve practical problems like spam detection. It highlights key steps such as data preprocessing, feature extraction, model training, and evaluation. The results confirm that machine learning models can effectively automate the process of filtering unwanted messages, making communication systems more secure and efficient.

## OUTPUT

<img width="930" height="251" alt="Image" src="https://github.com/user-attachments/assets/d86cd35a-d8f4-4947-b5b2-58208e5dde69" />


