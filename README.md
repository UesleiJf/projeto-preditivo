# README

## Description

This project aims to: analyze a database and through Machine Learning algorithms make assertive predictions for decision making.

Algorithms used: Linear Regression, Random Forest Regressor, Naive Bayes.

The project is divided into 3 parts:
- Static Analysis
- Choice of the best algorithm for problem solving
- Creating a Container Docker for use via client (entering data to see the forecast).

### Work environment details

* OS: Ubuntu 16.04 LTS
* IDE: Jupyter Notebook / Jupyter Lab
* Database: sqlite3

### Library Versions

* Python:   3.6
* Pickle
* Numpy
* Pylab
* Pandas
* Seaborn
* Statsmodels
* Matplotlib
* Sklearn

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

To run the Project:

    go/to/path/to/the/project

    jupyter notebook

Run the command below to update the pip and avoid dependency conflicts when installing requirements.txt

    pip install --upgrade pip

Navigate to the directory /systemcall/ and execute the commands below

A tab will open in your browser and you can browse the project.

### Creating a database.

You must create a CSV file with the following columns and data types:

id_socio: int
status: String
qtde_em_aberto: int
qtde_em_dia: int
qtde_em_atraso: int
qtde_frequencia_ano: int

Created by: Ueslei JF da Silva.
