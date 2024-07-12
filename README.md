ETL Pipeline
==============================

ETL task from d2k tech

## Description
    ├── notebooks          <- Jupyter notebooks
    ├── reports            
    │   └── figures        <- EDA graphics and figures are here
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           
    │   │   └── fetch_data.py   <- Script to fetch data from data source (https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
    │   │
    │   ├── features       
    │   │   └── build_features.py     <- Scripts to turn raw data into features
    │   │
    │   ├── load         
    │   │   ├── load_data.py     <- Scripts to load data into SQLite database
    │   │   └── SQLQuery.sql     <- SQL scripts to perform statistical analysis

Project Structure
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third-party sources
    │   ├── processed      <- The final, processed data for further usage.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Script to fetch data from data source
    │   │   └── fetch_data.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features
    │   │   └── build_features.py
    │   │
    │   ├── load         <- Scripts to load data into database
    │   │   ├── load_data.py
    │   │   └── SQLQuery.sql <- SQL scripts to perform statistical analysis
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
