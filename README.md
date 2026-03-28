# Real-time-Phishing-Detection-System-using-Machine-Learning-
🔍💻 Real-Time Phishing Detection System using Machine Learning 🛡️📧. This system leverages machine learning to analyze and classify URLs, emails, or web content. It detects phishing attempts by identifying patterns and anomalies, providing instant alerts to enhance cybersecurity and protect users from online threats.

PHISHING DETECTION SYSTEM

![Output screenshot 4](https://github.com/user-attachments/assets/aa34f9f8-080f-4c9a-8e2d-845354f84591)
![Output screenshot 3](https://github.com/user-attachments/assets/3a638d0b-62a3-45c5-a6a1-4120aa001060)
![Output screenshot 2](https://github.com/user-attachments/assets/8113108b-2564-4a39-b5eb-246195e3a765)
![Output screenshot 1](https://github.com/user-attachments/assets/642b4255-4013-44cd-94c6-1bd6e96d1e08)


# TABLE OF CONTENT :-
Introduction
Installation
Directory Tree
Result
Conclusion

#Introduction

The Internet has become an indispensable part of modern life. However, its widespread use has also created opportunities for malicious activities such as phishing. Phishing is a cyberattack technique where attackers attempt to deceive users through social engineering or by creating fraudulent websites that closely resemble legitimate ones. These attacks aim to steal sensitive information such as login credentials, account IDs, and passwords from individuals and organizations.

Although several techniques have been developed to detect phishing websites, attackers continuously evolve their strategies to bypass these systems. Machine Learning (ML) has emerged as one of the most effective approaches for phishing detection, as it can identify patterns and common characteristics present in malicious URLs. This project leverages machine learning techniques to analyze and classify URLs as either safe or phishing based on their features.

#Installation

The project is developed using Python 3.6.10.

If Python is not installed on your system, you can download and install it from the official Python website. Ensure that you are using a compatible or updated version of Python, and upgrade pip if necessary.

To install all required dependencies, navigate to the project directory after cloning the repository and run:

pip install -r requirements.txt
Project Structure (Directory Tree)
├── pickle
│   ├── model.pkl
├── static
│   ├── styles.css
├── templates
│   ├── index.html
├── Phishing URL Detection.ipynb
├── Procfile
├── README.md
├── app.py
├── feature.py
├── phishing.csv
├── requirements.txt
Technologies Used
Python
Machine Learning Algorithms
Flask (for web application)
HTML, CSS (for frontend)
Jupyter Notebook (for experimentation and analysis)
Pandas, NumPy (for data processing)
Scikit-learn, XGBoost, CatBoost (for model building)
Results

The performance of various machine learning models used for phishing URL detection is summarized below:

ML Model	Accuracy	F1 Score	Recall	Precision
Gradient Boosting Classifier	0.974	0.977	0.994	0.986
CatBoost Classifier	0.972	0.975	0.994	0.989
XGBoost Classifier	0.969	0.973	0.993	0.984
Multi-layer Perceptron	0.969	0.973	0.995	0.981
Random Forest	0.967	0.971	0.993	0.990
Support Vector Machine	0.964	0.968	0.980	0.965
Decision Tree	0.960	0.964	0.991	0.993
K-Nearest Neighbors	0.956	0.961	0.991	0.989
Logistic Regression	0.934	0.941	0.943	0.927
Naive Bayes Classifier	0.605	0.454	0.292	0.997

Among all models, the Gradient Boosting Classifier achieved the highest accuracy of 97.4%, making it the most effective model for this task.

# Feature Importance

Feature analysis revealed that certain attributes significantly influence phishing detection. The most important features include:

HTTPS usage
Anchor URL behavior
Website traffic

<img width="638" height="441" alt="image" src="https://github.com/user-attachments/assets/157b02be-8c88-4a57-936e-65b361d8c32c" />


These features play a crucial role in determining whether a URL is legitimate or malicious.

# Conclusion

This project demonstrates the effectiveness of machine learning techniques in detecting phishing URLs. Through exploratory data analysis and model experimentation, multiple algorithms were evaluated to identify the most accurate and reliable approach.

The study highlights the importance of feature engineering and model tuning in improving classification performance. Among the models tested, the Gradient Boosting Classifier delivered the best results, achieving an accuracy of 97.4% and significantly reducing the risk of misclassification.

Overall, this project provided valuable insights into phishing detection mechanisms and enhanced understanding of how machine learning models can be applied to real-world cybersecurity challenges.
