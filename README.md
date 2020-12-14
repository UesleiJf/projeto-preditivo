# Description

This project aims to: analyze a database and through Machine Learning algorithms make assertive predictions for decision making.

Algorithms used: Linear Regression, Random Forest Regressor, Naive Bayes and Gradient Boosting.

The project is divided into 3 parts:
- Static Analysis
- Choice of the best algorithm for problem solving
- Creating a Container Docker for use via client (entering data to see the forecast). Para executar essa parte do projeto veja o arquivo README.md da Part03.

### Work environment details

* OS: Ubuntu 16.04 LTS
* IDE: Jupyter Notebook / Jupyter Lab
* Database: sqlite3
* Docker

### Library Versions

* Python
* Pickle
* Numpy
* Pylab
* Pandas
* Seaborn
* Statsmodels
* Matplotlib
* Sklearn
* Flask
* Joblib

OBS: It is mandatory to install each library mentioned above.
For the installation we use pip install...

### Installation

First, you need to clone this project from Bitbucket:

git clone https://github.com/UesleiJf/projeto-preditivo

This project run under Python 3.6

After clone, you need to install Jupyter Notebook

    pip3 install jupyterlab

For full documentation for venv, you can see here:
https://jupyter.org/install

To run the Project go/to/path/to/the/project and execute

    jupyter notebook 
    
OR

    jupyter lab


A tab will open in your browser and you can browse the project:

http://localhost:8888

### Creating a database.

You must create a CSV file with the following columns and data types:

* id_socio: int
* status: String
* qtde_em_aberto: int
* qtde_em_dia: int
* qtde_em_atraso: int
* qtde_frequencia_ano: int


#### Created by: Ueslei José Ferreira da Silva.
#### 2020
