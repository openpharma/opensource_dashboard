# Open pharma dashboard

The objective of openpharma is to provide a neutral home for open source software related to pharmaceutical industry that is not tied to one company or institution. https://open-pharma.herokuapp.com/

# 0. General overview

## Global pipeline

You are in the front-end repository of openpharma. The global project include 3 repositories :
 - Data crawlers : https://github.com/openpharma/openpharma.github.io
 - ML for search bar and data categorization : https://github.com/openpharma/openpharma_ml
 - Front-end (current repo) : https://github.com/openpharma/opensource_dashboard

## Code

App developped in Python using the framework Streamlit (https://streamlit.io/).

## Deployment - CI/CD
Docker using Github Action on Heroku 
Probably move to AWS BeansTalk or Fargate



# 1. Global structure of the repo

```bash
.
├── LM-L6-BERT (folder with BERT model for search bar)
│   └── ....... 
├── apps         (pages for the webappp)
│   ├── about.py
│   ├── activity.py
│   ├── leaderboard.py
│   ├── openissues.py
│   └── pharmapackages.py
├── python_functions       (functions to handle dataframe and add custom html/css)
│   ├── df_activity.py
│   ├── df_leaderboard.py
│   ├── df_openissues.py
│   ├── df_pharmpack.py
│   └── search_engine.py
├── style                  (CSS fo custom html components)
│   ├── about.css
│   ├── activity.css
│   ├── header.css
│   ├── leaderboard.css
│   ├── openissues.css
│   └── pharmapackages.css
├── Dockerfile
├── README.md
├── app.py    (streamlit app main page -> entrypoint to naviagte through menu)
├── requirements.txt
├── setup.sh
└── utils.py  (Menu definition)
```

## Deployment on Heroku - Test



Using dockerfile


## Aims

* Help me find a relevant package by 'NLP' to define topics/categories (e.g. all the table packages, or all ADaM packages)
* Help me find 'similar' packages to one of interest
* Help me understand more about this package (e.g. OS health, riskmetric scores, who works on it)
* Help people discover where they could contribute to packages (e.g. open issues)

The following project is trying to define the final scope: https://github.com/openpharma/opensource_dashboard/projects/1



