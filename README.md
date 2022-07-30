# new_ml_project

Creating conda environment

conda create -p venv python==3.10.4 -y
conda activate venv/
OR

conda activate venv
pip install -r requirements.txt
To Add files to git

git add .
OR

git add <file_name>
Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status

git status
To check all version maintained by git

git log
To create version/commit all changes by git

git commit -m "message"
To send version/changes to github

git push origin main
To check remote url

git remote -v
To setup CI/CD pipeline in heroku we need 3 information

HEROKU_EMAIL = 
HEROKU_API_KEY = <>
HEROKU_APP_NAME = 
BUILD DOCKER IMAGE

docker build -t <image_name>:<tagname> .
Note: Image name for docker must be lowercase

To list docker image

docker images
Run docker image

docker run -p 5000:5000 -e PORT=5000 f8c749e73678
To check running container in docker

docker ps
Tos stop docker conatiner

docker stop <container_id>

# California-Housing-Price-Estimation

<div id="top"></div>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">California-Housing-Price-Estimation</h3>

  <p align="center">
    Machine Learning Project
    <br />
    <a href="https://github.com/vyankateshbhimrathi/California-Housing-Price-Estimation"><strong>Explore the Repo »</strong></a>
    <br />
    <br />
    <a href="https://github.com/vyankateshbhimrathi/California-Housing-Price-Estimation/blob/main/app.py">View Flask app code</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project
* Using Data Science and Machine learning, we can predict house prices which are located in california using various features.
* Building a **Flask App** hosted on **Heroku**.
* **Sklearn** for pre-processing and Model Building
* Pandas, Numpy, Matplotlib for csv reading, Data Processing, Data Cleaning, Visualization etc.

## Deployed app
[LINK TO HEROKU APP](https://ml-regression-california.herokuapp.com/)

<!-- GETTING STARTED -->
## Introduction
*  The dataset for **California-Housing-Price-Estimation** is taken from **Kaggle**. The dataset contains 16512 observations (rows) and 10 features (columns). 
*  The dataset contains 9 numerical features and 1 nominal features.  


### Exploratory Data Analysis
* In this step, we will apply Exploratory Data Analysis (EDA) i.e., univariate, bivariate and multivariate analysis to extract insights from the data set to know which features have contributed more in predicting insurance premium by performing Data Analysis using Pandas and Data visualization using Matplotlib & Seaborn. 
* It is always a good practice to understand the data first and try to gather as many insights from it.

### Model Building 
* This is a regression problem where we need to predict premium based on given sample attributes.
* Models used : **Linear Regression, Random forest Regressor.**

### Model Selection
* Hyperparameter tuning is done on each algorithm.
* Based on the model accuracy, rmse of train and test data machine learning algorithm selected.



### Flask
* Importing the Flask module and creating a Flask web server from the Flask module.
* Create an object **app** in flask class with `__name__` which represents current app.py file.
* Create `/` route to render default page html.
* Create a route `/predict` to get user input for regression. 
* Run the flask app with `app.run()` code.

### Heroku Deployment
* Create new repo in Github and push all the data using `Git`.
* Login to heroku and create the app.
* Using github actions we can automate the deployment each time we update the github.

### **Technologies used**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)


### **Tools used**
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)



<!-- CONTACT -->
## Contact
[[VYANKATESH BHIMRATHI | LinkedIn]][reach_linkedin_1]


<!-- MARKDOWN LINKS  -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-url]: https://linkedin.com/in/linkedin_username

<!-- Tools Used -->
[git]: https://git-scm.com/
[github]: https://github.com/
[heroku]: https://www.heroku.com/
[python]: https://www.python.org/
[flask]: https://flask.palletsprojects.com/en/2.1.x/
[sklearn]: https://scikit-learn.org/stable/

<!--contact-->
[reach_linkedin_1]: https://www.linkedin.com/in/vyankatesh-bhimrathi-1461a4140/
