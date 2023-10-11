# Data Science Challange - Platinum

## Introduction
Hi, my name is [Imranharun Mughni Hutomo](https://www.linkedin.com/in/imranharun/).
This API is meant for Binar Academy challenge purpose - Data Science Wave 11.

![Alt text](https://raw.githubusercontent.com/Imranharun/2300968-11-Imr-Sentiment_Analytics-Platinum/master/logo%20binar/logo%20binar.png)


## Prerequisites  & Installing
 
 
Create conda env:
 
 
``
conda create --n openai_env python=3.9
``
 
Activate env:
 
 
``
conda activate openai_env
``
 
Install All Depedencies :
 
``
pip install -r requirements.txt
``
 
Run :
 
``
make run
``

## Model file(s)

Since the files are considered to be large by git, files can be downloaded on this url:

[Download Models Here](https://drive.google.com/drive/folders/10KitDcOeGgmdKqj50BwrQNYXRx3v-6Uv?usp=sharing)


Put the model files to the **model-deploy-learn/models/**, you can choose any of the models;

Files in the link as in .h5 or .p formats.

### Model Description

There are 7 models in this API:

1. [huggingface (ayameRushia)](https://huggingface.co/ayameRushia/bert-base-indonesian-1.5G-sentiment-analysis-smsa)

2. NN (Neural Network)
3. RNN (Recurrent Neural Network)
4. LSTM (Long Short Term Memory Network)

Fine Tuned Ver.: This version applied with k-fold cross validation

5. LSTM Fine Tuned
6. NN Fine Tuned
7. RNN Fine Tuned

#### Loss & Accuracy Each Models



## API & ITS FEATURES (Simple Documentation)

### Cleansing API

Cleans text data, it removes:

    1. Hashtags attached to a word
    2. Symbols
    3. Emojis
    4. Word: user (after being lowered case by the cleansing code) - user as Twitter text context
    5. 'ø', 'ù', 'º', 'ð', etc
    6. Repeated words
    7. /n or enter
    8. Spaces

### Sentiment API

####
Sentiment Analytics with 7 different models, check the API code and the report.

#### Sentiment Analytics

You will require to insert a text into the box, it will show the sentiment of the sentence you submit. Although, this will only work in Bahasa Indonesia language.

#### Sentiment Upload

You will be able to upload CSV data in this service, the uploaded file will be put into the DB under the name "tweets.db" and it will be classified by the Sentiment Analytics.

The purpose of this service is to get sentiment in a bulk, so you won't need to put each text data manually 

``
routers/sentiment.py
``
and,

``
services/sentiment.py
``

### Database API

In this service I apply SQL Syntax for this service. There are two service routes within this feature

#### Get DB

This will get all data from the tweets.db.

#### Get DB w/ filter

Get the DB the filter / sorting based on the dropdown.