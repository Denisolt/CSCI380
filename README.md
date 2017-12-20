# Introduction to Software Engineering Project:

## Abstract:
To design an application for professors of different colleges to generate exams with 10 different question types, with a feature to print out the exams in 3 different formats, one of which is BlackBoard format, ensuring integration and compatibility with the most used academic tool.
## Introduction:
The main purpose of this project was to design and develop a system for professors of different colleges that generates different types of question for examination. The system will prompt the user to login using his credentials or create a new account, it also allows user to pick the college and its department or add a new college and its department, following which the user will have an option of either selecting an already entered course or adding a new course. The selected course will feature already entered exams and an option to create a new examination. This project was called the Examinator by the software engineering team, since it performs all the needed tasks of the professor and is built to improve and create an easier workflow of creating exams. 
## How to run the application:
In order to run the application from your own device, you need to ensure you have following installed:
  - Git
  - Python 3.5
  - pip
  - Virtual environments </br>

Open the terminal and type: </br>
`git clone https://github.com/Denisolt/CSCI-380.git` </br>
`cd CSCI-380-master` </br>
Create and activate a virtual environment: </br>
`virtualenv local` </br>
`source local/bin/activate` </br>
Now install the requirements from txt file by typing in terminal:</br>
`pip install -r requirements.txt`</br>
Our web application is using a database which is hosted on Heroku, this means that it will actually have data even when you run it on your device from scratch. To create a new super user type in terminal:</br>
`python manage.py createsuperuser`</br>
Now run the application in your local network by typing:</br>
`python manage.py runserver`</br>
Go to your local host in the browser or type: 127.0.0.1</br>
