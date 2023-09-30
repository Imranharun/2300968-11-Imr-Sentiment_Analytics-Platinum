# Data Science Challange - Platinum

Hi, my name is [Imran](https://www.linkedin.com/in/imranharun/).
This API is meant for Binar Academy challenge purpose - Data Science Wave 11.

![Alt text](https://raw.githubusercontent.com/Imranharun/2300968-11-Imr-Sentiment_Analytics-Platinum/master/logo%20binar/logo%20binar.png)

## Model file(s)

Since the files are considered to be large by git, files can be downloaded on this url:

``
https://drive.google.com/drive/folders/10KitDcOeGgmdKqj50BwrQNYXRx3v-6Uv?usp=sharing
``

Put the model files to the **model-deploy-learn/models/**, you can choose any;

Files in the link as in .h5 or .p formats.

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

#### Sentiment Upload
Upload Data, format guidance through the:

``
routers/sentiment.py
``
and,

``
services/sentiment.py
``

### Database API

#### Get DB

Get all the DB from tweets.db

#### Get DB w/ filter

Get the DB the filter / sorting based on the dropdown.