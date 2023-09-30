# DSC Challange
 
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