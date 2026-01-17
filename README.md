# Thyroid Nodule Malignancy Prediction System

This system is an AI diagnostic system developed based on large-scale, multi-center data. The user clicks the link: [https://thyroid-prediction-model-au6obvkv2srb5qpncfzfab.streamlit.app/](https://thyroid-prediction-model-au6obvkv2srb5qpncfzfab.streamlit.app/ "https://thyroid-prediction-model-au6obvkv2srb5qpncfzfab.streamlit.app/"), input simple clinical information and description of thyroid nodule ultrasound, can obtain the diagnosis of benign and malignant thyroid ultrasound AI and the size of the probability. Due to its light weight and simplicity, it can be used for large-scale, grassroots screening of benign and malignant thyroid nodules.

---

# 💻Repository Overview

This repository contains four main folders: Crude model, Feature selection, Model optimization, and Web Application

These codes are developed and run based on python 3.10, covering the entire process of system development, optimization, evaluation, etc. Please note that, for the sake of protecting patient privacy, we have only provided some simulation data and results, while hiding some intermediate results that we believe may disclose patient privacy. However, this does not affect the logic of the code or the development of the system. If you have any special requirements or other questions, please contact the author. Thank you for your understanding.

Next, a brief introduction to each part will be given.

## 📁Crude model

The Crude model directory is used for the development of the AI system using all features before feature screening to initially understand the overall performance and observe if there is any room for further optimization. This folder includes:

* 1.code folder: It records the codes for data reading, processing, encoding, model training, hyperparameter optimization, evaluation, as well as the implementation of related visualization functions such as ROC and PR curves in ipynb format.
* 2.input folder: Internal validation and external validation data stored in excel files.
* 3.output folder: Stores the results output by the code. Please note that to protect patient privacy, only the test sets of various scales and the results of external validation sets are displayed here.

## 📁Feature selection

The Feature selection directory is used after the training of the Crude model is completed, in order to further identify important features and simplify the model to facilitate its application. This folder includes:

1.code folder: It records the data reading, processing, and encoding in ipynb format, as well as feature screening methods including mRMR, Boruta, BorutaSHAP, Lasso, and ElasticNet.

2.output folder: Store the important features filtered and their sorting in an excel file.

## 📁Model optimization

Model optimization is the process of developing an AI system again using the important features that have been filtered after Feature selection. This folder includes:

* 1.code folder: It records the code for data reading, processing, encoding, model training, hyperparameter optimization, evaluation, ROC, PR curve and other related visualization functions, as well as SHAP interpretation and other function implementations in ipynb format.
* 2.input folder: Internal validation and external validation data stored in excel files.
* 3.output folder: Stores the results output by the code. Please note that to protect patient privacy, only the test sets of various scales and the results of external validation sets are displayed here.

## 📁Web Application

A Web Application is developed by selecting the best-performing training Model through Model optimization and based on the Streamlit framework. This folder includes:

* Web.py: Stores the relevant code for developing Web applications based on the Streamlit framework

---

# 📚 Citation

If you use this system in your research, please cite the following manuscript:

> Xiaomeng Jia,Runhong Chen,et al.*Towards Transparent and Deployable AI: A Multicenter Validation and Clinical Translation of an Interpretable Machine Learning Model for Thyroid Nodule Assessment.(Submitted).*

---

# ✉️ Contact & Support

If you have any questions, please feel free to contact the author at any time and we will reply as soon as possible.
