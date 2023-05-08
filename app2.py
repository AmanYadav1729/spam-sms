{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "56800644",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import string\n",
    "from nltk.corpus import stopwords\n",
    "import nltk\n",
    "from nltk.stem.porter import PorterStemmer\n",
    "\n",
    "ps = PorterStemmer()\n",
    "\n",
    "\n",
    "def transform_text(text):\n",
    "    text = text.lower()\n",
    "    text = nltk.word_tokenize(text)\n",
    "\n",
    "    y = []\n",
    "    for i in text:\n",
    "        if i.isalnum():\n",
    "            y.append(i)\n",
    "\n",
    "    text = y[:]\n",
    "    y.clear()\n",
    "\n",
    "    for i in text:\n",
    "        if i not in stopwords.words('english') and i not in string.punctuation:\n",
    "            y.append(i)\n",
    "\n",
    "    text = y[:]\n",
    "    y.clear()\n",
    "\n",
    "    for i in text:\n",
    "        y.append(ps.stem(i))\n",
    "\n",
    "    return \" \".join(y)\n",
    "\n",
    "tfidf = pickle.load(open('vectorizer.pkl','rb'))\n",
    "model = pickle.load(open('model.pkl','rb'))\n",
    "\n",
    "st.title(\"Email/SMS Spam Classifier\")\n",
    "\n",
    "input_sms = st.text_area(\"Enter the message\")\n",
    "\n",
    "if st.button('Predict'):\n",
    "\n",
    "    # 1. preprocess\n",
    "    transformed_sms = transform_text(input_sms)\n",
    "    # 2. vectorize\n",
    "    vector_input = tfidf.transform([transformed_sms])\n",
    "    # 3. predict\n",
    "    result = model.predict(vector_input)[0]\n",
    "    # 4. Display\n",
    "    if result == 1:\n",
    "        st.header(\"Spam\")\n",
    "    else:\n",
    "        st.header(\"Not Spam\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c7dd3d5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74071409",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
