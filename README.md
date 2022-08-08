# Open pharma dashboard

The objective of openpharma is to provide a neutral home for open source software related to pharmaceutical industry that is not tied to one company or institution. https://open-pharma.herokuapp.com/

📧 For any questions, feel free to contact me at the adress : mathieu.cayssol@gmail.com

# 0. General overview

## Global pipeline

You are in the front-end repository of openpharma. The global project include 3 repositories :
 - ⚙️ Data crawler : https://github.com/openpharma/openpharma.github.io
 - 🤖 ML for search bar and data categorization : https://github.com/openpharma/openpharma_ml
 - 📊 Front-end (current repo) : https://github.com/openpharma/opensource_dashboard


<img src="https://user-images.githubusercontent.com/49449000/183419490-7ed52bc9-2941-4b2a-8abf-fc7496b432ac.png" width="600"/>


# 1. Techonologies and structure of the repo

We are using Python 3.9.x and [Streamlit](https://streamlit.io/) to create the webapp. We also added custom html/css using [Boostrap 5.2](https://getbootstrap.com/). The repository follows the current organisation :

```bash
.
├── LM-L6-BERT  📁(folder with BERT model - used for make inference with the search bar)
│   └── ....... 
├── apps         📁(pages for the webapp)
│   ├── about.py
│   ├── activity.py
│   ├── leaderboard.py
│   ├── openissues.py
│   └── pharmapackages.py
├── python_functions       📁 functions to handle dataframe and add custom html/css
│   ├── df_activity.py
│   ├── df_leaderboard.py
│   ├── df_openissues.py
│   ├── df_pharmpack.py
│   └── search_engine.py
├── style                  📁 CSS fo custom html components
│   ├── about.css
│   ├── activity.css
│   ├── header.css
│   ├── leaderboard.css
│   ├── openissues.css
│   └── pharmapackages.css
├── Dockerfile     🐳(Dockerfile for deployment)
├── README.md
├── app.py    📄(streamlit app main page -> entrypoint to naviagte through menu)
├── requirements.txt
├── setup.sh
└── utils.py  📄(Menu definition)
```

# 2. Run the app locally

Prerequisites : 
- Python >= 3.9


```bash
git clone https://github.com/openpharma/opensource_dashboard.git
cd <PATH_TO_THE_CLONE>
```

In your virtual environnement :
```bash
pip install -r requirements.txt
```
```bash
streamlit run app.py
```


## Aims

* Help me find a relevant package by 'NLP' to define topics/categories (e.g. all the table packages, or all ADaM packages)
* Help me find 'similar' packages to one of interest
* Help me understand more about this package (e.g. OS health, riskmetric scores, who works on it)
* Help people discover where they could contribute to packages (e.g. open issues)

The following project is trying to define the final scope: https://github.com/openpharma/opensource_dashboard/projects/1



