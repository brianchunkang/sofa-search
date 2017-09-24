# Sofa Search

###### Thousands of sofas out there. Find your match in 20.

SofaSearch is a web application that helps users look for their dream sofa 🛋.

Try me on Heroku! - http://sofa-search.herokuapp.com

## Hack The North 2017 submission by:
* Lawrence Pang
* Nicholas Vadivelu 
* Victor Yu

## Tech Stack
* Python + Flask backend
* Machine learning tools Keras + Tensorflow
* Web page designed with HTML, CSS (with CSS transitions), & jQuery

## Dependencies
* Flask==0.12.2
* requests==2.18.4
* numpy==1.13.1
* pillow==2.7.0
* keras==2.0.8
* tensorflow==1.2.1

## Design Details
* A scraper retrieves sofa data from an Ikea website: including pictures, price, and link
* A sofa is presented to a user
  1. User can rate a sofa with a star number scale 
  2. User has the option to purchase - taking them to the site so they can purchase
  3. Save a list of sofas the user is interested in through a ‘save’ button
* This process goes on until the user discovers their one true sofa

## Local Deployment
* Install Python 3.6.2 (https://www.python.org/downloads/)
* Install virtualenv with ```pip install virtualenv```
* Navigate to your project root and create a virtualenv with ```virtualenv my_project```
* Activate your virtual environment with ```source my_project/bin/activate```
* Install dependencies in the environment with ```pip install -r requirements.txt```
* Start the application with ```heroku local web```
* View the application on localhost:5000
* Stop running the application: Ctrl-C
* Exit virtual environment: ```deactivate```
